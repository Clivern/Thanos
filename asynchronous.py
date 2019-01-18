import asyncio
import time
from datetime import datetime


async def sleep(n, name):
    print("Sleeping %d Seconds Task %s" % (n, name))
    time.sleep(n)

async def task(name, hold):
    print("Starting Task %s" % name)
    await sleep(hold, name)
    print("Closing Task %s" % name)


start = time.time()
loop = asyncio.get_event_loop()

tasks = [
    asyncio.ensure_future(task("A", 6)),
    asyncio.ensure_future(task("B", 4)),
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print("Total time: {}".format(end - start))
