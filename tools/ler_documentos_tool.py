import logging
import os
from datetime import datetime

from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.document_loaders import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter


class LerDocumentos:
    def __init__(self, db_path="db"):
        self.db_path = db_path
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    def carrega_arquivo(self):
        index_file = os.path.join(self.db_path, "index.faiss")

        if os.path.exists(index_file):
            print("Carregando banco de dados existente...")
            db = FAISS.load_local(self.db_path, self.embeddings, allow_dangerous_deserialization=True)
            logging.info(f"Documentos no FAISS carregado: {db.index.ntotal}")
            retriever = db.as_retriever(search_kwargs={"k": 5})

        else:
            print("Criando novo banco de dados...")
            start = datetime.now()

            loader = CSVLoader(file_path="dataset/sales.csv", encoding="utf-8")
            docs = loader.load()

            # Chunking só quando cria
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=3000,
                chunk_overlap=200,
                separators=["\n\n", "\n", ",", " "]
            )
            docs_chunks = text_splitter.split_documents(docs)

            db = FAISS.from_documents(docs_chunks, self.embeddings)
            db.save_local(self.db_path)
            logging.info(f"Documentos no FAISS criado: {db.index.ntotal}")
            retriever = db.as_retriever(search_kwargs={"k": 5})

            end = datetime.now()
            print(f"Tempo total: {end - start}")

        return retriever

    def consulta_retriever(self, query):
        """Busca documentos diretamente no FAISS sem LLM."""
        retriever = self.carrega_arquivo()
        resultados = retriever.get_relevant_documents(query)
        for i, doc in enumerate(resultados, start=1):
            print(f"Documento {i}:")
            print(doc.page_content)
            print(f"Metadados: {doc.metadata}")
            print("-" * 50)

    def output(self, llm, prompt):
        """Executa consulta usando LLM + FAISS via RetrievalQA."""
        retriever = self.carrega_arquivo()
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff"
        )
        return qa_chain.invoke(f"Responder em português: {prompt} {self.prompt_rules()}")

    def prompt_rules(self):
        return """
        Você é um agente de vendas:
        - Analisar valores dos produtos
        - Gerar relatórios detalhados
        - Analisar quais produtos vendem mais e em quais regiões
        """
