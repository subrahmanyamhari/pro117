//Create date variable


//Load HTML DOM

//Define variable to store predicted emotion


//HTML-->JavaScript--->Flask
//Flask--->JavaScript--->HTML

//jQuery selector and click action

$(function () {
    $("#predict_button").click(function () {
        //AJAX call
        var input_data = {"text":$("#text").val()}
        $.ajax({
            type:"POST",
            url:"/predict-emotion",
            data:JSON.stringify(input_data),
            dataType:"json",
            contentType:"application/json",

            success:function(result){
                predict_emotion = result.data.predict_emotion()
                console.log(predict_emotion)
                $("#prediction").html(predict_emotion)
            },
            error:function(result){
                alert("bad")
            }
        });
    });
})

