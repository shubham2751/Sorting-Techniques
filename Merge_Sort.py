def Merge_Sort(l):

    if len(l) < 2:  # 2 < 2 ==> False, 1 < 2 ==> True

        return l

    mid = len(l)//2

    # print(l[:mid])

    left = Merge_Sort(l[:mid])
    right = Merge_Sort(l[mid:])

    return Merge(left, right)


def Merge(left, right):

    result = []

    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):

        if left[left_pointer] < right[right_pointer]:

            result.append(left[left_pointer])

            left_pointer += 1

        else:

            result.append(right[right_pointer])

            right_pointer += 1

    result.extend(left[left_pointer:])

    result.extend(right[right_pointer:])

    return result


# l = [2, 4, 1, 6, 8, 5, 3, 7]
# l = [8, 7, 6, 5, 4, 3, 2, 1]

# l = [2, 7, 4, 1, 5, 3, 6]
l = [7, 2, 1, 6, 8, 5, 3, 4]

print(l)

ans = Merge_Sort(l)

print(ans)

# Time Complexity

# ==> BEST ==> O(N LOG N)

# ==> AVERAGE ==> O(N LOG N)

# ==> WORST ==> O(N LOG N)

# SPACE COMPLEXITY ==> O(N) # BECAUSE WE ARE USING ADDITIONAL SPACE FOR PERFORMING OPERATIONS. IT IS OUT-PLACE PROCEDURE 
# AND (SELECTION, BUBBLE, INSERTION, QUICK) ARE IN-PLACE PROCEDURE
