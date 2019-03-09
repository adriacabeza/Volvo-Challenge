function showMenu() {
    if ($('.menu').css("display") != "none") {
        $('.menu').css("display", "none");
    }
    else{
        $('.menu').css("display", "block");
        $('.menu').addClass('animated bounceIn');
    }
}
