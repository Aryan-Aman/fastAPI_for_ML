import time
from timeit import default_timer as timer

def process_task(name, seconds):
    print(f"Starting task: {name} @ {timer()} ")
    time.sleep(seconds) #time taken to complete the task
    print(f"completed task: {name} @ {timer()} ")

start = timer()
print(f"Process started at: {start}")
process_task("task 1", 4)
process_task("task 2", 2)
process_task("task 3", 5)
end=timer()
print(f"Total time taken for all tasks:{end -start} seconds")


# Process started at: 90259.8819822
# Starting task: task 1 @ 90259.8820209 
# completed task: task 1 @ 90263.8823479 
# Starting task: task 2 @ 90263.8825177 
# completed task: task 2 @ 90265.8826762 
# Starting task: task 3 @ 90265.8827214 
# completed task: task 3 @ 90270.883227 
# Total time taken for all tasks:11.001323400007095 seconds