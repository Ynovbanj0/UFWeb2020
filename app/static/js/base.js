// var id;

function signIn() {
    $('.signInSection').css('display') === "none" ? $('.signInSection').css('display', "flex") : $('.signInSection').css('display', "none");
}


// Non fonctionnel
// function youhou() {
//     var degree = 0;
//     id = setInterval(function() {
//         $('.navLogo').css({ 'transform': 'rotate(' + degree + 'deg)' });
//         degree += 1;
//         console.log(degree);
//         console.log($('.navLogo').css('transform'));
//         if (degree == 360) { clearInterval(id); };
//     }, 1);
// }

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
    // Si tu es pas un connard, tu mets a jour le nom des classes pour que ca passe crème incognito dans maman
})


// Essayer d'animer avec l'ajout d'une classe pour le display none.
// Sinon nique ses grand morts de ses parents les fils d'insceste de baleines évolution directs de la péniciline et d'une micose.