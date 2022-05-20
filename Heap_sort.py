import time



def heapify_up(tab, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and tab[i] < tab[l]:
        largest = l

    if r < n and tab[largest] < tab[r]:
        largest = r

    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        heapify_up(tab, n, largest)


def heapify_down(tab, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and tab[i] > tab[l]:
        smallest = l

    if r < n and tab[smallest] > tab[r]:
        smallest = r

    if smallest != i:
        tab[i], tab[smallest] = tab[smallest], tab[i]
        heapify_down(tab, n, smallest)


def heap_sort_up(tab):
    n = len(tab)

    for i in range(n // 2, -1, -1):
        heapify_up(tab, n, i)

    for i in range(n - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]

        heapify_up(tab, i, 0)


def heap_sort_down(tab):
    n = len(tab)

    for i in range(n // 2, -1, -1):
        heapify_down(tab, n, i)

    for i in range(n - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]

        heapify_down(tab, i, 0)


if __name__ == '__main__':
    #tab = Rand_Array.tab

    f = open("Rand_table.txt", "r")
    file = f.read().strip().split(' ')

    tab = [int(x) for x in file]

    start_up = time.time()
    heap_sort_up(tab)
    #print(tab)
    end_up = time.time()
    time_up = end_up - start_up

    start_down = time.time()
    heap_sort_down(tab)
    #print(tab)
    end_down = time.time()
    time_down = end_down - start_down

    print("\nHeap Sort: Rosnąco " + str(time_up) + "\nHeap Sort: Malejąco " + str(time_down))
    f.close()
    fhs = open("Wyniki.txt", "a")
    fhs.write("\nHeap Sort: Rosnąco " + str(time_up) + "\nHeap Sort: Malejąco " + str(time_down))
    fhs.close()