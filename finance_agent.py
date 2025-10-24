import asyncio
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv
from dedalus_labs.utils.streaming import stream_async

load_dotenv()

async def main():
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    result = await runner.run(
        input="""You are a financial expert. Can you help me find:
        1. The current stock price for Google (GOOG)
        2. Whether I should invest in Google today?
        
        """,
        model="openai/gpt-4.1",
        mcp_servers=["aq_humor/yahoo-finance-mcp"]
    )

    print(f"Stock Results:\n{result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())
