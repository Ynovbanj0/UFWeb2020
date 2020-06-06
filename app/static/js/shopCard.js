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