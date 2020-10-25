var $login_a = $("#login-a"); 
var $bgContainer = $('#bgContainer');
var $wrap = $('#wrapper');
var $start = $('#start');
var $register_a = $('#register-a');
// var $loginForm = $('#loginForm');
// var $registerForm = $('#registerForm');
// var $back = $('#back');
// var $back0 = $('#back0');
var loginGoBackLeft, registerGoBackLeft;
// var viewportWidth = $(window).width();
// var viewportHeight = $(window).height();

    setTimeout(function () {
        var $items = $('.item');
        console.log($items);
        $($items[0]).fadeIn(300);
        setTimeout(() => {
            flash($($items[0]), 30, 0.5, true);
        }, 3700);
        setTimeout(function () {
            $($items[1]).fadeIn(300);
        }, 800);
        setTimeout(function () {
            flash($($items[2]), 50, 0.1, true);
            $($items[2]).fadeIn(300);
        }, 1600);
        setTimeout(function () {
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
            if (x <= -200)
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
                    if (left >= 1070)
                        clearInterval(RegInterval);
                }, 10);
                $login_a.fadeIn(400);
            }, 400);
        }, 800);


    }, 6000);

setTimeout(function(){
    window.location.href='home';
},7600)

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
