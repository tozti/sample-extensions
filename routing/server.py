from tozti.utils import RouterDef
from aiohttp import web
from tozti import logger


router = RouterDef()
foo = router.add_resource('/hello_world')


@foo.get
async def foo_get(req):
    return web.Response(
        text='Hello world!')


MANIFEST = {
    'router': router,
}
