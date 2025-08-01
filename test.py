from components.parser import DocumentParser

parser = DocumentParser()

docs = parser.parse_document("uploads\SRIDHAR-MODUKURU-FlowCV-Resume-20250728.pdf")

print(len(docs['chunks']))


from components.vectorstore import VectorStore

s = VectorStore()

s.add_documents(docs['chunks'])
