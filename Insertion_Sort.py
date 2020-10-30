def Insertion_Sort(l):

    n = len(l)

    for i in range(1, n):  # 1==>n-1

        value = l[i]

        hole = i

        while hole > 0 and l[hole-1] > value:

            # swap
            l[hole] = l[hole-1]  # curr <== prev # backward # j <== j-1 swap

            hole = hole - 1

        l[hole] = value

    return l


# n = int(input())

# l = [int(input()) for i in range(n)]

# l = [2, 7, 4, 1, 5, 3, 6]
l = [7, 2, 1, 6, 8, 5, 3, 4]

ans = Insertion_Sort(l)

print(ans)


# Time Complexity

# ==> BEST ==> O(N)

# ==> AVERAGE ==> O(N^2)

# ==> WORST ==> O(N^2)

# SPACE COMPLEXITY ==> O(1) # BECAUSE WE ARE NOT USING ANY ADDITIONAL SPACE FOR PERFORMING OPERATIONS
