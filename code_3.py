
import random
if __name__ == "__main__":
    data = generate_random_data()
    for item in data:
def generate_random_data():

    data = [random.randint(1, 100) for _ in range(10)]
        print(f"Random Number: {item}")

def main():
    return data
    main()
