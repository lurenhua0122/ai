import os
os.environ['OPENAI_API_KEY'] = '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'

from llama_index import SimpleDirectoryReader
reader = SimpleDirectoryReader(
    input_dir="./wtf-langchain",
    required_exts=[".md"],
    recursive=True
)
docs = reader.load_data()

from llama_index import VectorStoreIndex

index = VectorStoreIndex.from_documents(docs)
query_engine = index.as_query_engine()
response = query_engine.query("什么是WTF LangChain？")
print(response)
response = query_engine.query("WTF LangChain教程的目的是什么？")
print(response)