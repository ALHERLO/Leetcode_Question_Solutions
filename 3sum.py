#SOLUTION TO 3SUM USING TWO POINTERS TECHNIQUE

nums = [-1,0,1,2,-1,4, -4]
# [-4, -1, -1, 0, 1, 2, 4]

nums2 = sorted(nums)
j, k = 0, (len(nums) - 1)
triplets = []

for i in range(len(nums2)):
    print("STARTING LOOP ---------------------------------")
    j, k = i+1, (len(nums) - 1)
    diff = -nums2[i]
    print("target sum = ", diff)
    while j < k:
        print("analysing:", nums2[i], nums2[j], nums2[k])
        if nums2[j] + nums2[k] > diff:
             k -= 1
             print("Decrementing k")
        elif nums2[j] + nums2[k] < diff:
             j += 1
             print("incrementing j")
        else:
            print("entering else")
            if nums2[i] != nums2[j] and nums2[i] != nums2[k]:
                triplets.append([nums2[i], nums2[j], nums2[k]])
                print("APPENDING:", nums2[i], nums2[j], nums2[k])
                break
            else:
                break


print(triplets)