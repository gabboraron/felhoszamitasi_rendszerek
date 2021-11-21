import PyPDF2
import requests

# #creating a pdf file object
# pdfFileObj = open('table_of_contents_en.pdf', 'rb')
 
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# # printing number of pages in pdf file
# print(pdfReader.numPages)
 
# # creating a page object
# pageObj = pdfReader.getPage(0)
 
# # extracting text from page
# print(pageObj.extractText())
 
# # closing the pdf file object
# pdfFileObj.close()

PDFFile = open("table_of_contents_en.pdf",'rb')

PDF = PyPDF2.PdfFileReader(PDFFile)
pages = PDF.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'

for page in range(pages):
	print("Current Page: {}".format(page))
	pageSliced = PDF.getPage(page)
	pageObject = pageSliced.getObject()
	if key in pageObject.keys():
		ann = pageObject[key]
		for a in ann:
			u = a.getObject()
			# if uri in u[ank].keys():
			# 	print(u[ank][uri])
			if str(u[ank][uri]).find(".tsv.gz") != -1 :
				url = str(u[ank][uri])
				try:
					r = requests.get(url, allow_redirects=True)
					print(str(str(str(url).split("/")[-1]).split(".")[0]))
					open(str(str(url).split("/")[-1]), 'wb').write(r.content)
				except:
					print("ERROR ON" + url)
