# Metoda lomuto
import sys
import time


sys.setrecursionlimit(10**6)

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort2(A, p, r):
    if p < r:
        q = partition2(A, p, r)
        quick_sort2(A, p, q - 1)
        quick_sort2(A, q + 1, r)


def partition2(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


if __name__ == '__main__':

    #tab = Rand_Array.tab
    f = open("Rand_table.txt", "r")
    file = f.read().strip().split(' ')

    tab = [int(x) for x in file]

    start_up = time.time()
    quick_sort(tab, 0, len(tab) - 1)
    end_up = time.time()
    #print(tab)


    start_down = time.time()
    quick_sort2(tab, 0, len(tab) - 1)
    end_down = time.time()
    #print(tab)

    time_up = end_up - start_up

    time_down = end_down - start_down
    print("\nQuick Sort: Rosnąco " + str(time_up) + "\nQuick Sort: Malejąco " + str(time_down))
    f.close()
    fqs = open("Wyniki.txt", "a")
    fqs.write("\nQuick Sort: Rosnąco " + str(time_up) + "\nQuick Sort: Malejąco " + str(time_down))
    fqs.close()



