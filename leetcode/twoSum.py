def twoSum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hashmap:
            print("test")
            print(num)
            print(hashmap[complement])
            return [hashmap[complement], i]

        hashmap[num] = i
        print(f"Hashmap: {hashmap}")

def main():
    nums = [2, 7, 11, 15]
    target = 26
    result = twoSum(nums, target)
    print(result)  

if __name__ == "__main__":
    main()