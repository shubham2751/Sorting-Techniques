# n = int(input())

# l = [int(input()) for i in range(n)]
# l = [6, 7, 3, 2, 9]

# l = [2, 7, 4, 1, 5, 3]

# l = [2, 7, 4, 1, 5, 3, 6]
l = [7, 2, 1, 6, 8, 5, 3, 4]

print(l)

for i in range(len(l)-1):

    min_v = i

    for j in range(i+1, len(l)):

        if l[min_v] > l[j]:
            min_v = j

    l[i], l[min_v] = l[min_v], l[i]

print(l)
