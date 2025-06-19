from langchain_openai import ChatOpenAI
from browser_use import Agent, BrowserSession
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    # Create a headless browser session
    browser_session = BrowserSession(headless=True)
    
    agent = Agent(
        task="Find the address of all Pace CCS offices",
        llm=llm,
        browser_session=browser_session,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
