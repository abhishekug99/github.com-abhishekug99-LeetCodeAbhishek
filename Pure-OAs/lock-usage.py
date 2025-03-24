"""
Lock Usage
Write a program that, given a list of N (0<=N<=1,000,000) lock acquire and release events (counting from 1), checks if there were any problems (acquire release order violation, dangling acquired lock, acquiring a lock twice or releasing a free lock, and if so, tells the earliest time that could be detected.

Note that there's no limit on how many nested locks may be acquired at any given moment

More formally, you are given an array of strings where each string is either "ACQUIRE X" or "RELEASE X" where all Xs are integers in the range [1..1000000).

Return:

Q. if there were no lock-related problems even after program termination

N+1, if the only issue after program termination were dangling acquired locks

K. in case event number K violated any of the principles (release a lock not acquired previously, acquire an already held lock Off violate lock acquire-release D

ordering).

Examples:

Input:

1. ACQUIRE 364

2. ACQUIRE 84

3. RELEASE 84

4. RELEASE 364

Output: 0 (nothing bad happenedj

Input:

1. ACQUIRE 364

2. ACQUIRE BA

3. RELEASE 364

RELEASE 84
Output: 3 (lock 84 should have been released before releasing 364)

Input:

1. ACQUIRE 123

2. ACQUIRE 364

3. ACQUIRE 84

4. RELEASE 84

5. RELEASE 364

6. ACQUIRE 456

Output: 7 (upon terminating, not all locks were released, namely 123 and 456, but we can't know that untii actually exiting)

Input:

1. ACQUIRE 123

2. ACQUIRE 364

3. ACQUIRE 84

4. RELEASE 84

5. RELEASE 364

6. ACQUIRE 789

7. RELEASE 456

8. RELEASE 123

Output: 7 (releasing a lock not acquired before)

Input:

1. ACQUIRE 364

2. ACQUIRE 84

3. ACQUIRE 364

4. RELEASE 364

Output: 3 (acquiring an already held lock)

Approach:
We can solve this problem by simulating the log events with a stack and a set. The stack will keep track of the order in which locks are acquired. The set lets us quickly check if a lock is already held. For each event (indexed starting at 1), we do the following:

ACQUIRE X:

If X is already in our “acquired” set, then the log is wrong and we return the event index immediately.

Otherwise, we push X onto the stack and add it to the set.

RELEASE X:

If X is not in the acquired set, then we are releasing a lock that was never acquired—return the event index.

If the lock on the top of the stack is not X (i.e. the locks are not being released in reverse order), then return the event index.

Otherwise, pop the stack and remove X from the set.

After processing all events, if there are still locks in the stack (dangling acquired locks), then the error is only detected at program termination. In that case we return N+1 (where N is the number of events).

If none of these errors occur, we return 0.
"""

def check_log_history(events):
    acquired = set()  # to track currently held locks
    stack = []        # to enforce LIFO order

    for i, event in enumerate(events, start=1):
        parts = event.split()
        action = parts[0]
        lock = parts[1]

        if action == "ACQUIRE":
            # if the lock is already acquired, error at event i.
            if lock in acquired:
                return i
            acquired.add(lock)
            stack.append(lock)
        elif action == "RELEASE":
            # releasing a lock not acquired is an error.
            if lock not in acquired:
                return i
            # must release in reverse order: top of the stack must be the lock.
            if stack[-1] != lock:
                return i
            # valid release: remove lock.
            stack.pop()
            acquired.remove(lock)
        else:
            # In case of unexpected command.
            raise ValueError("Invalid event action")

    # After processing all events, if any locks remain acquired, that's an error.
    if stack:
        return len(events) + 1

    return 0


# Test cases based on the problem examples:

# Example 1
events1 = [
    "ACQUIRE 364",
    "ACQUIRE 84",
    "RELEASE 84",
    "RELEASE 364"
]
print("Example 1 Output:", check_log_history(events1))  # Expected: 0

# Example 2
events2 = [
    "ACQUIRE 364",
    "ACQUIRE 84",
    "RELEASE 364",
    "RELEASE 84"
]
print("Example 2 Output:", check_log_history(events2))  # Expected: 3

# Example 3
events3 = [
    "ACQUIRE 123",
    "ACQUIRE 364",
    "ACQUIRE 84",
    "RELEASE 84",
    "RELEASE 364",
    "ACQUIRE 456"
]
print("Example 3 Output:", check_log_history(events3))  # Expected: 7

# Example 4
events4 = [
    "ACQUIRE 123",
    "ACQUIRE 364",
    "ACQUIRE 84",
    "RELEASE 84",
    "RELEASE 364",
    "ACQUIRE 789",
    "RELEASE 456",
    "RELEASE 123"
]
print("Example 4 Output:", check_log_history(events4))  # Expected: 7

# Example 5
events5 = [
    "ACQUIRE 364",
    "ACQUIRE 84",
    "ACQUIRE 364",
    "RELEASE 364"
]
print("Example 5 Output:", check_log_history(events5))  # Expected: 3
