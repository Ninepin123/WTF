storage=[]
passion="yes"
num = 250
def calculate():
    for i in range(0,4):
        num=num//5
        storage[i]=n//num
        n=n%num
    return storage
def is_integer(m):
    try:
        isinteger=int(m)
        isfloat=float(m)
        if isinteger==isfloat:
            return True
        else:
            return False
    except ValueError:
        return False
def tosum():
    global Totaldispatches
    Totaldispatches=0
    for i in range(0,4):
        Totaldispatches+=storage[i]
    return Totaldispatches
while(passion.lower()=="yes"):
    n=input("Please input the number of passengers:")
    if is_integer(n):
        n=int(n)
        storage=calculate()
        Totaldispatches=tosum()
        if n>=0:
            print("Bus={}".format(storage[0]))
            print("Truck={}".format(storage[1]))
            print("SUV={}".format(storage[2]))
            print("Motocycle={}".format(storage[3]))
            print("Totaldispatches={}".format(Totaldispatches))
        else:
            passion=input("輸入格式錯誤，是否要重新輸入（輸入Yes以繼續，輸入非Yes則自動結束，大小寫不拘束）:").lower()
    else:
        passion=input("輸入格式錯誤，是否要重新輸入（輸入Yes以繼續，輸入非Yes則自動結束，大小寫不拘束）:").lower()