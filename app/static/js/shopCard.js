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