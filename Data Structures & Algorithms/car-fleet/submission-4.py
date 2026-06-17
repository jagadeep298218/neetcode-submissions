class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        reach = []
        val = {}
        for i in range(len(position)):
            val[position[i]] = speed[i]
       
        position.sort(reverse = True)
        for i in range(len(position)):
            e = (target - position[i])/val[position[i]]
            if reach and e <= reach[-1]:
                continue
            reach.append(e)
        
        return len(reach)


