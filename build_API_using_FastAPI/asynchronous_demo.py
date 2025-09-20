import asyncio
from timeit import default_timer as timer

async def run_task(name, seconds):
    print(f"Starting task {name} @ {timer()}")
    await asyncio.sleep(seconds)
    print(f"Complete task {name} @ {timer()}")

async def main():
    start =timer()
    await asyncio.gather(
        run_task("task 1", 4),
        run_task("task 2", 2),
        run_task("task 3", 5)
    )
    end = timer()
    print(f"Total time taken for all tasks: {end - start} seconds")

asyncio.run(main())
# Starting task task 1 @ 91732.0597936
# Starting task task 2 @ 91732.0598471
# Starting task task 3 @ 91732.0598634
# Complete task task 2 @ 91734.064372
# Complete task task 1 @ 91736.0586209
# Complete task task 3 @ 91737.0671658
# Total time taken for all tasks: 5.007610000000568 second