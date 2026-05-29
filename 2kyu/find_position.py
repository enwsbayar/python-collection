# When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process --myjinxin2015 said

# Description:
# There is a infinite string. You can imagine it's a combination of numbers from 1 to n, like this:

# "123456789101112131415....n-2n-1n"
# Please note: the length of the string is infinite. It depends on how long you need it(I can't offer it as a argument, it only exists in your imagination) ;-)

# Your task is complete function findPosition that accept a digital string num. Returns the position(index) of the digital string(the first appearance).

# For example:

# findPosition("456") == 3
# because "123456789101112131415".indexOf("456") = 3
#             ^^^
# Is it simple? No, It is more difficult than you think ;-)

# findPosition("454") = ?
# Oh, no! There is no "454" in "123456789101112131415",
# so we should return -1?
# No, I said, this is a string of infinite length.
# We need to increase the length of the string to find "454"

# findPosition("454") == 79
# because "123456789101112131415...44454647".indexOf("454")=79
#                                    ^^^
# The length of argument num is 2 to 15. So now there are two ways: one is to create a huge own string to find the index position; Or thinking about an algorithm to calculate the index position.

# Which way would you choose? ;-)

# Some examples:
#  findPosition("456") == 3
#  ("...3456...")
#        ^^^
#  findPosition("454") == 79
#  ("...444546...")
#         ^^^
#  findPosition("455") == 98
#  ("...545556...")
#        ^^^
#  findPosition("910") == 8
#  ("...7891011...")
#         ^^^
#  findPosition("9100") == 188
#  ("...9899100101...")
#          ^^^^
#  findPosition("99100") == 187
#  ("...9899100101...")
#         ^^^^^
#  findPosition("00101") == 190
#  ("...99100101...")
#          ^^^^^
#  findPosition("001") == 190
#  ("...9899100101...")
#            ^^^
#  findPosition("123456789") == 0
#  findPosition("1234567891") == 0
#  findPosition("123456798") == 1000000071
# A bit difficulty, A bit of fun, happy coding ;-)


def _digits_count(n: int) -> int:
    if n <= 0:
        return 0

    length = 1
    start = 1
    count = 0

    while start * 10 <= n:
        count += 9 * start * length
        length += 1
        start *= 10

    count += (n - start + 1) * length
    return count


def _generate_candidates(num: str) -> set[int]:
    candidates: set[int] = {1, 2}
    n = len(num)

    for size in range(1, n + 1):
        for i in range(0, n - size + 1):
            token = num[i : i + size]
            if token[0] == "0" and token != "0":
                continue
            value = int(token)
            candidates.add(value)
            candidates.add(value - 1)
            candidates.add(value + 1)

    return {value for value in candidates if value >= 1}


def _build_segment(start: int, end: int) -> str:
    return "".join(str(i) for i in range(start, end + 1))


def findPosition(num: str) -> int:
    if not num:
        return 0

    candidates = _generate_candidates(num)
    best_position = None

    for value in sorted(candidates):
        start = max(1, value - 20)
        end = value + 20
        segment = _build_segment(start, end)
        offset = segment.find(num)

        if offset == -1:
            continue

        position = _digits_count(start - 1) + offset
        if best_position is None or position < best_position:
            best_position = position

    if best_position is not None:
        return best_position

    start = 1
    segment = ""
    while True:
        segment += str(start)
        if len(segment) >= len(num) + 100:
            index = segment.find(num)
            if index != -1:
                return index
            segment = segment[-(len(num) + 50) :]
        start += 1


if __name__ == "__main__":
    tests = {
        "456": 3,
        "454": 79,
        "455": 98,
        "910": 8,
        "9100": 188,
        "99100": 187,
        "00101": 190,
        "001": 190,
        "123456789": 0,
        "1234567891": 0,
        "123456798": 1000000071,
    }

    for key, expected in tests.items():
        result = findPosition(key)
        assert result == expected, f"{key}: expected {expected}, got {result}"

    print("All tests passed.")

