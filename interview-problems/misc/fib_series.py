

def createFibSeries(n):
    first = 0
    second = 1
    series = []
    series.append( first )
    series.append( second )
    for i in xrange(1, n):
        curr = first + second
        series.append( curr )
        first, second = second, curr
    return series

def f(nums, n):
    if n == 0:
        return 0
    elif n == 1 : 
        return 1
    else:
        curr = f(nums, n - 1) + f(nums, n - 2)
        nums.append(curr)
        return curr


if __name__ == "__main__":
    series = createFibSeries(10)
    nums = []
    f(nums, 10)
    print nums

    print series
