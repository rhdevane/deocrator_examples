import decorators as decor


def say_whee():
    print("Whee!")


@decor.my_decorator
def my_function():
    print('my function')


@decor.not_during_the_night
def say_whee():
    print("Whee!")


if __name__ == '__main__':

    print("git change")
    # test
    my_function()
    say_whee()
