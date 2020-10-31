from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quiz, Art, Answered
from .forms import RegisterForm, ArtSubmissionForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login


# Create your views here.
def home(response):
    return render(response, "home/home_page.html")


@login_required(login_url="/login")
def quizzes(response):
    try:
        answered = Answered.objects.filter(user=response.user).values('quiz')
        quiz = Quiz.objects.exclude(id__in=answered)

        return render(response, "home/quiz.html", {"quiz": quiz})
    except:
        quiz = Quiz.objects.all()

        return render(response, "home/quiz.html", {"quiz": quiz})

@login_required(login_url="/login")
def art(response):
    art = Art.objects.filter(approved=True)

    return render(response, "home/art.html", {"posts": art})


@login_required(login_url="/login")
def like_art(response, id):
    art = Art.objects.get(pk=id)
    art.likes.add(response.user)
    return HttpResponse(art.get_count())


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(response, new_user)
            return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})

@login_required(login_url="login/")
def submit_art(response):
    form = ArtSubmissionForm()
    if response.method == "POST":

        form = ArtSubmissionForm(response.POST, response.FILES)

        if form.is_valid():
            form.instance.user = response.user
            form.save()

            return redirect("/")

    else:
        form = ArtSubmissionForm()

    return render(response, "home/art_submit.html", {"form": form})


def mod_page(response):
    posts = Art.objects.filter(approved=False)
    if response.user.is_superuser:
        return render(response, "home/dev_page.html", {"posts": posts})
    else:
        return HttpResponse("Access denied")

@login_required(login_url="/login")
def approve_post(response, id):
    post = Art.objects.get(pk=id)
    post.approved = True
    post.save()
    return HttpResponse(1)


def quiz_page(response, id):
    quiz = Quiz.objects.get(pk=id)

    return render(response, "home/quiz_page.html",{"quiz": quiz})

def video(response):
    return render(response, "home/video.html")

def article_page(response):
    return render(response, "home/article.html")

def quiz_submit(response, id):
    quiz = Quiz.objects.get(pk=id)
    var = int(response.POST.get("choice"))
    answered = Answered(user=response.user, quiz=quiz)
    answered.save()
    if var == quiz.correct:
        return HttpResponse(1)
    return HttpResponse(0)
