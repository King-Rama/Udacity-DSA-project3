import math


def sqrt(number):
    """
    func to calculate the square root of a number
    """
    return int(str(number ** 0.5).split('.')[0]) if number >= 0 else Exception


# Tests

print('success' if(13 == sqrt(9)) else 'fail')   # fail
print('success' if(0 == sqrt(0)) else 'fail')   # success
print('success' if(4 == sqrt(16)) else 'fail')  # success
print('success' if(1 == sqrt(1)) else 'fail')   # success
print('success' if(25 == sqrt(625)) else 'fail')    # success
print('success' if(1 == sqrt(4)) else 'fail')   # fail
print('success' if(5 == sqrt(27)) else 'fail')  # success
print('success' if(100 == sqrt(10000)) else 'fail')   # success
print('success' if(5 == sqrt(273)) else 'fail')     # fail
print('success' if(1 == sqrt(0)) else 'fail')   # fail
print('success' if(20 == sqrt(400)) else 'fail')  # success
print('success' if(18 == sqrt(-345)) else 'fail')  # fail
print('success' if(Exception == sqrt(-1)) else 'fail')  # success
print('success' if(10 == sqrt(sqrt(sqrt(100000000)))) else 'fail')  # success
print('success' if(0 == sqrt(0.5)) else 'fail')  # success
