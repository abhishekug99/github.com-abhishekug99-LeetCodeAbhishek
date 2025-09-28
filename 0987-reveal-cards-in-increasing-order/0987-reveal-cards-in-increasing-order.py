class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
 
        deck.sort()
        res=[0]*len(deck)
        idx = deque(range(len(deck)))
        for card in deck:
            res[idx.popleft()] = card
            if idx:
                idx.append(idx.popleft())
        return res

        
            