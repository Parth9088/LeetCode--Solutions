class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        New_num = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count +=1
            New_num.append(count)
                
        return New_num