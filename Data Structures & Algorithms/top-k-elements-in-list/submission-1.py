from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        easy part is frequency map, use counter as a shortcut
        the hard part is how to grab k largest counts
        we can use bucket sort!
        '''
        count_map = Counter(nums)

        # list comprehension
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count_map.items():
            buckets[freq].append(num)

        results = []
        for bucket in reversed(buckets):
            for num in bucket:
                results.append(num)
            if len(results) == k:
                return results

