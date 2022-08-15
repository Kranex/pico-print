import uasyncio as asyncio
import re
from lib.nanoweb import Nanoweb, send_file

naw = Nanoweb()

HTTP_OK = '200 OK'

def status(code):
    return b"HTTP/1.1 %s\r\n" % code

def file_of_type(file, types):
    for type in types:
        if file.endswith(type):
            return True
    return False

@naw.route('/*')
async def assets(request):
    await request.write(status(HTTP_OK))
    
    args = {}

    filename = request.url.strip('/')
    if not file_of_type(filename, ['.html', '.js', '.css']):
        args = {'binary': True}

    print("./public/%s" % filename)

    await request.write('\r\n')

    await send_file(
        request,
        "./public/%s" % filename,
        **args,
    )

@naw.route('/')
async def index(request):
    await request.write(status(HTTP_OK))
    await send_file(
        request,
        "./public/index.html"
    )

loop = asyncio.get_event_loop()
loop.create_task(naw.run())
loop.run_forever()
