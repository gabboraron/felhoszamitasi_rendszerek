var loaded = 0;

window.addEventListener('load', function()
{
    //based on this: https://stackoverflow.com/a/41738983
    $.ajax({ // First Request
        type :"GET",
        url : 'feed.php?subject=tumor&times=' + loaded,     
        cache: false,
        success: function(server_response){     
            answer = JSON.parse(server_response);
            dataDiv = document.getElementById('liveData');
            dataDiv.innerHTML = answer;
            console.log("elso: " + answer);
            //$('.price1').html(server_response).show();                  
        }           
    }),

    $.ajax({ //Seconds Request
        type :"GET",
        url : 'feed.php?subject=budapest&times=' + loaded,     
        cache: false,
        success: function(server_response){     
            answer = JSON.parse(server_response);
            //dataDiv.innerHTML = answer;
            console.log("masodik: " + answer);
            //console.log(answer);
            //$('.price1').html(server_response).show();                  
        }           
    });
});