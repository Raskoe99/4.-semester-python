from contextlib import contextmanager


def averager(*args):
     sum = 0
     for i in args:
            sum += i
     return sum/len(args)


def avrg_generator():
    total = 0.0
    count = 0
    avrg = None
    while True:
        temp = yield avrg
        total += temp
        count += 1
        avrg = total/count


class Openfile:
    def __init__(self, filename, model):
        self.filename = filename
        self.model = model

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass
                  

class makeParagraph:
    def __enter__(self):
        print("<p>", end = " ")

    def __exit__(self, *args):
        print("</p>")

@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    except:
        f.close()

with open_file('textcontent.txt', 'r') as f:
    print(f.read())

