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
    var prodId = $(this).attr("id");
    jQuery.ajax({
        type: 'GET',
        url: window.origin + '/addToCard' + '/' + prodId,

        success: function(code_html, statut) {
            console.log("Well added to Card.");
        },

        error: function(resultat, statut, erreur) {
            console.log("Can not add it to Card.");
            console.log(erreur);
        },
        complete: function(resultat, statut) {
            document.location.reload(true);
        }
    });
});

$('.elementImg').click(function() {
    var prodId = $(this).attr("id");
    var url = window.origin + '/product' + '/' + prodId
    window.location.replace(url);
});