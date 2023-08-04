def insertion_sort(arr: list) -> list:
    """
    Performs an insertion sort in Python
    """

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

    return arr

# Example usage; this will only execute if you run `main.py`
if __name__ == "__main__":
    import random

    n = 10 # Number of random numbers (exclusive)
    numbers = [int(random.random() * 100) for x in range(n)]
    print(insertion_sort(numbers))
