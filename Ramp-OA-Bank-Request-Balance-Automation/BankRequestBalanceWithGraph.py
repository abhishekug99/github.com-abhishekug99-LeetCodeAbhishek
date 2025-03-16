def solution(balances, requests):
    cashback_schedule = {}  # Dictionary to track cashback deposits
    
    for i, request in enumerate(requests):
        parts = request.split()
        action, timestamp, holder_id, amount = parts[0], int(parts[1]), int(parts[2]), int(parts[3])

        # Validate account number
        if holder_id < 1 or holder_id > len(balances):
            return [- (i + 1)]

        if action == "deposit":
            balances[holder_id - 1] += amount

        elif action == "withdraw":
            if balances[holder_id - 1] < amount:  # Validate sufficient balance
                return [- (i + 1)]

            balances[holder_id - 1] -= amount

            # Schedule cashback after 24 hours
            cashback_time = timestamp + 86400
            cashback_amount = amount * 2 // 100  # 2% cashback rounded down
            if cashback_amount > 0:
                if cashback_time not in cashback_schedule:
                    cashback_schedule[cashback_time] = []
                cashback_schedule[cashback_time].append((holder_id - 1, cashback_amount))

        # Process any cashback scheduled at this timestamp before moving forward
        if timestamp in cashback_schedule:
            for acc_id, cashback in cashback_schedule[timestamp]:
                balances[acc_id] += cashback
            del cashback_schedule[timestamp]

    return balances
    
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
    print(solution(balances1, requests1))