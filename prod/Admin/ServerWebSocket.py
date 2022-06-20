import websockets
import asyncio


async def echo(websocket, path):
    cmd = input()
    while True:

        if cmd == "exit":
            break
        await websocket.send(cmd)
        cmd_output = await websocket.recv()
        cmd = input(cmd_output)


start_server = websockets.serve(echo, "localhost", 5566)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
