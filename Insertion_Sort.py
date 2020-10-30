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


'''
l = [7, 2, 4, 1, 5, 3]
     0  1  2  3  4  5

n = 6

iter-i-1: # 1==>6-1=5

        value = l[i] = l[1] = 2

        hole = i = 1

        while-j-1: hole > 0 ==> 1 > 0 && l[hole-1] > value ==> l[1-1=0] > 2

                a[]


'''
