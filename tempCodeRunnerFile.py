from typing import List, Tuple

def largest_rectangle(matrix: List[List[int]]) -> Tuple[int, int]:
    def largest_rectangle_in_histogram(heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return max_area

    max_area = 0
    max_number = None
    dp = [0] * len(matrix[0])
    for row in matrix:
        for i, num in enumerate(row):
            dp[i] = dp[i] + 1 if (dp[i] and num == max_number) else 1
        area = largest_rectangle_in_histogram(dp)
        if area > max_area:
            max_area = area
            max_number = num
    return max_number, max_area