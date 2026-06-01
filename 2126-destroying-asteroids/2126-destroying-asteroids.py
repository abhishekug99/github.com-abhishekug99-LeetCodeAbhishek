class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if a>mass:
                return False
            mass+=a
        return True

        # vistedastro = set()
        # def getNext(asteroids, mass):
        #     startastro = 0
        #     for n in asteroids:
        #         if n <=mass and n not in vistedastro:
        #             startastro = max(n, startastro)
        #             vistedastro.add(n)
        #     return startastro
        
        # for i in range(len(asteroids)):
        #     newMass = getNext(asteroids, mass)
        #     mass+=newMass
        
        # if len(vistedastro) == len(asteroids):
        #     return True    
        
        # return False

            