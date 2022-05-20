import random
import time

random_start = time.time()
tab = [random.randint(0, 5*10**5) for _ in range(5*10**5)]

random_end = time.time()
#print(tab)
time_rand = random_end - random_start
print("Czas losowania " + str(time_rand))


with open("Rand_table.txt", 'w') as fp:
    for item in tab:
        fp.write("%s " % item)

fhs = open("Wyniki.txt", "w")
fhs.write("Czas losowania " + str(time_rand))
fhs.close()
