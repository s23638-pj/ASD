import time


def merge_sort_up(A):
    if len(A) > 1:
        mid = len(A) // 2

        left = A[:mid]
        right = A[mid:]

        merge_sort_up(left)
        merge_sort_up(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1


def merge_sort_down(A):
    if len(A) > 1:
        mid = len(A) // 2

        left = A[:mid]
        right = A[mid:]

        merge_sort_down(left)
        merge_sort_down(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    # tab = Rand_Array.tab
    f = open("Rand_table.txt", "r")
    file = f.read().strip().split(' ')

    tab = [int(x) for x in file]

    start_up = time.time()
    merge_sort_up(tab)
    end_up = time.time()
    time_up = end_up - start_up

    with open("Sorted_up.txt", 'w') as fp:
        for item in tab:
            fp.write("%s " % item)

    start_down = time.time()
    merge_sort_down(tab)
    #print(tab)
    end_down = time.time()
    time_down = end_down - start_down

    with open("Sorted_down.txt", 'w') as fp:
        for item in tab:
            fp.write("%s " % item)

    f.close()