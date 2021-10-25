$(document).ready(function () {
    // console.log('js working till here ');

    let preview = document.getElementById('1');
    let nreview = document.getElementById('0');
    

    if(preview != null){
        // console.log('preview is not null, switching it to green');
        $('#mcontent').css("transition","background-color 1.5s ease");
        $('#mcontent').css('background-color', 'rgb(208, 238, 208)');
    }
    else if(nreview != null){
        // console.log('nreview is not null, switching it to red');
        $('#mcontent').css("transition","background-color 1.5s ease");
        $('#mcontent').css('background-color', 'rgb(245, 227, 227)');
    }
    else {
        $('#mcontent').css("transition","background-color 1.5s ease");
        $('#mcontent').css('background-color', 'fff');
    }
});