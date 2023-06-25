class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # val : index
        # print(nums)

        for index, value in enumerate(nums):
            difference = target - value
            if difference in prevMap:
                print(prevMap[difference], value, target)
                return [prevMap[difference], index]
            prevMap[value] = index
            print(prevMap)    
        return


    twoSum(self="self", nums = [2, 7, 11, 15, 2, 2, 2, 2, 3, 4, 5, 6], target = 21)    

