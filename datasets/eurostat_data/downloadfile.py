import requests

url = str("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/demo_mlexpec.tsv.gz")
r = requests.get(url, allow_redirects=True)
print(str(str(str(url).split("/")[-1]).split(".")[0]))
open('demo_mlexpec.tsv.gz', 'wb').write(r.content)
