#!/usr/bin/env python3

import asyncio
import websockets

async def hello():
    uri = 'ws://localhost:8765'
    async with websockets.connect(uri) as websocket:
        await websocket.send('hello, world')
        print(await websocket.recv())

asyncio.run(hello())
