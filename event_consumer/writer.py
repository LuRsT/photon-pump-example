import asyncio

import photonpump


async def write_event(conn):
    await conn.publish_event(
        'adventure',
        'player_created',
        body={'name': 'Gil'}
    )

async def run():
    async with photonpump.connect('172.17.0.2') as conn:
        await write_event(conn)

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(run())
