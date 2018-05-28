
(function ($) {
    "use strict";
    var mainApp = {

        main_fun: function () {
            /*====================================
            METIS MENU 
            ======================================
            $('#main-menu').metisMenu();*/

            /*====================================
              LOAD APPROPRIATE MENU BAR
           ======================================*/
            $(window).bind("load resize", function () {
                if ($(this).width() < 768) {
                    $('div.sidebar-collapse').addClass('collapse')
                } else {
                    $('div.sidebar-collapse').removeClass('collapse')
                }
            });
       },

        initialization: function () {
            mainApp.main_fun();

        }

    }

});
//calendar functions

    var monthsArray = new Array();
    monthsArray["January"] = "0";
    monthsArray["February"] = "1";
    monthsArray["March"] = "2";
    monthsArray["April"] = "3";
    monthsArray["May"] = "4";
    monthsArray["June"] = "5";
    monthsArray["July"] = "6";
    monthsArray["August"] = "7";
    monthsArray["September"] = "8";
    monthsArray["October"] = "9";
    monthsArray["November"] = "10";
    monthsArray["December"] = "11";

    var months = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"];

    var weekday = new Array();
    weekday[0] = "Sunday";
    weekday[1] = "Monday";
    weekday[2] = "Tuesday";
    weekday[3] = "Wednesday";
    weekday[4] = "Thursday";
    weekday[5] = "Friday";
    weekday[6] = "Saturday";



function dateConversion(day, month,year){
    d=new Date(year,month-1,day)
    mainFunction(d)
}
function nextFunction() {
    var month =((document).getElementById('currMonth')).innerHTML;
    var year = ((document).getElementById('currYear')).innerHTML;
    var current = new Date(year,monthsArray[month],1);
    var next= new Date(current.setMonth( current.getMonth( ) + 1 ));
    mainFunction(next)
}

function prevFunction() {
    var month =((document).getElementById('currMonth')).innerHTML;
    var year = ((document).getElementById('currYear')).innerHTML;
    var current = new Date(year,monthsArray[month],1);
    var previous= new Date(current.setMonth( current.getMonth( ) - 1 ));
    mainFunction(previous)
}
function mainFunction(d){
    $('.days').empty()
    html=""

    //save month as a number and as a word to be displayed
    var month=d.getMonth()
    namedmonth=months[d.getMonth()];
    var year=d.getFullYear();

    //display month name
    document.getElementById("currMonth").innerHTML=namedmonth;
    document.getElementById("currYear").innerHTML=year;

    //find out what day is the first and last day of the month
        // in order to get days of the previous/upcoming month

    var FirstDay = new Date(year, month, 1);
    var LastDay = new Date(year, month + 1, 0);

    if (typeof weekday[FirstDay.getDay()] != 'undefined') {     // CHECK FOR 'undefined'.
        FirstDay=FirstDay
        LastDay= LastDay
    }
    else {
        FirstDay=""
        LastDay=""
    }

    //get number of days this month
    days= LastDay.getDate();

    //get previous/upcoming month's number of days
    var futureMonth= new Date(d.setMonth( d.getMonth( ) + 1 ));
    var pastMonth = new Date(d.setUTCMonth(month - 1));
    var LastPastDay = new Date(pastMonth.getFullYear(), pastMonth.getMonth()+1, 0).getDay();
    var LastMonthDays= new Date(pastMonth.getFullYear(), pastMonth.getMonth()+1, 0).getDate();
    var FirstFutureDay = new Date(futureMonth.getFullYear(),futureMonth.getMonth(),1).getDay();

    if (FirstDay.getDay()==0){
        for (var i=LastMonthDays-5; i <= LastMonthDays; i++) {
            day1 = i
            month1 = pastMonth.getMonth()+1
            year1 = pastMonth.getFullYear()
            url="<a onclick=\"generateUrl("+day1+","+month1+","+year1+")\">"
            html +=url+ "<li>"+(i)+"</li></a>";
        }
    }else{
        for (var i=LastMonthDays-FirstDay.getDay()+2; i <= LastMonthDays; i++) {
            day1=i
            month1=pastMonth.getMonth()+1
            year1=pastMonth.getFullYear()
            url="<a onclick=\"generateUrl("+day1+","+month1+","+year1+")\">"
            html +=url+"<li>"+(i)+"</li></a>";
        }
    }
    for (var i=0; i < days; i++) {
        day1=i+1
        month1=month+1
        year1=year
        currentD = new Date(year1,month1,day1)
        url="<a onclick=\"generateUrl("+day1+","+month1+","+year1+")\">"
        html +=url+"<li><b>"+(i+1)+"</b></li></a>";
            }
    for (var i=1; i <= 7-LastDay.getDay(); i++) {
        day1=i
        month1=futureMonth.getMonth()+1
        year1=futureMonth.getFullYear()
        url="<a onclick=\"generateUrl("+day1+","+month1+","+year1+")\">"
        html +=url+"<li>"+(i)+"</li></a>";
    }

    $("#daysBuilder").append(html);
    };


JS_REVERSE_JS_VAR_NAME = 'Urls'
function generateUrl(day, month, year){
    location.href = "/calendar/"+day+"/"+month+"/"+year+"/"
    }

// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

//Leads Reports Radio Buttons


function leadsSelection(){
    document.getElementById('succLeads').style.display = "none"
        document.getElementById('allLeads').style.display = "block"

}
function leadsSelection2(){
    document.getElementById('allLeads').style.display = "none"
        document.getElementById('succLeads').style.display = "block"

}

function sales(){
    document.getElementById('profitsDiv').style.display = "none"
        document.getElementById('salesDiv').style.display = "block"

}
function profit(){
    document.getElementById('salesDiv').style.display = "none"
        document.getElementById('profitsDiv').style.display = "block"

}

function upcoming(){
    document.getElementById('upcomingDiv').style.display = "block"
    document.getElementById('pastDiv').style.display = "none"

}
function past(){
    document.getElementById('upcomingDiv').style.display = "none"
    document.getElementById('pastDiv').style.display = "block"

}

/** Show or Hide Sales Banner in home page **/
function showSales(){
    document.getElementById('hideSales').style.display = "block"
}
function hideSales(){
    document.getElementById('hideSales').style.display = "none"
}

/** Show or Hide each notification banner respectively in home page **/
function birthdays(){
    document.getElementById('birthdays').style.display = "block"
    document.getElementById('toDo').style.display = "none"
    document.getElementById('generalRenewals').style.display = "none"
    document.getElementById('lifeRenewals').style.display = "none"
    document.getElementById('generalPayments').style.display = "none"
    document.getElementById('lifePayments').style.display = "none"
    document.getElementById('leadsToContact').style.display = "none"
}

function todo(){
    document.getElementById('birthdays').style.display = "none"
    document.getElementById('toDo').style.display = "block"
    document.getElementById('generalRenewals').style.display = "none"
    document.getElementById('lifeRenewals').style.display = "none"
    document.getElementById('generalPayments').style.display = "none"
    document.getElementById('lifePayments').style.display = "none"
    document.getElementById('leadsToContact').style.display = "none"
}

function renewals(){
    document.getElementById('birthdays').style.display = "none"
    document.getElementById('toDo').style.display = "none"
    document.getElementById('generalRenewals').style.display = "block"
    document.getElementById('lifeRenewals').style.display = "block"
    document.getElementById('generalPayments').style.display = "none"
    document.getElementById('lifePayments').style.display = "none"
    document.getElementById('leadsToContact').style.display = "none"
}

function payments(){
    document.getElementById('birthdays').style.display = "none"
    document.getElementById('toDo').style.display = "none"
    document.getElementById('generalRenewals').style.display = "none"
    document.getElementById('lifeRenewals').style.display = "none"
    document.getElementById('generalPayments').style.display = "block"
    document.getElementById('lifePayments').style.display = "block"
    document.getElementById('leadsToContact').style.display = "none"
}

function leadsToContact(){
    document.getElementById('birthdays').style.display = "none"
    document.getElementById('toDo').style.display = "none"
    document.getElementById('generalRenewals').style.display = "none"
    document.getElementById('lifeRenewals').style.display = "none"
    document.getElementById('generalPayments').style.display = "none"
    document.getElementById('lifePayments').style.display = "none"
    document.getElementById('leadsToContact').style.display = "block"
}
