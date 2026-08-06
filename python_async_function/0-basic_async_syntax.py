#!/usr/bin/env python3
"""Task 0 - Module that provides an async coroutine
that takes a random delay before returning it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random amount of time between
    0-10sec and return the delay.
    """

    delay = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return delay
