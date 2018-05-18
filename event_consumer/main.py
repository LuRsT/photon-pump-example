import asyncio

import photonpump


HOST = 'localhost'


async def write_an_event(conn):
    await conn.publish_event(
        'pony_stream', 'pony.jumped', body={
        'name': 'Applejack',
        'height_m': 0.6
    })


async def read_an_event(conn):
    event = await conn.get('pony_stream', max_count=1, direction=photonpump.messages.StreamDirection.Backward)
    print(event[0].event)


async def run():
    async with photonpump.connect(HOST) as conn:
        await write_an_event(conn)
        await read_an_event(conn)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(run())
