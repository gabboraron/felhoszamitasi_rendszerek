var loaded = 0;

var searchterm = 'románia';

window.addEventListener('load', function()
{
    //based on: https://stackoverflow.com/a/41738983
    $.ajax({ // First Request
        type :"GET",
        url : 'feed.php?subject='+searchterm+'&times=' + loaded, 
        cache: false,
        success: function(server_response){     
            //answer = JSON.parse(server_response);
            answer = server_response;
            dataDiv = document.getElementById('liveData');
            //dataDiv.innerHTML = "'"+answer+"'";
            //dataDiv.innerHTML = answer;
            console.log("elso: ", answer);
            //$('.price1').html(server_response).show();   
            if (answer[answer.length-2] == 200) {
                dataDiv.innerHTML = "Találatok száma: "+ answer[answer.length-1]+"<br>";
                table = printInTable(["időbélyeg", "cím", "leírás", "link"],answer);
                table.id = "covidnewsHU";
                dataDiv.appendChild(table);          
            }else{
                dataDiv.innerHTML ="HIBA<br> hibakód: "+ answer[answer.length-2]+"<br>";
            }  
        }           
    }),

    $.ajax({ //Seconds Request
        type :"GET",
        url : 'torrentfeed.php?subject='+searchterm+'&times=' + loaded,     
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