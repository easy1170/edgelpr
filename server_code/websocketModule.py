import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import asyncio
import time
import websockets
import datetime
import multiprocessing as mp

@anvil.server.callable
def startWebsocket():
    async def handler(websocket, path):
        while True:
            await websocket.send("[*] M1 from SERVER 1 "+str(datetime.datetime.now()))
            time.sleep(0.1)

    start_server = websockets.serve(handler, "localhost", 3031)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()