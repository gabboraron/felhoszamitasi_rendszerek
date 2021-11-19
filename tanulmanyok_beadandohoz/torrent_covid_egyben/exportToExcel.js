/****
 * 
 * Based on https://codepedia.info/javascript-export-html-table-data-to-excel
 * 
 * 
 * 
 * */

function ExportToExcel(type, tableID, sheetName, fileName, fn, dl) {
       var elt = document.getElementById(tableID);
       var wb = XLSX.utils.table_to_book(elt, { sheet: sheetName });
       return dl ?
         XLSX.write(wb, { bookType: type, bookSST: true, type: 'base64' }):
         XLSX.writeFile(wb, fn || (fileName + '.' + (type || 'xlsx')));
    }