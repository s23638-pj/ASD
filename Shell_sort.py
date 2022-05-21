import time


def shell_sort_up(tab, n):
    gap = n // 2

    while gap > 0:
        j = gap

        while j < n:
            i = j - gap

            while i >= 0:
                if tab[i + gap] > tab[i]:

                    break
                else:
                    tab[i + gap], tab[i] = tab[i], tab[i + gap]

                i = i - gap
            j += 1
        gap = gap // 2


# def shell_sort_down(tab, n):
#     gap = n // 2
#
#     while gap > 0:
#         j = gap
#
#         while j < n:
#             i = j - gap
#
#             while i >= 0:
#                 if tab[i + gap] < tab[i]:
#
#                     break
#                 else:
#                     tab[i + gap], tab[i] = tab[i], tab[i + gap]
#
#                 i = i - gap
#             j += 1
#         gap = gap // 2


if __name__ == '__main__':
    # tab = Rand_Array.tab

    f = open("Rand_table.txt", "r")
    file = f.read().strip().split(' ')

    tab = [int(x) for x in file]

    start_rand = time.time()
    shell_sort_up(tab, len(tab))
    # print(tab)
    end_rand = time.time()
    time_rand = end_rand - start_rand

    f = open("Sorted_up.txt", "r")
    file = f.read().strip().split(' ')

    tab = [int(x) for x in file]

    start_up = time.time()
    shell_sort_up(tab, len(tab))
    # print(tab)
    end_up = time.time()
    time_up = end_up - start_up

    f = open("Sorted_down.txt", "r")
    file = f.read().strip().split(' ')

    tab = [int(x) for x in file]

    start_down = time.time()
    shell_sort_up(tab, len(tab))
    # print(tab)
    end_down = time.time()
    time_down = end_down - start_down
    print("\nShell Sort: Z losowej: " + str(time_rand) + "\nShell Sort: Z posortowanej: " + str(time_up) + "\nShell Sort: Z odwrotnie posortowanej: " + str(time_down))
    f.close()
    fhs = open("Wyniki.txt", "a")
    fhs.write("\nShell Sort: Z losowej: " + str(time_rand) + "\nShell Sort: Z posortowanej: " + str(time_up) + "\nShell Sort: Z odwrotnie posortowanej: " + str(time_down))
    fhs.close()
