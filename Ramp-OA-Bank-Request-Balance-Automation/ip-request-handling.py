from collections import deque

def solution(timestamps, ipAddresses, limit, timeWindow):
 
    requests_per_ip = {}  # Maps IP -> deque of timestamps for accepted requests
    results = []

    for t, ip in zip(timestamps, ipAddresses):
        if ip not in requests_per_ip:
            requests_per_ip[ip] = deque()

        while requests_per_ip[ip] and (t - requests_per_ip[ip][0]) > timeWindow:
            requests_per_ip[ip].popleft()

        if len(requests_per_ip[ip]) < limit:
            results.append(1)
            requests_per_ip[ip].append(t)
        else:
            results.append(0)

    return results

timestamps = [1600000000000, 1600000000000, 1600000000001] 
ipAddresses = ["56.75.0.49", "62.2.159.38", "62.2.159.38"]
limit = 2
timeWindow = 10

output = solution(timestamps, ipAddresses, limit, timeWindow)
print("Output:", output) 
