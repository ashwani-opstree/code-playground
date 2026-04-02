class Solution:
    # def mySqrt(self, x: int) -> int:
    #     return int(x ** 0.5)
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right

print(Solution().mySqrt(8))