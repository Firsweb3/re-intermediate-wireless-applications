def main():
        print(f"Random Number: {item}")
if __name__ == "__main__":


    data = generate_random_data()

import random

def generate_random_data():
    main()
    data = [random.randint(1, 100) for _ in range(10)]
    return data
    for item in data: