# 🍐🍐


ar = [99, 40, 53, 31, 92, 68, 17, 70, 100, 16, 26, 82, 72, 89, 19, 14, 56, 7, 26, 69, 8, 44, 51, 88, 24, 34, 40, 70, 90, 68, 95, 95, 28, 39, 71, 75, 31, 17, 96, 60, 98, 98, 33, 35, 68, 84, 17, 11, 76,
      17, 45, 61, 72, 76, 18, 67, 55, 81, 57, 43, 45, 96, 58, 49, 4, 61, 38, 66, 82, 16, 44, 100, 50, 19, 82, 15, 72, 5, 81, 97, 94, 70, 7, 92, 75, 55, 1, 87, 4, 9, 92, 35, 83, 20, 53, 8, 90, 2, 92, 82]
k = 32
# ar = [1, 2, 3, 4, 5, 6]
# k = 5
n = len(ar)


def divisibleSumPairs(n, k, ar):
    pairCount = 0
    for i in range(n):
        for j in range(i+1, n):
            if ((ar[i] + ar[j]) % k == 0):
                # print("bingo")
                # print(ar[i], ar[j])
                pairCount += 1
    # print("pairCount: ", pairCount)
    return pairCount


divisibleSumPairs(n, k, ar)
