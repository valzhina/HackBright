print("Day 1")
the_file = open("um-deliveries-day-1.txt")
for line in the_file:
    line = line.rstrip()
    # print(type(line))
    words = line.split('|') #split slises string into a list with objects ([word0],[word1],[word2])
    # print(type(words))

    melon = words[0] #thtis is str
    count = words[1] #thtis is str
    amount = words[2] #thtis is str
    # print(type(melon))

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 2")
the_file = open("um-deliveries-day-2.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 3")
the_file = open("um-deliveries-day-3.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[3]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()
