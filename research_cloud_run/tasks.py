from tools import search_tool, google_scholar_tool, tavily_search_tool
from agents import researcher_agent, expert_curator_agent, summarizer_agent
from crewai import Task

research_topic = Task(
    description=(
        "Research and identify information that is exactly fulfill the criteria in the {topic}. "
    ),
    expected_output=(
        "A detailed write-up listing information from the research, "
        "including any key details + overview."
    ),
    tools=[search_tool, google_scholar_tool],
    agent=researcher_agent,
)

select_top_information = Task(
    description=(
        "Review the list of information provided by the Researcher. "
        "Evaluate their relevance to select the top three for the summary."
    ),
    expected_output=(
        "A curated list of the top three research items with a comprehensive analysis of why each was chosen, "
        "highlighting their relevance to a informative summary."
    ),
    agent=expert_curator_agent,
)

summarizer_task = Task(
    description=(
        "Craft an engaging and informative 100 word summary that covers the {topic} in as much detail as possible. "
        "Include key details and narratives that would interest the audience."

    ),
    expected_output=(
        "A complete 100 word summary with key details addressing the researched information, "
        "and a key insight that ties together all the found information. Details in the answers are very important."
    ),
    agent=summarizer_agent,
)