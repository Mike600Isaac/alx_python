# is_same_class = __import__('0-is_same_class').is_same_class

# a = 1
# if is_same_class(a, int):
#     print("{} is an instance of the class {}".format(a, int.__name__))
# if is_same_class(a, float):
#     print("{} is an instance of the class {}".format(a, float.__name__))
# if is_same_class(a, object):
#     print("{} is an instance of the class {}".format(a, object.__name__))


"""
   

    Parameters:
        obj: Any Python object.
        a_class: A Python class or class name to compare the type of the object against.

    Returns:
        bool: True if the object is an instance of the specified class or its subclass; otherwise, False.

    Example:
        >>> class Animal:
        ...     pass
        ...
        >>> class Dog(Animal):
        ...     pass
        ...
        >>> class Cat(Animal):
        ...     pass
        ...
        >>> obj1 = Dog()
        >>> obj2 = Cat()
        >>> obj3 = Animal()
        >>>
        >>> is_kind_of_class(obj1, Dog)
        True
        >>> is_kind_of_class(obj2, Animal)
        True
        >>> is_kind_of_class(obj3, Cat)
        False
    """


def is_kind_of_class(obj, a_class):
    """
    Check if the given object is an instance of, or if it is an instance of a class
    that inherited from, the specified class.
     """
    return isinstance(obj, a_class)