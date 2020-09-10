import sys

def message(x):
    
    print(x)

    if len(x) == 2:
        print(x[1])
    
    elif len(x) == 3:
        print(x[1])
        print(x[2])

print(message(sys.argv))

