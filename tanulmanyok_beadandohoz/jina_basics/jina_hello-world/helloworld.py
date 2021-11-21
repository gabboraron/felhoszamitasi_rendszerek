from jina import Document, DocumentArray
from jina import Executor, requests
from jina import Flow, Document, Executor, requests

doc1 = Document(text="hello world")
doc2 = Document(uri="cute_kittens.png")

docs = DocumentArray([doc1, doc2])

class MyExecutor(Executor):

	@requests
	def foo(self, **kwargs):
		print(kwargs)

class MyExecutor(Executor):

	@requests(on='/bar')
	def foo(self, docs, **kwargs):
		print(docs)


f = Flow().add(name='myexec1', uses=MyExecutor)

with f:
    f.post(on='/bar', inputs=Document(), on_done=print)