import asyncio
import websockets
import json
import ssl

def connect():

    uri = "serveruri"

    async def hello():
        async with websockets.connect(uri) as websocket:

            #await websocket.send('test')

            while True:
                try:
                    greeting = await websocket.recv()
                    #greeting = json.loads(greeting)
                    print(greeting)
                except Exception as e:
                    print("HATA: " + str(e))
                    exit()
                # if "_source" in greeting and "related_in_streams" in greeting["_source"]:
                #     print(greeting["_source"]["related_in_streams"])
                    #print(f"< {greeting}")
    print("sss")
    asyncio.get_event_loop().run_until_complete(hello())
    asyncio.get_event_loop().run_forever(ssl=ssl.CERT_NONE)


if __name__ == '__main__':
    connect()

