"""culture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views as home
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib.auth.urls import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home, name="home"),
    path('quiz', home.quizzes, name="quiz"),
    path('art', home.art, name='art'),
    path('like/<int:id>', home.like_art),
    path('', include("django.contrib.auth.urls")),
    path('register', home.register),
    path('submit', home.submit_art, name='submit'),
    path('dev', home.mod_page),
    path('approvePost/<int:id>', home.approve_post, name="approve"),
    path('quiz_page/<int:id>', home.quiz_page, name="quiz_page"),
    path('video/', home.video, name="video"),
    path('article/', home.article_page, name="article"),
    path('quizSubmit/<int:id>', home.quiz_submit)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

