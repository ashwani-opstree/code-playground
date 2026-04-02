def palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

print(palindrome("A man, a plan, a canal: Panama"))
def palindrome_no(nums: int) -> bool:
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1

    return True

print(palindrome(123))