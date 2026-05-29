#Вариант 5
import threading
import random
import time

class LockWriting:
    def __init__(self, ):
        self.threads = 10
        self.lock = threading.Lock()
        self.file_name_1 = "lock_testing.txt"
        self.file_name_2 = "wo_lock_testing.txt"


    def writing_numbers(self): #функция записи в файл с использованием lock, lock ставлю именно на функцию дозаписи в файл
        nums = []
        for _ in range(100):
            num = random.randint(1,1000)
            nums.append(str(num))
        text = '\n'.join(nums)

        with self.lock: 
            with open(self.file_name_1, 'a', encoding = 'utf-8') as f: #дозапись здесь именно потому, что если бы было w, то каждый поток просто бы перезаписывал файл, а так записи будут добавляться
                f.write(text + '\n')
    

    def processing(self):  #функция выполнения задачи с разбиением на потоки
        threads = []
        for _ in range(self.threads):
            t = threading.Thread(target = self.writing_numbers)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
    
    def sequential(self):  #в лабе не написано это делать, но я сделал для себя чисто чтобы сравнить результаы такую же функцию, только без lock и потоков
        numbers = []
        for _ in range(1000):
            num = random.randint(1,1000)
            numbers.append(str(num))
        text = '\n'.join(numbers)
        with open(self.file_name_2, 'a', encoding = 'utf-8')as f:
            f.write(text + '\n')

    
    def compare(self):   #функция сравнения результатов выполненния задачи и вызова функций, выполняющих задачи
        start = time.time()
        self.processing()
        end = time.time()
        print("2 задача:\nВремя выполнения записи с использованием lock:", end - start)

        start = time.time()
        self.sequential()
        end = time.time()
        print("Время выполнения записи последовательно:", end - start)


        