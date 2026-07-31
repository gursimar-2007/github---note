people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = 0
count = 0

while len(people) > 1:
    count += 1

    if count == 3:
        print(f"{people[index]}")
        people.pop(index)
        count = 0

        if len(people) > 0:
            index = index % len(people)
    else:
        index = (index + 1) % len(people)

print("Winner:", people[0])
