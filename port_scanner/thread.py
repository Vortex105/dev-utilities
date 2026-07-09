import threading


def print_numbers():
    for i in range(1, 6):
        print(i)


def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print(letter)


# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()
