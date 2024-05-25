from crewai import Agent
from llms import llm_gpt_4o, llm_gemini_flash

researcher_agent = Agent(
    role="Researcher",
    goal="Research and find key details about a {topic}",
    backstory=(
        "You are tasked with researching and identifying key details about {topic}. "
        "Your findings will be crucial for informing the content of a summary "
        "You are good at writing summaries that are very short (2 sentences) but packed with details"
        "Make different searches with additional keywords to find comprehensive information"
    ),
    # tasks="Research the internet for details. Make different searches with additional keywords to find comprehensive information",
    allow_delegation=False,
    llm=llm_gemini_flash,
    verbose=True
)

summarizer_agent = Agent(
    role="Summarizer",
    goal="Write a compelling and detailed summary script about the {topic}. Details are very important.",
    backstory=(
        "You are a skilled writer tasked with creating a summary that captivate and educate listeners. "
        "You are good at building a summary that is coherent and has a story arc if necessary, based on research provided to you."
        "Write a short, but informative summary script using the information provided by the researcher."
    ),
    # tasks="Write a short, but informative summary script using the information provided by the researcher.",
    allow_delegation=False,
    llm=llm_gemini_flash,
    verbose=True
)

expert_curator_agent = Agent(
    role="Expert Senior Curator",
    goal="Curate the research from the researcher agent and select the information that is most informative on {topic}",
    backstory=(
        "As an expert in curation, you select the most important research on the topic {topic}. "
        "This selection will guide the focus of the summary, ensuring details, relevance and interest. "
        "You work with the output of the researcher_agent. If the information is not enough to answer "
        "the user question accurately, ask the researcher_agent to research again."
    ),
    # tasks="Select the top 3 AI-based startups from the list provided by the researcher, based on potential impact and innovation.",
    llm = llm_gpt_4o,
    allow_delegation=True,
    verbose=True
)