def snail(snailMap):
    result = []
    if not snailMap or not snailMap[0]:
        return result
    n = len(snailMap)
    if n == 0:
        return result

    top, bottom = 0, n - 1
    left, right = 0, n - 1

    while top <= bottom and left <= right:

        for x in range(left, right + 1):
            result.append(snailMap[top][x])
        top += 1

        for y in range(top, bottom + 1):
            result.append(snailMap[y][right])
        right -= 1

        if top <= bottom:
            for x in range(right, left - 1, -1):
                result.append(snailMap[bottom][x])
            bottom -= 1

        if left <= right:
            for y in range(bottom, top - 1, -1):
                result.append(snailMap[y][left])
            left += 1

    return result

array = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(snail(array))  