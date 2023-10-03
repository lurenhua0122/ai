import os
import streamlit as st
from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain


OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
persist_directory = 'pdf_persist1'
collection_name = 'pdf_collection1'
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, verbose=True)

chains = load_qa_chain(llm=llm, chain_type='stuff', verbose=True)
vectorstore = None


def load_pdf(pdf_path):
    return PyMuPDFLoader(pdf_path).load()


st.title('PDF Chatbot')

with st.container():
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        path = os.path.join('.', uploaded_file.name)
        with open(path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        docs = load_pdf(path)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=0)

        split_docs = text_splitter.split_documents(docs)

        vectorstore = Chroma.from_documents(
            split_docs, embeddings, collection_name=collection_name, persist_directory=persist_directory)

        vectorstore.persist()
        st.write("Done")

with st.container():
    question = st.text_input("Question")
    if vectorstore is not None and question is not None and question != "":
        docs = vectorstore.similarity_search(
            question, 3, include_metadata=True)
        answer = chains.run(input_documents=docs,
                            question=question, debug=True)
        st.write(answer)
