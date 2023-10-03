from langchain.retrievers.document_compressors import DocumentCompressorPipeline
from langchain.document_transformers import EmbeddingsRedundantFilter
from langchain.retrievers.document_compressors import EmbeddingsFilter
from langchain.retrievers.document_compressors import LLMChainFilter
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers import ContextualCompressionRetriever
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os

os.environ['OPENAI_API_KEY'] = "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"


def pretty_print_docs(docs):
    print(f"\n{'-' * 100}\n".join([f"Document {i+1}:\n\n" +
          d.page_content for i, d in enumerate(docs)]))


question = "Where did Paul Graham study?"


documents = TextLoader(
    "/Users/mike/Documents/ai/LlamaIndex/data/paul_graham_essay.txt").load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

retriver = FAISS.from_documents(texts, OpenAIEmbeddings()).as_retriever()
docs = retriver.get_relevant_documents(
    question)

# pretty_print_docs(docs)


llm = OpenAI(temperature=0)
compressor = LLMChainExtractor.from_llm(llm=llm)

compressor_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=retriver)

compressor_docs = compressor_retriever.get_relevant_documents(question)
# pretty_print_docs(compressor_docs)


_filter = LLMChainFilter.from_llm(llm=llm)

compressor_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=retriver)

compressor_docs = compressor_retriever.get_relevant_documents(question)
# pretty_print_docs(compressor_docs)


embeddings = OpenAIEmbeddings()
embeddings_filter = EmbeddingsFilter(
    embeddings=embeddings, similarity_threshold=0.76)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=embeddings_filter, base_retriever=retriver)

compressed_docs = compression_retriever.get_relevant_documents(question)
# pretty_print_docs(compressed_docs)


splitter = CharacterTextSplitter(
    chunk_size=300, chunk_overlap=0, separator=". ")
redundant_filter = EmbeddingsRedundantFilter(embeddings=embeddings)
relevant_filter = EmbeddingsFilter(
    embeddings=embeddings, similarity_threshold=0.76)
pipeline_compressor = DocumentCompressorPipeline(
    transformers=[splitter, redundant_filter, relevant_filter]
)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=pipeline_compressor, base_retriever=retriver)

compressed_docs = compression_retriever.get_relevant_documents(
    question)
pretty_print_docs(compressed_docs)
