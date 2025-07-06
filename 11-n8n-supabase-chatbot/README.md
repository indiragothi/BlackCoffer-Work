# AI-Powered Document Q&A Agent using n8n, Supabase, and OpenAI

This project demonstrates an end-to-end AI assistant that performs **question-answering operations** on documents stored in **Google Drive**. 


Whenever a document is created or updated, the system:
1. Extracts its content
2. Generates vector embeddings using **OpenAI**
3. Stores the embeddings in **Supabase**
4. Allows users to ask questions about the document via an intelligent **chat interface** built in **n8n**

---

##  Features

-  Real-time sync with Google Docs (triggered on file create/update)
-  Semantic search via vector embeddings
-  Scalable vector database using Supabase
-  Natural language answering using OpenAI GPT
-  Persistent chat memory with PostgreSQL
-  Built using a fully visual, no-code workflow in n8n

---

##  Tech Stack

| Tool        | Purpose                                 |
|-------------|------------------------------------------|
| [n8n](https://n8n.io)         | Automation platform for orchestrating the flow |
| [Supabase](https://supabase.com)   | Database and vector storage (Postgres + match function) |
| [OpenAI](https://openai.com)       | For both embeddings and LLM responses |
| Google Drive | Document source (monitored via triggers) |

---


---

##  Flow of Execution

1. **Trigger**: Google Drive file is created/updated
2. **Download**: Document is downloaded and parsed
3. **Delete Existing**: Old records with the same file ID are deleted from Supabase
4. **Split + Embed**: Text is chunked and embedded using OpenAI
5. **Store**: Embeddings and metadata are stored in Supabase
6. **Chat**: When a question is asked, the most relevant chunks are retrieved and passed to the LLM for answering
7. **Memory**: Supabase also stores multi-turn chat memory for better responses

 
 