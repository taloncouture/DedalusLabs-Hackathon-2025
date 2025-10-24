import asyncio
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv
from dedalus_labs.utils.streaming import stream_async

load_dotenv()



async def main(user_input):
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    result = await runner.run(
        input="""I have a business idea and want to know whether this is a good idea or not: """ + user_input,
        model="openai/gpt-4.1",
        mcp_servers=[
            "joerup/exa-mcp",        # Semantic search engine
            "windsor/brave-search-mcp"  # Privacy-focused web search
        ]
    )

    return result.final_output

#if __name__ == "__main__":
#    asyncio.run(main())
