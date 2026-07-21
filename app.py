import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()  # carga las variables del archivo .env

st.set_page_config(page_title="AstroAlura 🔭", page_icon="🔭")
st.title("🔭 AstroAlura")
st.caption("Tu asistente de IA sobre planetas, estrellas, galaxias, misiones espaciales y fenómenos astronómicos")

api_key = os.environ.get("GOOGLE_API_KEY")

@st.cache_resource
def cargar_agente():
    loader = PyPDFLoader("base_conocimiento_astronomia.pdf")
    paginas = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(paginas)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    vectorstore = FAISS.from_documents(docs, embeddings)

    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
    prompt = ChatPromptTemplate.from_template(
        """Eres un asistente experto en astronomía. Responde usando ÚNICAMENTE el contexto.
Si no está en el contexto, responde EXACTAMENTE: "Lo sentimos, esa información no se encuentra en la base de datos."

Contexto:
{context}

Pregunta: {question}"""
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    def format_docs(docs):
        return "\n\n".join(d.page_content for d in docs)

    return (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt | llm | StrOutputParser()
    )

if not api_key:
    st.error("⚠️ No se encontró la API Key. Revisa tu archivo .env")
else:
    qa_chain = cargar_agente()

    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

    for msg in st.session_state.mensajes:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    pregunta = st.chat_input("Escribe tu pregunta sobre astronomía...")

    if pregunta:
        st.session_state.mensajes.append({"role": "user", "content": pregunta})
        with st.chat_message("user"):
            st.write(pregunta)
        with st.chat_message("assistant"):
            with st.spinner("Consultando el universo..."):
                respuesta = qa_chain.invoke(pregunta)
                st.write(respuesta)
        st.session_state.mensajes.append({"role": "assistant", "content": respuesta})