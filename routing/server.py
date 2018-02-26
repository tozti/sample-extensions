from tozti.utils import RouterDef
from aiohttp import web

router = RouterDef()
foo = router.add_route('/hello_world')


@foo.get
async def foo_get(req):
    return web.Response(
        text='Hello world!')


MANIFEST = {
    'name': 'routing',
    'router': router,
}
