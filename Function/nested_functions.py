
def outer(): # outer
    print("This is the outer function.")
    def inner():
        print("This is the inner function.")
    inner()

outer()


