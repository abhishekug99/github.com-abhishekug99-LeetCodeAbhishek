Bank Request Automation Bot
This repository contains a Python solution for automating the management of incoming banking requests. The bot processes sequential deposit and withdrawal requests while handling a cashback policy for withdrawals.

Problem Simplification
Accounts and Balances:
You start with a list of initial account balances.

Types of Requests:

Deposit: Increase an account's balance by a given amount.
Withdraw: Decrease an account's balance by a given amount.
Cashback Policy: For each withdrawal, 2% of the withdrawn amount (rounded down) is credited back to the account exactly 24 hours later (i.e., 86400 seconds after the withdrawal timestamp).
Important: Only cashback events that occur at or before the timestamp of the last request are processed; any pending cashback after that are ignored.
Error Handling:

Invalid Account Number: If a request refers to an account outside the range of available accounts.
Insufficient Funds: When a withdrawal amount exceeds the account's current balance.
If an invalid request is encountered, the function returns an array containing a single negative integer [-<request_id>], where <request_id> is the 1-based index of the first invalid request.

Logical Explanation of the Code
Precompute Cashback Events:
For every withdrawal request, calculate the cashback amount (2% of the withdrawal, rounded down) and record an event with its execution timestamp (withdrawal timestamp + 86400 seconds).

Processing Requests Sequentially:

For each request, process any pending cashback events (those whose event timestamp is less than or equal to the current request's timestamp).
Validate the account number and, for withdrawals, ensure sufficient funds.
Update the account balance based on the request:
Deposit: Simply add the deposit amount.
Withdraw: Deduct the withdrawal amount if possible.
Post-Processing Cashback Events:
After all requests have been processed, process any remaining cashback events that are due by the last request's timestamp.

Error Detection:
If any request fails validation (e.g., invalid account number or insufficient funds), the process is halted and the function returns the negative index of that request.

Conclusion
This solution efficiently processes each banking request while integrating delayed cashback events. It ensures that account balances are updated in a timely manner and that any invalid transactions are detected early. The approach leverages precomputed events and sequential processing to maintain a clear, logical structure that can be easily understood and modified.

Feel free to explore and extend this code for more complex banking automation tasks!