def announce(f):
    def wrapper():
        print("About to run the funktion ...")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("hello, world!")

hello()