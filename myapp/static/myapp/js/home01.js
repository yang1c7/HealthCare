var $login_a = $("#login-a");
var $bgContainer = $('#bgContainer');
var $wrap = $('#wrapper');
var $start = $('#start');
var $register_a = $('#register-a');
var viewportWidth = $(window).width()

var loginLeft = $login_a.css('left');
var login_aWidth = $login_a.width();
var register_aWidth = $register_a.width();
var LGoToMid = (viewportWidth - login_aWidth)/2 + 438;
var RGoToMid = (viewportWidth - register_aWidth)/2 + 480;
$login_a.click(function(){
    $login_a.attr("disabled",true).css("pointer-events","none");
    $register_a.attr("disabled",true).css("pointer-events","none");
    $bgContainer.fadeOut(800);
    $wrap.fadeOut(800);
    $start.fadeOut(800);
    $register_a.fadeOut(800);
    $login_a.stop().animate({
        //left: LGoToMid + "px",
        left: "1065px",
        top: '80px',
        'font-size':'70px'
    }, 1000, "swing", function(){
        //$loginForm.fadeIn(1000);
         window.location.href = 'login';
    });
});

$register_a.click(function(){
    $register_a.attr("disabled",true).css("pointer-events","none");
    $login_a.attr("disabled",true).css("pointer-events","none");
    $bgContainer.fadeOut(800);
    $wrap.fadeOut(800);
    $start.fadeOut(800);
    $login_a.fadeOut(800);
    $register_a.stop().animate({
        //left: RGoToMid + "px",
        left: "1040px",
        top: '60px',
        'font-size':'60px'
    }, 1000, "swing", function(){
        //$registerForm.fadeIn(1000);
        window.location.href = 'register';
    });
});
