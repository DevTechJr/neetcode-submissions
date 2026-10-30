class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        myMap = {}

        for num in nums:
            if myMap.get(num) == None:
                myMap[num] = True
            else:
                return num
        
        