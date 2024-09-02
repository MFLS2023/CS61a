def fizzbuzz(n):
    i=0
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"

    while i in range(0,n):
        if i%3==0 and i%5!=0:
            print("fizz")
        elif i%5==0 and i%3!=0:
            print("buzz")
        elif i%3==0 and i%5==0:
            print("fizzbuzz")
        else :
            print(i)
        i+=1


