import time
import json
import asyncio
from websockets.server import serve
from websockets.legacy.server import WebSocketServerProtocol
from threading import Thread
from copy import deepcopy
import struct

READ_SIZE = 1000


clients = dict()
ck = 0
sum_size = 0;
async def echo(websocket:WebSocketServerProtocol, path: str):
    global sum_size
    global clients
    clients[hash(websocket)] = websocket


    async for data in websocket:
        print(f"{time.time()} data type {type(data)}")
        if isinstance(data, bytes):
            with open('test.mp3', 'ba') as f:
                f.write(data)

            sum_size += len(data)
            print(f"recv sum_size = {sum_size}")

async def main():
    async with serve(echo, "localhost", 8765, max_size=2**21):
        await asyncio.Future()  # run forever


def th_main():
    asyncio.run(main())

async def tick():
    while True:
        keys = list(clients.keys())
        num = 0
        for k in keys:
            if clients[k].state > 1:
                clients.pop(k)
                continue
            msg = f" - tick {num} {k}"
            print(f"send {k} msg: {msg}")
            await clients[k].send(msg)
            num+=1

        time.sleep(1)
        if len(clients) == 0:
            print(f" - tick empty")


def th_tick():
        asyncio.run(tick());



if __name__ == '__main__':
    th1 = Thread(target=th_main)
    th2 = Thread(target=th_tick)
    th1.start(); th2.start()
    th1.join(); th2.join()
    

    

