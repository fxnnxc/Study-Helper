import random

class ProblemGenerator():
    """
    Read the Text and read the file...
    If there is no such a file, read the test file.

    """
    def __init__(self):
        self.readfile()
        self._file = None
        self._lines = None

    def readfile(self):
        try:
            W = open(self._file, 'r')
        except:
            self._file = "test.txt"
            W = open("test.txt",'r')

        self._lines = W.readlines()
        W.close()

    def study(self,k):
        print(f"전체 갯수는 : {len(self._lines)}\n")
        try:
            for i in range(k):
                T = random.choice(self._lines)
                print(T[0], '----------------------------------------------', T[2:])
        except:
            print("!FINISHED!")

    def remove(self,L,W):
        for i in L:
            if W in i:
                L.remove(i)
                print(f"Remove {i[0]}")
                break

    def makeTest(self):
        W_copy = self._lines.copy()
        while len(W_copy)>0:
            random.shuffle(W_copy)
            T = W_copy.pop()
            A = [T[2:-1]]
            random.shuffle(self._lines)
            L_copy = self._lines.copy()
            A = A + [L_copy.pop()[2:-1] for i in range(4)]
            random.shuffle(A)
            A.insert(0,T[0])
            A.insert(1,T[2:-1])
            yield A

    def text_to_list(self):
        return self.L.copy()