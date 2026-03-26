import os
 
class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
 
    @staticmethod
    def validate():
        if not Config.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not set in environment variables")
