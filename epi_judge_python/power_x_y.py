from test_framework import generic_test


def power(x: float, y: int) -> float:
    result,power=1,y

    # if power is negative we solve the problem for 1/x while flipping the sign of the power
    if power<0:
        power,x=-power,1.0/x
    while power:

        # the result is only updated if LSB of power is 1
        if power & 1:
           result*=x

        # in all cases, whether of not result is updated power is shifted right and x->x^2
        x,power=x**2,power>>1
    return result



if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
