$(document).ready(function(){
    function getCookie(name){
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
    const csrftoken = getCookie('csrftoken');
    $(".likeButton").on('click', function(){

        var id = $(this).val()
        $.ajax({
            url: "/like/" + id,
            data: {
                csrfmiddlewaretoken: csrftoken,
                id: id

            },
            type: "post",
            success: function(response){

                window.location.reload()
            }



        })



    })

    $(".approveButton").on('click', function(){
        var id = $(this).val()


         $.ajax({
            url: "approvePost/" + id,
            data: {
                csrfmiddlewaretoken: csrftoken,
                id: id

            },
            type: "post",
            success: function(response){
                alert("Approved!")
                window.location.reload()
            }

         })

    })

    $(".quizSubmit").on('click', function(){
        var radioValue = $("input[name='quizSelection']:checked").val()
        var id = $(this).val()
        $.ajax({

         url: "/quizSubmit/" + id,
         data: {
            csrfmiddlewaretoken: csrftoken,
            choice: radioValue
         },
         type: "post",
         success: function(result){
            if(result == 1){
                alert("Correct")
            }
            else{
               alert("Wrong")

            }
            window.location.reload()
         }


        })


    })
})


