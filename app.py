# Cambio para la práctica de Git
import streamlit as st
import docx
from pypdf import PdfReader
import io
from deep_translator import GoogleTranslator
import time

st.set_page_config(page_title="Traductor Profesional IA", page_icon="🌐")
st.title("🌐 Traductor de Documentos (Word & PDF)")

idiomas = {"Español": "es", "Inglés": "en", "Francés": "fr", "Alemán": "de", "Italiano": "it"}
col1, col2 = st.columns(2)
with col1: orig = st.selectbox("Idioma de origen", list(idiomas.keys()))
with col2: dest = st.selectbox("Idioma de destino", list(idiomas.keys()))

archivo = st.file_uploader("Sube tu archivo (Word o PDF)", type=['docx', 'pdf'])

if archivo is not None:
    lista_parrafos = []
    
    # Lectura inteligente
    if archivo.name.endswith('.docx'):
        doc = docx.Document(archivo)
        lista_parrafos = [p.text for p in doc.paragraphs if p.text.strip()]
    elif archivo.name.endswith('.pdf'):
        lector = PdfReader(archivo)
        for pagina in lector.pages:
            texto_p = pagina.extract_text()
            if texto_p:
                lista_parrafos.extend(texto_p.split('\n'))

    if st.button("Traducir ahora"):
        with st.spinner("Traduciendo... esto puede tardar un poco según el tamaño del archivo ⏳"):
            traductor = GoogleTranslator(source=idiomas[orig], target=idiomas[dest])
            doc_final = docx.Document()
            
            for p in lista_parrafos:
                try:
                    # Traducción con pequeña pausa para no saturar a Google
                    traducido = traductor.translate(p)
                    doc_final.add_paragraph(traducido)
                    time.sleep(0.1) 
                except:
                    doc_final.add_paragraph(p) 
            
            memoria = io.BytesIO()
            doc_final.save(memoria)
            memoria.seek(0)
            
            st.success("¡Traducción completa!")
            st.download_button("⬇️ Descargar archivo traducido (.docx)", memoria, "Traduccion.docx")
