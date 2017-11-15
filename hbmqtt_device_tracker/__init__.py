import asyncio


class DeviceTracker:
    def __init__(self, context):
        self.context = context
        self.context.logger.debug('Initialized')

    @asyncio.coroutine
    def on_broker_client_connected(self, client_id):
        self.context.logger.debug('%s connected' % client_id)
        yield from self.context.broadcast_message('location/%s' % client_id, b'home')

    @asyncio.coroutine
    def on_broker_client_disconnected(self, client_id):
        self.context.logger.debug('%s connected' % client_id)
        yield from self.context.broadcast_message('location/%s' % client_id, b'not_home')