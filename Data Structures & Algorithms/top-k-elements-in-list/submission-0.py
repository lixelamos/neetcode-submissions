from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element in the array
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Step 2: Sort elements by frequency and get the top k
        # Create a list of (num, freq) and sort it by freq in descending order
        sorted_items = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        
        # Step 3: Extract the top k elements
        top_k = [item[0] for item in sorted_items[:k]]
        
        return top_k

# Example usage:
solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(solution.topKFrequent(nums, k))  # Output: [1, 2]

nums = [4, 4, 4, 4, 6, 6, 2, 2, 2, 2, 3, 3]
k = 3
print(solution.topKFrequent(nums, k))  # Output: [4, 2, 6]
