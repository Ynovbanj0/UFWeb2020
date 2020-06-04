function signIn() {
    $('.signInSection').css('display') === "none" ? $('.signInSection').css('display', "flex") : $('.signInSection').css('display', "none");
}

jQuery(function($) {
    $('.header-nav__wrapper').on('click', function() {
        $('.nav--responsive').toggleClass("nav--responsive__active", true).toggleClass("nav--responsive", false);
        $('.overlay').toggle();
        setTimeout(function() {
            $('.overlay').addClass("is-open");
        }, 300);
        $('.header-nav-burger').addClass('is-animate');
        $('body').addClass('overflow');
    });
    $('.overlay').on('click', function() {
        $('.nav--responsive__active').toggleClass("nav--responsive__active", false).toggleClass("nav--responsive", true);
        $('.overlay').removeClass("is-open");
        setTimeout(function() {
            $('.overlay').toggle();
        }, 300);
        $('.header-nav-burger').removeClass('is-animate');
        $('body').removeClass('overflow');
    });
})



$('.addToCard').click(function() {
    var prodId = $('.addToCard').attr("id");
    jQuery.ajax({
        type: 'GET',
        url: window.origin + '/addToCard' + '/' + prodId,
        dataType: 'JSON',

        success: function(code_html, statut) {
            console.log("Well added to comments.");
        },

        error: function(resultat, statut, erreur) {
            console.log("Can not add it to comments.");
        },
        complete: function(resultat, statut) {
            document.location.reload(true);
        }
    });
});