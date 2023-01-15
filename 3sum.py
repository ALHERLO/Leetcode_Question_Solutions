#SOLUTION TO 3SUM USING TWO POINTERS TECHNIQUE

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -1]

i, j = 0, (len(nums) - 1)

triplets = []

print(i, j)

while j >= i :
    print("i:", nums[i], "      j:", nums[j])
    i += 1
    j -= 1
    k = 0
    while k < len(nums) - 1:

        if k == i or k == j:
            k += 1
        print("k: ", nums[k])
        if nums[i] + nums[j] + nums[k] == 0 and i != j and i != k and j != k:
            triplets.append([nums[i], nums[j], nums[k]])
            print()
        k += 1

print(triplets)
