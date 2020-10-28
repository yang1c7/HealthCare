var $navigation = $('#navigation');
var $showArea = $('#showArea');
var $appointments = $('#appointments');
var $naviArray = $('.naviItems');
var $showitems = $('.shownItems');
var $time = $('#time');
var $title = $('#title h1');
var $bg = $('body');
var $mask = $('#mask');
var username = $('#username').html();
var $changeUname = $('#changeUname');
var $changeEma = $('#changeEma');
var $uninput = $('#uninput');
var $emailinput = $('#emailinput');

var $fninput = $('#fninput');
var $changefn = $('#changefn');

var $lninput = $('#lninput');
var $changeln = $('#changeln');

var $ageinput = $('#ageinput');
var $changeage = $('#changeage');

var $addrinput = $('#addrinput');
var $changeaddr = $('#changeaddr');

var $genderselect = $('#genderselect');
var $changegender = $('#changegender');

var error = $('#error').html();
var $mes = $('#message');
if(error == 1){
    $mes.fadeIn(800);
}

$navigation.fadeIn(1000);
$showArea.fadeIn(1000);
$appointments.fadeIn(1000);

$naviArray.click(function(){
    var index = this.getAttribute("value");
    $naviArray.each(function(){
        if(index === this.getAttribute("value")){
            $(this).css('background-color', 'rgba(0, 0, 0, 0.3)');
        }else{
            $(this).css('background-color', 'rgba(0, 0, 0, 0)');
        }
    });
    $showitems.each(function(){
        if(index === this.getAttribute("value")){
           // $(this).css('display', 'block');
           $(this).fadeIn(1000);
        }else{
           // $(this).css('display', 'none');
           $(this).fadeOut(1000);
        }
    });
});

setInterval(() => {
    var myDate = new Date();
    var time = myDate.toLocaleString();
    $time.html(time);
    var hour = myDate.getHours();

    if( hour >= 6 && hour < 12 ){
        $title.html('Good morning, ' + username);
        $bg.css({
            "background-image": "url('../../static/myapp/img/morning.jpg')",
            "background-repeat":"no-repeat",
            "background-size": "100%"
        });
        $mask.css("opacity", '0.5');
    }else if(hour >= 12 && hour < 18 ){
        $title.html('Good afternoon, ' + username);
        $bg.css({
            "background-image": "url('../../static/myapp/img/afternoon.jpg')",
            "background-repeat":"no-repeat",
            "background-size": "100%"
        });
        $mask.css("opacity", '0.5');
    }else if(hour >= 18 && hour < 24){
        $title.html('Good evening, '  + username);
        $bg.css({
            "background-image": "url('../../static/myapp/img/evening.jpg')",
            "background-repeat":"no-repeat",
            "background-size": "100%"
        });
        $mask.css("opacity", '0.3');
    }else{
        $title.html('Good night, ' + username);
    }
}, 1000);

// $changeUname.html().click(function () {
//     $uninput.css('display', 'block');
//     $changeUname.css('display', 'none');
//     return  false;
// });
// $changeEma.click(function () {
//     $emailinput.fadeIn(800);
//     $changeEma.fadeOut(800);
//     return  false;
// });
var showusername = function () {
     $changeUname.fadeOut(800, function () {
         $uninput.fadeIn(800);
         $mes.fadeOut(800);
     });
}
var showemail = function () {
     $changeEma.fadeOut(800, function () {
        $emailinput.fadeIn(800);
     });
}

var showfirstname = function () {
     $changefn.fadeOut(800, function () {
        $fninput.fadeIn(800);
     });
}

var showlastname = function () {
     $changeln.fadeOut(800, function () {
        $lninput.fadeIn(800);
     });
}

var showage = function () {
     $changeage.fadeOut(800, function () {
        $ageinput.fadeIn(800);
     });
}

var showaddr = function () {
     $changeaddr.fadeOut(800, function () {
        $addrinput.fadeIn(800);
     });
}

var showgender = function () {
     $changegender.fadeOut(800, function () {
        $genderselect.fadeIn(800);
     });
}

