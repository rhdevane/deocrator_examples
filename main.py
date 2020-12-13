import decorators as decor

def say_whee():
    print("Whee!")

@decor.my_decorator
def my_function():
    print('my function')

@decor.not_during_the_night
def say_whee():
    print("Whee!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    my_function()
    say_whee()
