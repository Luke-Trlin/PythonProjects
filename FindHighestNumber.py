import random
import time

def FindHighest(array):
    HighestNumber = 0
    for i in array:
        
        if i <= HighestNumber:
    
            continue

        else:
            HighestNumber = i
            print(f"New highest number found: {HighestNumber}")
    end_time = time.time()
    return HighestNumber


start_time = time.time()
MyArray = [random.randint(0, 100) for _ in range(10)]

# Start the timer

HighestNumberInArray = FindHighest(MyArray)
print(HighestNumberInArray)
print(f"Time taken to find the highest number: {time.time() - start_time} seconds")







