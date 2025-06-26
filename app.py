from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from dotenv import load_dotenv
from src.rag_mistral import RagMistralModel

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure CORS
allowed_origins = os.getenv('ALLOWED_ORIGINS', 'http://localhost:3000').split(',')
CORS(app, origins=allowed_origins)

# Initialize RAG model
TOP_K = int(os.getenv('TOP_K', 3))
MAX_GEN_TOKENS = int(os.getenv('MAX_GEN_TOKENS', 250))

try:
    app.logger.info("Initializing RAG model...")
    rag_model = RagMistralModel(
        top_k=TOP_K, 
        top_k_hist=3, 
        max_gen_tokens=MAX_GEN_TOKENS
    )
    app.logger.info("RAG model initialized successfully")
except Exception as e:
    app.logger.error(f"Failed to initialize RAG model: {str(e)}")
    rag_model = None

@app.route('/')
def home():
    """Render the main chat interface."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests from the frontend."""
    try:
        app.logger.info("Chat endpoint called")
        
        if rag_model is None:
            app.logger.error("RAG model is None")
            return jsonify({
                'error': 'Le modèle RAG n\'est pas initialisé.',
                'status': 'error'
            }), 500
            
        data = request.get_json()
        app.logger.info(f"Received data: {data}")
        
        if not data or 'message' not in data:
            app.logger.error("No message in request")
            return jsonify({'error': 'Message is required'}), 400
        
        user_message = data['message']
        app.logger.info(f"Processing message: {user_message}")
        
        # Generate response using RAG model
        app.logger.info("Calling rag_model.ask()")
        response = rag_model.ask(user_message)
        app.logger.info(f"RAG response: {response}")
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
    
    except Exception as e:
        app.logger.error(f"Error in chat endpoint: {str(e)}")
        import traceback
        app.logger.error(f"Full traceback: {traceback.format_exc()}")
        return jsonify({
            'error': 'Une erreur s\'est produite lors du traitement de votre demande.',
            'status': 'error'
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy'}), 200

@app.route('/test_rag', methods=['GET'])
def test_rag():
    """Test RAG functionality directly."""
    try:
        if rag_model is None:
            return jsonify({
                'error': 'Le modèle RAG n\'est pas initialisé.',
                'status': 'error'
            }), 500
            
        test_question = "Qu'est-ce qu'une appendicite?"
        response = rag_model.ask(test_question)
        
        return jsonify({
            'question': test_question,
            'response': response,
            'status': 'success'
        })
    
    except Exception as e:
        app.logger.error(f"Error in test_rag: {str(e)}")
        import traceback
        app.logger.error(f"Full traceback: {traceback.format_exc()}")
        return jsonify({
            'error': str(e),
            'traceback': traceback.format_exc(),
            'status': 'error'
        }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True
    )