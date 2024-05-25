# Custom models
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm_gpt_4o = ChatOpenAI(
    model = "gpt-4o"
)

llm_gemini_flash = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")