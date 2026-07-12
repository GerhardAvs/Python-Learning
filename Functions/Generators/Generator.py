

def gen():
    x = 1
    yield x
    
    x += 1
    yield x
    
    x += 1
    yield x
    
g = gen()
print(next(g))
print(next(g))
print(next(g))