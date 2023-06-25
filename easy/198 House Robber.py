class Solution: 
    def houseRobber(self, nums = list[int]) -> list[int]:
        rob1, rob2 = 0, 0

        #[rob 1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = n
        return rob2
            
        #rob2 is the most recently robbed house, rob1 is the house robbed previous to that.
            

    
    houseRobber(self = 'self', nums = [1,2,3,6])