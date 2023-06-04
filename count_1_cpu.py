from multiprocessing import Pool, cpu_count
import time

def factorize(*numbers):
    results = []
    for number in numbers:
        factors = []
        for i in range(1, abs(number) + 1):
            if number % i == 0:
                factors.append(i)
        results.append(factors)
    return results


start_time = time.time()
a, b, c, d = factorize(128, 255, 99999, 10651060)
end_time = time.time()

execution_time = end_time - start_time
print(f"Время выполнения: {execution_time} секунд")





