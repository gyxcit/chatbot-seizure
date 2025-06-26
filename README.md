# Epilepsy Chatbot

A Retrieval-Augmented Generation (RAG) chatbot specializing in epilepsy using the Mistral model.

## Features
- RAG-based question answering about epilepsy
- Web interface for user interactions
- API endpoint for programmatic access

## Setup and Installation

### Prerequisites
- Python 3.9+
- Docker (optional)

### Local Development Setup
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: 
   - Windows: `venv\Scripts\activate`
   - Unix: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and configure your environment variables
6. Run the application: `python app.py`

### Docker Setup
1. Build the image: `docker build -t epilepsy-chatbot .`
2. Run the container: `docker run -p 5000:5000 --env-file .env epilepsy-chatbot`

## API Documentation
- `GET /`: Web interface
- `POST /ask`: Question answering endpoint
  - Request body: `{"question": "your question here"}`
  - Response: `{"answer": "model response"}`
- `GET /health`: Health check endpoint

## Data Sources
This chatbot uses medical literature on epilepsy, seizure detection, and wearable technologies.