def ScanArray(ArrayName):
    Total = 0
    ZeroCount=0
    for i in (100):
        if i == 0:
            ZeroCount += 1
        Total += i
    AverageValue = Total / 100
    print(ZeroCount," 0")
    print('Average: ', AverageValue)

