def Bubble_Sort(l):

    n = len(l)

    for i in range(1, n):

        for j in range(0, n-i-1):

            if l[j] > l[j+1]:

                l[j], l[j+1] = l[j+1], l[j]

    return l


# n = int(input())

# l = [int(input()) for i in range(n)]

l = [2, 7, 4, 1, 5, 3, 6]
# l = [7, 2, 1, 6, 8, 5, 3, 4]

ans = Bubble_Sort(l)

print(ans)

# Time Complexity

# ==> BEST ==> O(N)

# ==> AVERAGE ==> O(N^2)

# ==> WORST ==> O(N^2)

# SPACE COMPLEXITY ==> O(1) # BECAUSE WE ARE NOT USING ANY ADDITIONAL SPACE FOR PERFORMING OPERATIONS
