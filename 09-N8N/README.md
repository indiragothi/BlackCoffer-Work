# N8N-Supabase Document Q&A System

This project implements an automated document processing and question-answering system using N8N workflows integrated with Supabase vector database and Hugging Face embeddings. The system enables users to ask questions about Google Drive documents and receive accurate answers based on the document content.

## System Overview

The system works by:
1. Detecting when documents are created or updated in Google Drive
2. Processing and extracting content from these documents
3. Converting document content into vector embeddings using Hugging Face models
4. Storing these embeddings in a Supabase Vector Store
5. Enabling users to ask questions through a chat interface
6. Retrieving relevant document sections from Supabase
7. Generating responses using a language model

## Workflow Components

### Document Processing Workflow

This workflow handles document ingestion and embedding creation:

1. **Triggers**:
   - `File Updated` - Activates when a document is modified in Google Drive
   - `File Created` - Activates when a new document is added to Google Drive

2. **Processing Steps**:
   - `Edit Fields` - Prepares document metadata and content for processing
   - `Supabase (delete: row)` - Removes old entries for updated documents
   - `Google Drive (download: file)` - Retrieves the document content
   - `Extract from File` - Parses text content from the document
   - `Supabase Vector Store` - Stores document embeddings for retrieval

3. **Embedding Generation**:
   - `Embeddings HuggingFace` - Generates vector embeddings of document content
   - `Document → Default Data Loader` - Processes document structure
   - `Text Splitter → Recursive Character Text Splitter` - Chunks document for better processing

### Question-Answering Workflow

This workflow handles user queries and generates responses:

1. **Trigger**:
   - `When chat message received` - Activates when a user submits a question

2. **Processing Steps**:
   - `Question and Answer Chain` - Orchestrates the Q&A process
   - `Model & Retriever` - Combines language model with document retrieval

3. **Retrieval System**:
   - `Vector Store Retriever` - Finds relevant document chunks based on query similarity
   - `Supabase Vector Store` - Database that stores document embeddings
   - `Embeddings HuggingFace` - Generates embeddings for user queries

4. **Response Generation**:
   - `Hugging Face Inference Model` - Processes retrieved context and generates answers

## Setup Instructions

### Prerequisites

1. N8N installed and running
2. Supabase account and project
3. Google Drive API credentials
4. Hugging Face account (for embedding model access)

### Configuration Steps

1. **Google Drive Integration**:
   ```
   - Create Google Drive credentials in Google Cloud Console
   - Add credentials to N8N Google Drive node
   - Configure monitored folder path: "Supabase Agent" 
   ```

2. **Supabase Setup**:
   ```
   - Create a new Supabase project
   - Enable Vector extension in the database
   - Create a vector table with appropriate schema:
     - id: uuid (primary key)
     - content: text (document chunk)
     - embedding: vector(384) (or appropriate dimension)
     - metadata: json (document source information)
   ```

3. **Hugging Face Model Configuration**:
   ```
   - Configure embedding model (e.g., "sentence-transformers/all-MiniLM-L6-v2")
   - Set up inference model for answer generation
   ```

4. **N8N Workflow Import**:
   ```
   - Import provided workflow JSON files
   - Configure credentials for all services
   - Adjust file paths and model parameters as needed
   ```

## Using the System

1. **Adding Documents**:
   - Place documents in the monitored Google Drive folder ("Supabase Agent")
   - System automatically processes new and updated files (e.g., "sampletext")
   - Wait for processing to complete (embedding generation and storage)

2. **Asking Questions**:
   - Access the chat interface
   - Enter questions related to document content
   - System retrieves relevant sections and generates answers
   - Example: Questions about "MoonBites" marketing campaign from sample document

## Technical Details

### Embedding Process

The system uses a chunking strategy to divide documents into manageable pieces:
- Text is split using the Recursive Character Text Splitter
- Each chunk is embedded separately
- Metadata tracks document source and chunk location

### Retrieval Mechanism

When a question is asked:
1. The question is converted to an embedding
2. Vector similarity search finds relevant document chunks
3. Retrieved context is sent to the language model
4. The model generates a coherent answer based on context

### Data Flow

```
Document in Google Drive
  ↓
Content Extraction
  ↓
Text Chunking
  ↓
Embedding Generation
  ↓
Vector Storage in Supabase
  ↓
User Question → Vector Embedding
  ↓
Similarity Search in Vector Database
  ↓
Context Retrieval
  ↓
Answer Generation
  ↓
Response to User
```

## Maintenance and Troubleshooting

### Common Issues

- **Document Processing Failures**:
  - Check Google Drive API quotas
  - Verify file format compatibility
  - Monitor N8N execution logs

- **Embedding Errors**:
  - Ensure Hugging Face API is accessible
  - Check model compatibility
  - Verify embedding dimensions match database schema

- **Query Issues**:
  - Investigate vector search parameters
  - Check retrieval chunk size settings
  - Verify language model is responding correctly

## Future Improvements

- Add support for more document formats
- Implement user feedback loop for answer quality
- Add authentication for chat interface
- Improve embedding quality with domain-specific models
- Implement caching for frequently asked questions

## Example Workflow Configuration

The workflow is designed to handle the sample marketing campaign data in the "sampletext" file, which includes information about fictional campaigns like "MoonBites," "EcoMends," and "Velox."