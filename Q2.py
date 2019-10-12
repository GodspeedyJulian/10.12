def Sensor():
    return 70

def CheckTemp():
    while True:
        ID = float(input('ID: '))
        if 1 <= ID <= 10 and ID == int(ID):
            break
    Temp = Sensor
    ()
    print('Temperature: ', Temp)
    if Temp >= 40:
        print('Alarm')
    elif Temp <= 20:
        print('Cold')
    else:
        print('Normal')
CheckTemp()
