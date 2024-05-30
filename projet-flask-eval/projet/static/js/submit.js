$(document).ready(function() {
    $('#paiement').submit(function(event) {
        event.preventDefault();

        console.log("heheheheh")

        var formData = new FormData($(this)[0]);

        $.ajax({
            url: '/add-paiement',
            type: 'POST',
            dataType: 'json',
            processData: false,
            contentType:false,
            data: formData,
            success: function(response) {
                swal("Paiement valide !!", response.message, "success")
            },
            error: function(xhr, status, error) {
                sweetAlert("Paiement invalide", xhr.responseJSON.error, "error")
            }
        });

    });
});

