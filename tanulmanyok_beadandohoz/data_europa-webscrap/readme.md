# Helth data scrap from data.europa.eu

> Since there is no available API I have to use these technique to get the data.
>
> The RSS/ATOM feed from `https://data.europa.eu/data/datasets?categories=heal&page=1&locale=en&query=MYQUERYTERM` is not active at all time, there is in many cases false answers or even there is no answer but on the page it is, the [`euDataScrap.py`](euDataScrap.py) is useless, So I have to iterate on each time on GUI site, and this means much more usage of servers on both sides! 


The etractiono from GUI URL with [`euDataScrapFromGUI.py`](euDataScrapFromGUI.py) failed because of the ajax refresh of the site.