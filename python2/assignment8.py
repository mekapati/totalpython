
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

class ValueVeryLargeError(Error):
    """Raised when the input value is very large"""
    pass


number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number and i_num < number+100:
            raise ValueTooLargeError
        elif i_num > number+100:
            raise ValueVeryLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()
    except ValueVeryLargeError:
        print("This value is Very large, try again!")
        print()
    finally:
        print("The 'try except' is finished")

print("Congratulations! You guessed it correctly.")

