$(document).ready(function() {
    $('.flipTimer').flipTimer({ 
    
    // count up or countdown
    direction: 'down', 
    
    // the target date
    date: 'August 20, 2022 00:00:00', 
    
    // callback works only with direction = "down"
    callback: function() { alert('times up!'); };
    
    // custom date
    seconds: false,
    minutes: false,
    hours: false,
    days: false,
    
    });
    });