"""
An email service tracks messages in a way that enables toggling between read and unread status. 
It primarily toggles the read/unread status of the newest messages, 
while older messages are rarely accessed or tight Which data structure and approach is best for this scenario?
"""


import math



def binomial(n, k):
    # Calculate the binomial coefficient C(n, k) = n! / (k! * (n - k)!)
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)

def decompressVideo(x, y, k):
    result = []
    
    # While there are '0's and '1's to place
    while x > 0 and y > 0:
        # Calculate how many valid strings start with '0' if we place '0' at the current position
        num_ways_with_zero = binomial(x + y - 1, x - 1)
        
        if k <= num_ways_with_zero:
            # If k-th string is within the set of strings starting with '0'
            result.append('0')
            x -= 1
        else:
            # Otherwise, place '1' and adjust k accordingly
            result.append('1')
            k -= num_ways_with_zero
            y -= 1
    
    # If there are '0's left, append all '0's
    result.extend(['0'] * x)
    # If there are '1's left, append all '1's
    result.extend(['1'] * y)
    
    return ''.join(result)