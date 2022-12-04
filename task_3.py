def hourglass(n):
    size = 2 * n + 1
    for i in range(n):
        print(i * " " + (size - i * 2) * "*" + i * " ")
    
    for i in range(n + 1):
        stars = (2 * i + 1)
        print(((size - stars) // 2) * " " + stars * "*" + ((size - stars) // 2) * " ")
