# Extract datasets from ec.europa.eu/eurostat

> This little script extract all data from eurostat based on table of [contents file](table_of_contents_en.pdf) orginially hosted on http://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&file=table_of_contents_en.pdf
>
> Since there is only a [REST API Query builder](https://ec.europa.eu/eurostat/web/json-and-unicode-web-services/getting-started/query-builder) is available on the site of eurostat, I can't search in the full database, and can't scrap data with webscrap techniques because of the sites of data previewer use lazy load technique, or AJAX. So I have to extract the full database and create a search script for them.

## Usage:
1. Download the table of contents file from eurostat: http://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&file=table_of_contents_en.pdf
2. run `python3 downloadfile.py` edited with the file name, if it has changed.
3. extract with some tool the downloaded `.gz` files *(suggestion: https://stackoverflow.com/questions/31028815/how-to-unzip-gz-file-using-python )*
4. delete the `.gz` files.