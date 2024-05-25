from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
load_dotenv()

# Custom imports from src directory
from crewai import Crew
from agents import summarizer_agent, researcher_agent, expert_curator_agent
from llms import ChatOpenAI, ChatGoogleGenerativeAI
from tasks import research_topic, select_top_information, summarizer_task



# Initialize LLM models
llm_gpt_4o = ChatOpenAI(model="gpt-4o")
llm_gemini_flash = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

# Initialize Crew with agents and tasks
crew = Crew(
    agents=[
        researcher_agent,
        expert_curator_agent,
        summarizer_agent
    ],
    tasks=[
        research_topic,
        select_top_information,
        summarizer_task
    ],
    verbose=2,
    memory=True
)


# Read API key from environment variable
API_KEY = os.getenv('FUNC_API_KEY')

def research_function(request):
    data = request.get_json()
    api_key = request.headers.get('x-api-key')

    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    topic = data.get('topic', '')
    if not topic:
        return jsonify({"error": "No topic provided"}), 400

    inputs = {"topic": topic}
    result = crew.kickoff(inputs=inputs)
    return jsonify(result)
