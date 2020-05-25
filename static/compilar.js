$(document).ready(
    $('#idCompilar').on('click',function(event){
        $.ajax({
            type: "POST",
            url: "localhost:3000/compilar",
            data: {"texto":"el codigo"},
            dataType: "json",
            success: function (response) {
                alert('enviado')
            }
        });
    })
)