from jina.flow import Flow

f = Flow().add(uses='cnn-encoding').addd(uses='simple-indexer')

with f:
	f.index(docs)