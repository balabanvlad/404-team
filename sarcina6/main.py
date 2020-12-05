# Sarcina 2.1


class Lab():
    def __init__(self):
        self.stiva = []
        self.flag = []
        self.matrix = []
        self.k = 0

    def up(self, i, j):
        # print('up')
        i1 = i
        number = ''
        while True:
            i1 = i1 + 1
            try:
                int(self.matrix[i1][j])
            except:
                break
            number += self.matrix[i1][j]
        number = int(number)
        self.action(i - number, j)

    def down(self, i, j):
        # print('down')
        i1 = i
        number = ''
        while True:
            i1 = i1 - 1
            try:
                int(self.matrix[i1][j])
            except:
                break
            number += self.matrix[i1][j]
        number = int(number)
        self.action(i + number, j)

    def right(self, i, j):
        # print('rihjt')
        j1 = j
        number = ''
        while True:
            j1 = j1 - 1
            try:
                int(self.matrix[i][j1])
            except:
                break
            number += self.matrix[i][j1]
        number = int(number)
        self.action(i, j + number)

    def left(self, i, j):
        # print('left')
        j1 = j
        number = ''
        while True:
            j1 = j1 + 1
            try:
                int(self.matrix[i][j1])
            except:
                break
            number += self.matrix[i][j1]
        number = int(number)
        self.action(i, j - number)

    def par_left(self, i, j):
        j1 = j
        number = ''
        while True:
            j1 = j1 + 1
            try:
                int(self.matrix[i][j1])
            except:
                break
            number += self.matrix[i][j1]
        number = int(number)
        temp = self.stiva.pop()
        self.flag.insert(0, temp)
        self.action(i, j - number)

    def par_right(self, i, j):
        j1 = j
        number = ''
        while True:
            j1 = j1 - 1
            try:
                int(self.matrix[i][j1])
            except:
                break
            number += self.matrix[i][j1]
        number = int(number)
        temp = self.stiva.pop()
        self.flag.append(temp)
        self.action(i, j + number)

    def minus(self, i, j):
        i1 = i
        number = ''
        while True:
            i1 = i1 + 1
            try:
                int(self.matrix[i1][j])
            except:
                break
            number += self.matrix[i1][j]
        number = int(number)
        del self.flag[0]
        self.action(i - number, j)

    def plus(self, i, j):
        i1 = i
        number = ''
        while True:
            i1 = i1 - 1
            try:
                int(self.matrix[i1][j])
            except:
                break
            number += self.matrix[i1][j]
        number = int(number)
        self.flag.pop()
        self.action(i + number, j)

    def procent(self, i, j):
        self.flag = self.flag[::-1]
        self.action(i + 1, j)

    def pat_right(self, i, j):
        j1 = j - 1
        self.stiva.append(self.matrix[i][j1])
        self.action(i, j - 2)

    def pat_left(self, i, j):
        j1 = j + 1
        self.stiva.append(self.matrix[i][j1])
        self.action(i, j + 2)

    def inm(self, i, j):
        i1 = i - 1
        self.stiva.append(self.matrix[i1][j])
        self.action(i - 2, j)

    def dot(self, i, j):
        i1 = i + 1
        self.stiva.append(self.matrix[i1][j])
        self.action(i + 2, j)

    def action(self, i, j):
        c = self.matrix[i][j]
        # print(c,end='')

        if c == '>':
            self.right(i, j)
        if c == '<':
            self.left(i, j)

        if c == '^':
            self.up(i, j)

        if c == 'v':
            self.down(i, j)
        if c == '(':
            self.par_left(i, j)
        if c == ')':
            self.par_right(i, j)
        if c == '-':
            self.minus(i, j)
        if c == '+':
            self.plus(i, j)
        if c == '%':
            self.procent(i, j)
        if c == ']':
            self.pat_right(i, j)
        if c == '[':
            self.pat_left(i, j)
        if c == '*':
            self.inm(i, j)
        if c == '.':
            self.dot(i, j)
        if c == '@':
            print(*self.flag, sep='')
            # print('Stop___________________')

    def start(self, i, j):
        # print(*self.flag,sep='')
        self.k += 1
        self.flag = []
        self.stiva = []
        self.action(i + 1, j)

    def ececution(self):
        i = -1
        for line in self.matrix:
            i += 1
            for j in range(len(line)):
                if self.matrix[i][j] == '$':
                    self.start(i, j)
                    break

    def read_file(self):
        with open("labirint.txt", 'r') as file:
            while True:
                read_line = file.readline()
                if len(read_line) == 0:
                    break
                vector = []
                for read_c in read_line:
                    vector.append(read_c)
                self.matrix.append(vector[:-1])


if __name__ == '__main__':
    a = Lab()
    a.read_file()
    a.ececution()
