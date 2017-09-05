"""collections.deque"""

from collections import deque

queue = deque(["Lily", "JB", "Leia", "Hachi"])
queue.append("Luke")

first = queue.popleft()
print("First : " + first)
first = queue.popleft()
print("First : " + first)

for value in queue:
    print("Name : " + value)

print("Value in loop still exists as "+ value)
