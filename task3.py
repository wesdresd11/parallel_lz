#Вариант 5
import asyncio
import random
import time


class AsyncDelay:
    def __init__(self, count_files):        
        self.count_files = count_files
        self.files = []
        for i in range(count_files):
            self.files.append(f'file_{i}.txt')

    async def read_file(self, file_name): #async функция мнимого чтения файлов с рандомной задержкой, задержка для i-го файла прошла - чтение файла завершено
        delay = random.uniform(0.1, 5)
        print(f"Начато чтение {file_name}, задержка {delay:.2f} сек")
        await asyncio.sleep(delay)
        print(f"Завершено чтение {file_name}")

    async def run(self): #асинхронное выполнение чтения
        tasks = []
        for file_name in self.files:
            task = asyncio.create_task(self.read_file(file_name))
            tasks.append(task)

        await asyncio.gather(*tasks)

    def start(self):  #начать асинхронное выполнение с выводом временного результата
        start_time = time.time()
        print('3 задача:')
        asyncio.run(self.run())
        end_time = time.time()
        print(f"Общее время выполнения: {end_time - start_time:.2f} сек")


        