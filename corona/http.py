import asyncio
from typing import Union

from aiohttp import ClientSession
from aiohttp import __version__ as aioversion

from corona import VERSION


class APIError(Exception):
    pass


class NotFound(Exception):
    pass


class HttpClient:
    def __init__(self):
        self.ready = asyncio.Event()
        self.session = None  # type: Union[ClientSession, None]

        async def _init_session():
            self.session = ClientSession(headers={
                "User-Agent": "corona.py/{} aiohttp/{}".format(VERSION, aioversion)
            })
            self.ready.set()

        asyncio.get_event_loop().create_task(_init_session())

    async def request(self, route: str) -> dict:
        await self.ready.wait()
        req = await self.session.get(route)
        if req.status == 404:
            raise NotFound("Country or Province you're trying to find does not exist!")
        if req.status != 200:
            raise APIError("API Returned non OK status code: %s" % str(req.status))
        return await req.json()
