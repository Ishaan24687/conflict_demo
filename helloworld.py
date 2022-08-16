def hello_world():
    print(f'Hello World!')

def hello_world(city, state):
    print(f'Hello World {city}, {state}!')


def main():
    hello_world('NYC', 'New York')


main()


def hello_world(city):
    print(f'Hello World {city}!')

def main():
    hello_world('NYC')


main()
