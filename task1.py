def oops(x):
    return "IndexError"


def second():
    try:
        raise oops()
    except IndexError:
        print("catch")
