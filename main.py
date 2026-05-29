#Вариант 5
from task1 import MultithreadingCompare
from task2 import LockWriting
from task3 import AsyncDelay


def main():
    indices = list(range(10))
    writer = MultithreadingCompare(indices)
    writer.compare()

    sync = LockWriting()
    sync.compare()

    reader = AsyncDelay(10)
    reader.start()


if __name__ == "__main__":
    main()