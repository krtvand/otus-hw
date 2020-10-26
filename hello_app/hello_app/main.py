from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def health(request):
    return web.Response(text='{"status": "OK"}')


async def liveness(request):
    return web.Response(text='{"status": "OK"}')


async def readiness(request):
    return web.Response(text='{"status": "OK"}')


app = web.Application()
app.add_routes(
    [
        web.get('/', handle),
        web.get('/health', health),
        web.get('/liveness', liveness),
        web.get('/readiness', readiness),
    ]
)


def main():
    web.run_app(app, host='0.0.0.0', port=8000)


if __name__ == '__main__':
    main()
