class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = [item[0] for item in count.most_common(k)]
        return res