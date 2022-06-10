targets = list(map(int, input().split('|')))

line = input().split("@")
while line[0] != "Game over":
    command = line[0]

    if command == "Shoot Left":
        start_index = int(line[1])
        length = int(line[2])
        result = len(targets) - ((start_index + length) % len(targets))
        if 0 <= start_index < len(targets):
            targets[result] -= 5
            print(result)
            print(targets)


    elif command == "Shoot right":
        start_index = int(line[1])
        length = int(line[2])
        result = (start_index + length) % len(targets)
        if 0 <= start_index < len(targets):
            targets[result] -= 5
            print(result)
            print(targets)
    line = input().split("@")