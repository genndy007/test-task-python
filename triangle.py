def triangle(n: int):
    print(*(int('1'*i)*i for i in range(1, n)), sep='\n')


triangle(5)