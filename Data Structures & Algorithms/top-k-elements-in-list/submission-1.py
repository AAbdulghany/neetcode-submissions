class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fequency_list = [[] for i in range(len(nums)+1)]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)\

        for num,cnt in count.items():
            fequency_list[cnt].append(num)
        
        result = []
        for i in range(len(fequency_list)-1, 0, -1):
            for num in fequency_list[i]:
                result.append(num)
                if len(result) == k:
                    return result
