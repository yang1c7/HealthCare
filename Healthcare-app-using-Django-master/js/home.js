var $login_a = $("#login-a"); 
var $bgContainer = $('#bgContainer');
var $wrap = $('#wrapper');
var $start = $('#start');
var $register_a = $('#register-a');
var $loginForm = $('#loginForm');
var $registerForm = $('#registerForm');
var $back = $('#back');
var $back0 = $('#back0');
var loginGoBackLeft, registerGoBackLeft;
var viewportWidth = $(window).width();
var viewportHeight = $(window).height();

setTimeout(function(){
var $items = $('.item');
console.log($items);
$($items[0]).fadeIn(300);
setTimeout(() => {
    flash($($items[0]), 30, 0.5, true);
}, 3700);
setTimeout(function(){$($items[1]).fadeIn(300);}, 800);
setTimeout(function(){
    flash($($items[2]), 50, 0.1, true);
    $($items[2]).fadeIn(300);
}, 1600);
setTimeout(function(){
    flash($($items[3]), 31, 0.1, false);
    setTimeout(() => {
        flash($($items[3]), 50, 0.2, true);
    }, 900);
    $($items[3]).fadeIn(300);
}, 2400);

}, 1000);

setTimeout(() => {
    var x = -100;
    var itemInterval = setInterval(() => {
        $wrap.css('margin-top', x);
        x = x - 8;
        if(x <= -200)
            clearInterval(itemInterval);
    }, 10);
    $start.fadeIn(400);

    setTimeout(() => {
        $register_a.fadeIn(400);

        setTimeout(() => {
            var left = $register_a.position().left;
            loginGoBackLeft = left;
            var RegInterval = setInterval(() => {
                $register_a.css('left', left);
                left += 10;
                registerGoBackLeft = left;
                if(left >= 1070)
                clearInterval(RegInterval);
            }, 10);
            $login_a.fadeIn(400);
        }, 400);
    }, 800);

    
    
   
}, 6000);

function flash($ele, times, x, on){
var flag = true;
var count = 0;
var intv = setInterval(() => {
    count++;
    if(flag){
        $ele.css('opacity', x);
        flag = false;
    }else{
        $ele.css('opacity', 0);
        flag = true;
    }
    if(count == times){
        if(on)
            $ele.css('opacity', 1);
        else
            $ele.css('opacity', 0);
        clearInterval(intv);
    }
    
}, 10);
}

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
    $login_a.animate({ 
        left: LGoToMid + "px",
        top: '80px',
        'font-size':'70px'
    }, 800, "swing", function(){
        $loginForm.fadeIn(1000);
    });
});
$back.click(function(){
    $login_a.attr("disabled",false).css("pointer-events","auto"); 
    $register_a.attr("disabled",false).css("pointer-events","auto"); 
    $loginForm.fadeOut(800);
    $login_a.animate({ 
        left: loginGoBackLeft,
        top: '50%',
        'font-size':'100px'
    }, 800, "swing", function(){
        $bgContainer.fadeIn(1000);
        $wrap.fadeIn(1000);
        $start.fadeIn(1000);
        $register_a.fadeIn(1000);
    });
});
$register_a.click(function(){
    $register_a.attr("disabled",true).css("pointer-events","none"); 
    $login_a.attr("disabled",true).css("pointer-events","none"); 
    $bgContainer.fadeOut(800);
    $wrap.fadeOut(800);
    $start.fadeOut(800);
    $login_a.fadeOut(800);
    $register_a.animate({ 
        left: RGoToMid + "px",
        top: '60px',
        'font-size':'60px'
    }, 800, "swing", function(){
        $registerForm.fadeIn(1000);
    });
});
$back0.click(function(){
    $login_a.attr("disabled",false).css("pointer-events","auto"); 
    $register_a.attr("disabled",false).css("pointer-events","auto"); 
    $registerForm.fadeOut(800);
    $register_a.animate({ 
        left: registerGoBackLeft - 10,
        top: '50%',
        'font-size':'100px'
    }, 800, "swing", function(){
        $bgContainer.fadeIn(1000);
        $wrap.fadeIn(1000);
        $start.fadeIn(1000);
        $login_a.fadeIn(1000);
    });
});