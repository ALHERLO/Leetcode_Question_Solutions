#TWO SUM II LEETCODE PROBLEM 167

numbers = [1, 3, 4, 6, 9, 10, 13, 14, 16, 18]
target = 13

l, r = 0, len(numbers) - 1

while l < r:
    print(l, r)
    if numbers[l] + numbers[r] == target:
        print("Solution:", l+1, r+1)
        break
    if numbers[l] + numbers[r] > target:
        r -= 1

    if numbers[l] + numbers[r] < target:
        l += 1





