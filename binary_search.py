print("Enter number (1-1000): ")
attempt = 1
num = int(input())
low, high = 1, 1000
current = (low + high) // 2
answer = " "
low, high = 1, 1000
while answer != "=":
    print(f"Is your number {current}? If less, print '<'. If more, print '>'. If correct, print '=': ")
    answer = input()

    match answer:
        case ">":
            attempt += 1
            low = current + 1
        case "<":
            attempt += 1
            high = current - 1
        case "=":
            print(f"Correct! Number of attempts: {attempt}")
            break
        case _:
            print("Please enter a valid response: <, >, or =")

    current = (low + high) // 2
