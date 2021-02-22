def mult(x, y):
    return ("{} X {} = {}".format(x, y, x*y))

def div(x, y):
    if(y == 0):
        return "ERROR"
    return ("{} / {} = {}".format(x, y, x/y))

def som(x, y):
    return ("{} + {} = {}".format(x, y, x+y))

def sub(x, y):
    return ("{} - {} = {}".format(x, y, x-y))


x = int(input("informe uma valor: \n"))

for i in range(9):
    print(mult(x, i),"\t", som(x, i), "\t", sub(x,i), "\t", div(x, i))