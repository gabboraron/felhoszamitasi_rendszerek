var loaded = 0;

var searchterm = 'tumor';

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

    //based on https://stackoverflow.com/questions/70030175/why-i-got-undefined-symbol-xml-sethashsalt-error-when-i-run-code-from-php-but?noredirect=1#comment123794600_70030175
    $.ajax({ //Seconds Request
        type :"GET",
        url : 'torrentfeed.php?subject='+searchterm+'&times=' + loaded,     
        cache: false,
        success: function(server_response){     
            torrentAnswer = server_response;
            //dataDiv.innerHTML = torrentAnswer;
            console.log("masodik: " + torrentAnswer);
            dataDiv = document.getElementById('liveData2');
            if (torrentAnswer[torrentAnswer.length-2] == 200) {
                dataDiv.innerHTML = "Találatok száma: "+ torrentAnswer[torrentAnswer.length-1]+"<br>";
                table = printInTable(["cím", "típusa", "ID", "letöltési link", "leírás link"],torrentAnswer);
                table.id = "academicTorrent";
                dataDiv.appendChild(table);          
            }else{
                dataDiv.innerHTML ="HIBA<br> hibakód: "+ torrentAnswer[torrentAnswer.length-2]+"<br>";
            }  
            //console.log(answer);
            //$('.price1').html(server_response).show();                  
        }           
    });
});