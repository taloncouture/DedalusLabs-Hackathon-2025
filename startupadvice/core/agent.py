import asyncio
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv
from dedalus_labs.utils.streaming import stream_async

load_dotenv()



async def main(user_input):
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    result = await runner.run(
            input="""You are a business expert and are not afraid to tell the client that their idea is bad or not. End your reasoning with a final answer yes/no:""" + user_input,
        model="openai/gpt-4.1",
        mcp_servers=[
        ]
    )

    return result.final_output

#if __name__ == "__main__":
#    asyncio.run(main())
