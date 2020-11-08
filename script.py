#!/bin/env python

def add_one(number):
    """A function that adds one to the number given and returns it"""
    return number + 1


def add_name(func):
    def wrapper():
        print(f'Hey, Vincent!')
        func()

    return wrapper


def Hello_World():
    print("Hello, World!")

Hello_World = add_name(Hello_World)


if __name__ == "__main__":
    Hello_World()

    print(add_one)
    print(add_one(3))
    print(add_one(9))