from multiprocessing.pool import ThreadPool
import os
import time
import random



def writing_numbers(file_index):
    file_name = f"file_{file_index}.txt"
    nums = []
    for i in range(100):
        num = random.randint(1,1000)
        nums.append(str(num))
    text = ' '.join(nums)
    with open(file_name, 'w', encoding = 'utf-8') as f:
        f.write(text)


def processing(indices):
    with ThreadPool(processes = 10) as pool:
        pool.map(writing_numbers, indices)

def sequential(indices):
    for i in indices:
        file_name = f"seq_file_{i}.txt"
        nums = []
        for i in range(100):
            num = random.randint(1,1000)
            nums.append(str(num))
        text = ' '.join(nums)
        with open(file_name, 'w', encoding = 'utf-8') as f:
            f.write(text)
    


if __name__ == "__main__":
    indices = list(range(10))
    start = time.time()
    processing(indices)
    end = time.time()
    complete_time = end - start
    print(complete_time)
    start_seq = time.time()
    sequential(indices)
    end_seq = time.time()
    seq_complete = end_seq - start_seq
    print(seq_complete)



