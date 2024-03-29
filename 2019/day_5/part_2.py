# Sunny with a Chance of Asteroids
# Part 2: Rank 16548

with open("input") as input_file:
    position = 0
    numbers = input_file.read().split(",")

    while position < len(numbers):
        number = numbers[position]
        opcode = int(number[-2:])

        m1 = int(number[-3]) if len(number) > 2 else None
        m2 = int(number[-4]) if len(number) > 3 else None
        m3 = int(number[-5]) if len(number) > 4 else None

        if opcode in [1, 2, 5, 6, 7, 8]:
            val_1 = int(numbers[position + 1] if m1 else numbers[int(numbers[position + 1])])
            val_2 = int(numbers[position + 2] if m2 else numbers[int(numbers[position + 2])])

        if opcode in [1, 2, 7, 8]:
            val_3 = int(numbers[position + 3])

        if opcode == 1:
            numbers[int(numbers[position + 3])] = str(val_1 + val_2)
            position += 4

        if opcode == 2:
            numbers[int(numbers[position + 3])] = str(val_1 * val_2)
            position += 4

        if opcode == 3:
            numbers[int(numbers[position + 1])] = input("Program Input: ")
            position += 2

        if opcode == 4:
            print(numbers[int(numbers[position + 1])])
            position += 2

        if opcode == 5:
            if val_1 != 0:
                position = val_2
            else:
                position += 3

        if opcode == 6:
            if val_1 == 0:
                position = val_2
            else:
                position += 3

        if opcode == 7:
            numbers[val_3] = int(val_1 < val_2)
            position += 4

        if opcode == 8:
            numbers[val_3] = int(val_1 == val_2)
            position += 4

        if opcode == 99:
            break