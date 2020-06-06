$('.shoppedLogo').click(function() {
    var url = window.origin + '/card'
    window.location.replace(url);
});

$('.imgCard').click(function() {
    var prodId = $(this).attr("id");
    var url = window.origin + '/product' + '/' + prodId
    window.location.replace(url);
});

$('.buy').click(function() {
    window.location.replace(window.origin + '/gimmeYourBankAccount');
});

$('.cardDelBtn').click(function() {
    var prodId = $(this).attr("id");
    jQuery.ajax({
        type: 'GET',
        url: window.origin + '/deleteCard' + '/' + prodId,

        success: function(code_html, statut) {
            console.log("Well deleted to Card.");
        },

        error: function(resultat, statut, erreur) {
            console.log("Can not delete it from Card.");
            console.log(erreur);
        },
        complete: function(resultat, statut) {
            document.location.reload(true);
        }
    });
});