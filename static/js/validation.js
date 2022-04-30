function validation(username) { 
    var data = {}; 
    var phone_number = $('#number').val();
    var confirmation = $('#confirmation').val();
    data['phone_number'] = parseInt(phone_number, 10);

    if (phone_number == confirmation) {
        $.ajax({ 
            type : "PUT", 
            url : `http://ec2-44-204-141-35.compute-1.amazonaws.com:3200/${username}/phone_number`, 
            data: JSON.stringify(data), 
            contentType: 'application/json;charset=UTF-8', 
            success: function(result) { 
                alert("Número actualizado con éxito!");
            },
            error: function(result) {
                alert("El número ingresado no tiene un formato válido!");
            }
        });
    } else {
        alert("Los números no coinciden!");
    }
}