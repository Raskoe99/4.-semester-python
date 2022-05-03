from time import sleep


class Compute: 
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        if self.last > 9:
            raise StopIteration()
        self.last += 1
        sleep(.5)
        return self.last

c = Compute()

it = iter(c)

'''for i in it:
    print(i)


def gen_comp():
    for i in range(5000000000):
        yield i

it = gen_comp

next(it)'''

#List comprehensions and Generator expressions
#Det første "i" i funktionenen er outputtet, midten skal være en præcondition
'''list_comprehension = [i    if i % 2 == 0 else "bum"    for i in range(10) ]
print(list_comprehension)'''

#Med generator expression
gen_expr = (i    if i % 2 == 0 else "bum"    for i in range(10))
#Print af en generator giver bare object location
#print(gen_expr)

#I stedet skal der itereres over objektets output
for i in it:
    print(next(gen_expr))