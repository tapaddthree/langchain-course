from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from rich import print


llm = ChatOpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
tools = [TavilySearch()]
agent = create_agent(llm, tools)


def main():
    print("Hello from langchain-course!")
    agent.invoke(
        {
            "messages": HumanMessage(
                content="Search for 3 active ai engineer job postings that use langchain. Search linkedin.com. Output their job titles, companies, and links."
            )
        }
    )


if __name__ == "__main__":
    main()
