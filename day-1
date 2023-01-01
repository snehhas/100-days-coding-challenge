#Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if str(i) in d:
                d[str(i)]+=1
            else:
                d[str(i)]=1
        m=max(d.values())
        for i in d.keys():
            if d[str(i)]==m:
                return int(i)
