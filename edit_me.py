#
#  PLEASE PUT YOUR NAME HERE
#

def FindMax(lst):
    """return the maximum element"""

    current_max = lst[0]

    #
    #  YOUR CODE GOES HERE
    #

    return current_max

test_list = [2112*i % 2024 for i in range(10000)]

print(FindMax(test_list))
