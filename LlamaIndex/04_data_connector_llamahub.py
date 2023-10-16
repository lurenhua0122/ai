
from pathlib import Path
from llama_index import download_loader
from llama_index import VectorStoreIndex
from llama_index import SimpleDirectoryReader
import os
os.environ['OPENAI_API_KEY'] = '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'

MarkdownReader = download_loader("MarkdownReader")

loader = MarkdownReader()
documents = loader.load_data(file=Path('./wtf-langchain/README.md'))
     
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("LangChain极简入门教程用的什么框架版本？")
print(response)