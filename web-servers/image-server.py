from aiohttp import web
from tkinter import filedialog


routes = web.RouteTableDef()
img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
ip = 'localhost'
port = 8080


@routes.get('/')
async def index(request):
    return web.FileResponse(img_path)


app = web.Application()
app.add_routes(routes)
web.run_app(app, host=ip, port=port)
