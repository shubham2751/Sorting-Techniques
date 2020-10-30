def Quicksort(l, low, high):

    pivot = (low+high)//2

    i = low
    j = high

    while i < j:

        while l[i] < l[pivot]:

            i += 1

        while l[j] > l[pivot]:

            j -= 1

        if i <= j:

            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1

    if low < j:
        Quicksort(l, low, j)

    if i < high:
        Quicksort(l, i, high)


def main():

    # l = [2, 7, 4, 1, 5, 3, 6]
    # l = [7, 2, 1, 6, 8, 5, 3, 4]

    # l = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    Quicksort(l, 0, (len(l)-1))
    print(l)


if __name__ == "__main__":
    main()
