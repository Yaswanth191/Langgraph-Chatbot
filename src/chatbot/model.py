import cohere
from dotenv import load_dotenv
import os

load_dotenv()

class CohereModel:
    def __init__(self):
        api_key = os.getenv("COHERE_API_KEY")
        if not api_key:
            raise ValueError("COHERE_API_KEY not found in environment variables")
        self.client = cohere.Client(api_key)
    
    def generate_response(self, prompt: str) -> str:
        """Generate response from Cohere model"""
        try:
            response = self.client.generate(
                model="command",
                prompt=prompt,
                max_tokens=100,
                temperature=0.7,
                truncate="END"
            )
            return response.generations[0].text.strip()
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

def create_cohere_model():
    """Factory function to create and return a CohereModel instance"""
    return CohereModel()