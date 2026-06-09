🤖 Built a Career Advisor Chatbot using Google Gemini API and Streamlit to provide career guidance, skill recommendations, and personalized learning roadmaps. 🚀 Supports multi-turn conversations with secure API integration, logging, and error handling for a seamless user experience.




# Career Advisor Chatbot 🤖

A simple AI-powered Career Advisor Chatbot built using **Google Gemini API** and **Streamlit**.

The chatbot helps users explore career paths, learn required skills, discover certifications, and get personalized learning roadmaps through natural conversations.

## Features

* Career guidance and recommendations
* Multi-turn conversations
* Gemini API integration
* Streamlit chat interface
* Conversation history
* Error handling and logging
* Secure API key management using `.env`

## Tech Stack

* Python
* Streamlit
* Google Gemini API
* Python Dotenv

## Project Structure

```text
.
├── app.py
├── chatbot/
│   ├── gemini_client.py
│   ├── prompts.py
│   └── logger.py
├── .env
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone <repository-url>

cd <repository-name>

pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

Run the application:

```bash
streamlit run app.py
```

## Sample Questions

* How can I become a Data Scientist?
* What skills are required for AI Engineering?
* Suggest certifications for Cloud Computing.
* Create a roadmap for Full Stack Development.

## Author

Govardhan Reddy
