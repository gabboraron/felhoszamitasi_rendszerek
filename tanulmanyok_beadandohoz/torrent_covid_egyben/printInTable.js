/****
 * 
 * A function to print out an RSS like array to a table
 * based on this: https://stackoverflow.com/questions/70013641/how-to-use-correctly-json-stringify-with-an-php-returned-js-object?noredirect=1#comment123765415_70013641
 * 
 * 
 * 
 ****/

function printInTable(heading, tableData) {
	var table = document.createElement("table");
    var row = document.createElement("TR");
    for (var i = 0; i < heading.length; i++) {
        var head = document.createElement("TH");
        head.innerHTML = heading[i];
        row.appendChild(head);
    }
    table.appendChild(row);

    for (var i = 0; i < tableData.length-2; i++) {
        var row = document.createElement("TR");
        
        for (var j = 0; j < tableData[i].length; j++) {
            var data = document.createElement("TD");
            data.innerHTML = tableData[i][j];
            row.appendChild(data);
        }
        table.appendChild(row);        
    }
    return table;
}