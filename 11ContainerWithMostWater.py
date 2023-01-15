res = set()
maxheight = height[len(height) - 1]

for i in range(0, len(height)):
    j = len(height) - 1
    if height[i] < height[i - 1]:
        continue

    while j > i:
        if height[j] >= maxheight:
            if height[j] < height[i]:
                res.add((j - i) * (height[j]))
            else:
                res.add((j - i) * (height[i]))
        j -= 1

return max(res)