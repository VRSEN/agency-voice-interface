import asyncio
from agency_swarm.tools import BaseTool
from datetime import datetime


class GetCurrentTime(BaseTool):
    """
    A tool to get the current time.
    """

    async def run(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    tool = GetCurrentTime()
    print(asyncio.run(tool.run()))