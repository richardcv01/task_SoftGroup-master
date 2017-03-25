import os
class AOpen:
    dict_mode = {'r': os.O_RDONLY, 'w': os.O_WRONLY | os.O_CREAT, 'a': os.O_WRONLY | os.O_APPEND ,
                 'rw': os.O_RDONLY | os.O_WRONLY, 'wa': os.O_WRONLY | os.O_CREAT | os.O_APPEND,
                 }

    def __init__(self, filename, mode, encoding='utf-8'):
        self.mode = AOpen.dict_mode[mode]
        self.filename = filename
        self.filename = mode
        self.encoding = encoding
        self.Fd = os.open(filename, self.mode)
        self.st_siz = os.stat(filename).st_size
        self.pos = 0 #new line add
        self.line = 0  # new line add
        self.resSt = str(os.read(self.Fd, self.st_siz), self.encoding)


    def read(self, n=0):
        if n:
            self.n = n
        else:
            self.n = self.st_siz
        resSt = ''
        try:
            os.lseek(self.Fd, self.pos, 0)
            St = str(os.read(self.Fd, self.n), self.encoding)
            count = St.count('\n')
            #if count:
            os.lseek(self.Fd,self.pos,0)
            res = str(os.read(self.Fd, self.n+count), self.encoding)
            self.pos += n
            resSt = res
                 #new line add

        except OSError as e:
            print(e)
        res = resSt
        return res

    def readLine(self):
        self.n = self.st_siz
        ListSt = self.resSt.split('\n')
        if self.line+1 <= len(ListSt):
            res = ListSt[self.line]
            self.line += 1
            return res

    def write(self, s):
        os.write(self.Fd, bytes(s, encoding = 'utf-8'))

    def writeLine(self, s):
        s = '\n' + s
        try:
            os.write(self.Fd, bytes(s, encoding = 'utf-8'))
        except IOError as e:
            print(e)

    def close(self):
        os.close(self.Fd)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.close(self.Fd)
        return False


if __name__ == '__main__':
    file = AOpen('2.txt','r')
    #print(file.readLine())
    #print('-' * 10)
    #print(file.readLine())
    #print('-' * 10)
    #print(file.readLine())
    #print('-' * 10)
    #print(file.readLine())

    file.close()

    with AOpen('2.txt', 'r') as F:
        line = F.readLine()
        while line:
            print(line)
            line = F.readLine()




