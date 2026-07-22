[README.md](https://github.com/user-attachments/files/30283252/README.md)
# AstroAlura 🔭

Agente de inteligencia artificial que responde preguntas en lenguaje natural sobre astronomía —planetas, estrellas, galaxias, misiones espaciales y fenómenos astronómicos— a través de una interfaz de chat visual, desplegada públicamente en la nube.

Proyecto desarrollado como challenge final del curso **Alura Agente**.

## 🌐 Demo en vivo

**👉 [Probar AstroAlura](https://astroalura-df2fenivzktuqzwfl38ie2.streamlit.app)**

*(agregar aquí una captura de pantalla de la app funcionando, mostrando una pregunta y su respuesta)*

##  Descripción

Cualquier persona puede escribir una pregunta sobre astronomía (por ejemplo, "¿cuántas lunas tiene Júpiter?") directamente en el chat, y el agente responde basándose en una base de conocimiento propia en PDF. Si la pregunta no puede responderse con la información disponible, el agente lo indica claramente en vez de inventar una respuesta.

##  Arquitectura

El proyecto sigue un patrón de **RAG (Retrieval-Augmented Generation)**:

```
Documento fuente (PDF de astronomía)
      ↓
PyPDFLoader (LangChain) → extrae el texto del PDF
      ↓
RecursiveCharacterTextSplitter → divide el texto en fragmentos (chunks)
      ↓
Embeddings (Gemini Embedding) → convierte cada fragmento en un vector numérico
      ↓
Vectorstore (FAISS) → almacena los vectores para búsqueda semántica
      ↓
Retriever → busca los 3 fragmentos más relevantes según la pregunta (k=3)
      ↓
LLM (Gemini 3.5 Flash) → genera la respuesta en lenguaje natural,
                          o indica que no encontró la información
      ↓
Interfaz de chat (Streamlit) → desplegada públicamente en Streamlit Community Cloud
```

**Flujo resumido:** el usuario escribe una pregunta en la interfaz web → el agente busca en el vectorstore los fragmentos más relevantes del documento → esos fragmentos se pasan como contexto al modelo de lenguaje → el modelo responde basándose únicamente en esa información, o informa que no la encontró.

## Tecnologías utilizadas

| Componente | Herramienta |
|---|---|
| Lenguaje | Python |
| Orquestación del agente | LangChain |
| Lectura del documento | PyPDFLoader (LangChain) |
| División en fragmentos | RecursiveCharacterTextSplitter |
| Embeddings | Gemini Embedding (`gemini-embedding-001`) |
| Base de datos vectorial | FAISS |
| Modelo de lenguaje (LLM) | Gemini 3.5 Flash |
| Interfaz visual | Streamlit |
| Entorno de desarrollo | Visual Studio Code |
| Despliegue | Streamlit Community Cloud |

## 📚 Base de conocimiento

El documento fuente (`base_conocimiento_astronomia.pdf`) cubre seis áreas temáticas:

1. **Planetas del Sistema Solar** — características, composición, lunas y datos orbitales.
2. **Estrellas** — el Sol, Sirio, Betelgeuse, Proxima Centauri y clasificación estelar.
3. **Galaxias** — Vía Láctea, Andrómeda, tipos de galaxias y agujeros negros supermasivos.
4. **Misiones espaciales** — Apolo, Hubble, James Webb, rovers marcianos, ISS y Voyager.
5. **Fenómenos astronómicos** — eclipses, supernovas, agujeros negros, lluvias de meteoros y radiación cósmica de fondo.
6. **Datos rápidos y curiosidades** — cantidad de planetas, distancias al Sol, comparaciones de tamaño, planeta más cercano a la Tierra, entre otros.

## 💬 Ejemplos de preguntas y respuestas

**Pregunta:** ¿Cuántas lunas tiene Júpiter?
**Respuesta:** Según el contexto, Júpiter tiene al menos 95 lunas conocidas.

**Pregunta:** ¿Cuál es el planeta más cercano a la Tierra?
**Respuesta:** *(agregar aquí la respuesta obtenida)*

**Pregunta:** ¿Cuál es la capital de Francia?
**Respuesta:** Lo sentimos, esa información no se encuentra en la base de datos.

> ✅ El agente distingue correctamente entre preguntas que puede responder con el documento y preguntas fuera de su base de conocimiento, evitando inventar información (mitigación de alucinaciones).

## ⚙️ Instrucciones de instalación y ejecución local

### Requisitos previos
- Python 3.10 o superior
- API key gratuita de Gemini: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

### Pasos

1. Clona este repositorio:
   ```bash
   git clone https://github.com/isa850/AstroAlura.git
   cd AstroAlura
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` en la raíz del proyecto (usa `.env.example` como plantilla) con tu API key:
   ```
   GOOGLE_API_KEY=tu_clave_de_api_aqui
   ```

5. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

6. Se abrirá automáticamente en tu navegador en `http://localhost:8501`.

##  Despliegue

La aplicación está desplegada públicamente en **Streamlit Community Cloud**, conectado directamente a este repositorio de GitHub. La API key se almacena de forma segura en los "Secrets" de Streamlit Cloud, sin quedar expuesta en el código ni en el repositorio.

**URL pública:** [https://astroalura-df2fenivzktuqzwfl38ie2.streamlit.app](https://astroalura-df2fenivzktuqzwfl38ie2.streamlit.app)

## 📂 Estructura del repositorio

```
AstroAlura/
├── app.py                              # Aplicación principal (interfaz + lógica del agente)
├── base_conocimiento_astronomia.pdf    # Documento fuente utilizado
├── requirements.txt                    # Dependencias del proyecto
├── .env.example                        # Plantilla de variables de entorno
├── .gitignore                          # Archivos excluidos del repositorio
└── README.md                           # Este archivo
```

## Posibles mejoras futuras

- Ampliar la base de conocimiento con más categorías (exoplanetas, cosmología, astrofísica).
- Agregar historial de conversación persistente entre sesiones.
- Incluir imágenes o gráficos junto a las respuestas (por ejemplo, imágenes de planetas).
- Aumentar el número de fragmentos recuperados (`k`) para preguntas que requieren combinar varias secciones del documento.

## 👤 Autor (Isabel sofia riascos

Proyecto desarrollado como parte del challenge final del curso Alura Agente.


