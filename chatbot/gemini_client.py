import os
import google.generativeai as genai

from dotenv import load_dotenv
from chatbot.logger import logger

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-2.5-flash")


def get_response(chat_history, user_input):

    try:
        MAX_HISTORY = 10
        limited_history = chat_history[-MAX_HISTORY:]
        contents = []

        for msg in limited_history:
            role = "user" if msg["role"] == "user" else "model"
            contents.append({"role": role,"parts": [msg["content"]]})

        contents.append({"role": "user","parts": [user_input]})

        response = model.generate_content(contents)
        logger.info("Gemini API call successful")
        return response.text

    except Exception as e:
        logger.error(f"Gemini API Error: {e}")

        return (
            "Sorry, I am currently unable "
            "to process your request."
        )