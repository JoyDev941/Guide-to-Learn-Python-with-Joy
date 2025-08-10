storage = []

def add(x):
    if x != 10:
        storage.append(x)
        add(x + 1)
    else:
        print(storage)
    

add(1)
    