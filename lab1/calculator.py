def sum(a, b):
    """ 
    Sum of 2 numbers

    :type a: any
    :param a: First num

    :type b: any
    :param b: Second num

    :raises: none

    :rtype: any
    """

    return a + b

def minus(a, b):
    """ 
    Difference of numbers

    :type a: any
    :param a: first number

    :type b: any
    :param b: second number

    :raises: none

    :rtype: any
    """
    return a - b

def div(a, b):
    """ 
    Division of 2 numbers

    :type a: any
    :param a: first number

    :type b: any
    :param b: second number

    :raises: ZeroDivisionError

    :rtype: float
    """
    if b == 0:
        raise ZeroDivisionError("Can not div by zero")
    
    return a / b