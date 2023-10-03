import os
os.environ['OPENAI_API_KEY'] = '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'

from llama_index import VectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)


query_engine = index.as_query_engine()
response = query_engine.query("Who is the author?")

print(response)

response = query_engine.query("Introduce me Paul Graham")
print(response)