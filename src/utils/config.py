from dotenv import load_dotenv
import os

load_dotenv()

def get_config():
    """Get configuration from environment variables"""
    return {
        "google_api_key": os.getenv("GOOGLE_API_KEY")
    }