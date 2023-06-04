from multiprocessing import Pool, cpu_count
import time

def factorize(number):
    factors = []
    for i in range(1, abs(number) + 1):
        if number % i == 0:
            factors.append(i)
    return factors

if __name__ == '__main__':
    numbers = [128, 255, 99999, 10651060]
    start_time = time.time()
    
    # Создание пула процессов с использованием всех  ядер процессора
    with Pool(cpu_count()) as pool:
        results = pool.map(factorize, numbers)
        
    end_time = time.time()
    
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time} секунд")
    print("Результаты:")
    for number, factors in zip(numbers, results):
        print(f"Число {number}: {factors}")
