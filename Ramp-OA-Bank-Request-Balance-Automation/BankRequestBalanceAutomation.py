def solution(balances, requests):
    # Precompute cashback events for all withdrawals.
    cashback_events = []  # Each event: (event_time, account, cashback_amount)
    for req in requests:
        tokens = req.split()
        if tokens[0] == "withdraw":
            timestamp = int(tokens[1])
            account = int(tokens[2])
            amount = int(tokens[3])
            cashback = (amount * 2) // 100  # 2% rounded down
            cashback_events.append((timestamp + 86400, account, cashback))
    
    # Pointers for requests and cashback events.
    cash_idx = 0
    num_cashbacks = len(cashback_events)
    last_timestamp = int(requests[-1].split()[1])
    
    # Process each request, merging with cashback events.
    for i, req in enumerate(requests):
        tokens = req.split()
        req_type = tokens[0]
        timestamp = int(tokens[1])
        
        # Process pending cashback events due before or at current request's timestamp.
        while cash_idx < num_cashbacks and cashback_events[cash_idx][0] <= timestamp:
            event_time, account, cashback = cashback_events[cash_idx]
            balances[account - 1] += cashback
            cash_idx += 1

        # Validate account.
        holder_id = int(tokens[2])
        if holder_id < 1 or holder_id > len(balances):
            return [-(i + 1)]
        amount = int(tokens[3])
        
        # Process the request.
        if req_type == "deposit":
            balances[holder_id - 1] += amount
        elif req_type == "withdraw":
            if balances[holder_id - 1] < amount:
                return [-(i + 1)]
            balances[holder_id - 1] -= amount
        else:
            return [-(i + 1)]
    
    # Process any remaining cashback events that are due by the last request timestamp.
    while cash_idx < num_cashbacks and cashback_events[cash_idx][0] <= last_timestamp:
        event_time, account, cashback = cashback_events[cash_idx]
        balances[account - 1] += cashback
        cash_idx += 1

    return balances

# Example usage:
if __name__ == "__main__":
    # Example 1:
    balances1 = [1000, 1500]
    requests1 = [
        "withdraw 1613327630 2 480",
        "withdraw 1613327644 2 800",
        "withdraw 1614105244 1 100",
        "deposit 1614108844 2 200",
        "withdraw 1614108845 2 150"
    ]
    print(solution(balances1, requests1))  # Expected output: [900, 295]
