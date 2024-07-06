import asyncio
from .process_jobs import start_processing_jobs


async def main():
    await start_processing_jobs()

if __name__ == "__main__":
    asyncio.run(main())