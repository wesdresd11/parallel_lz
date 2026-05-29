#Вариант 5
import threading
import time
import random


class MultithreadingCompare:
    def __init__(self, indices):
        self.indices = indices


    def writing_numbers(self, file_index): #функция создания файлов, если их с таким именем не существует, или открытия существующих и записи рандомных значений
        file_name = f"file_{file_index}.txt"
        nums = []
        for _ in range(100):
            num = random.randint(1,1000)
            nums.append(str(num))
        text = '\n'.join(nums)
        with open(file_name, 'w', encoding = 'utf-8') as f: #w значит открыть файл на перезапись, т.е если текст был, то он удалится и запишется мой, если не было, то просто запишется мой текст
            f.write(text + '\n')


    def processing(self):  #функция разбиения на потоки, взял из лекции
        threads = []
        for i in self.indices:
            t = threading.Thread(target=self.writing_numbers, args=(i,)) #как аргумент передаю индекс фалйа
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    def sequential(self): #функция выполнения задачи без потоков, просто напрямую
        for i in self.indices:
            file_name = f"seq_file_{i}.txt"
            nums = []
            for _ in range(100):
                num = random.randint(1,1000)
                nums.append(str(num))
            text = ' '.join(nums)
            with open(file_name, 'w', encoding = 'utf-8') as f:
                f.write(text)
        


    def compare(self): #функция сравнения и вызова функций, решающих задачи через потоки и просто напрямую с выводом рез-ов в консоль
        start = time.time()
        self.processing()
        end = time.time()
        complete_time = end - start
        print(f'1 задача:\nВремя выполнения задачи с использованием многопточности: {complete_time}')

        start_seq = time.time()
        self.sequential()
        end_seq = time.time()
        seq_complete = end_seq - start_seq
        print(f'Время выполнения задачи без деления на потоки: {seq_complete}')


        