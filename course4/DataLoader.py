import os

class DataLoader():
    '''
    processLine: a function used to process each line read from file
    numLines: how many lines you want to read from file
    '''
    def __init__(self, fileName, numLines = None, processLine=lambda x:x):
    # def __init__(self):

        CD = os.getcwd()
        self.data = None
        self.numLines = numLines
        self.file = os.path.join(CD,fileName)
        self.processLine = processLine

    def read(self):
        print('Loading data ...')
        out = []
        with open(self.file, 'r') as f:
            lines = f.readlines()
            for num,line in enumerate(lines):
                line = self.processLine(line)
                out.append(line)
                if self.numLines:
                    if num == self.numLines-1:
                        break
        self.data = out
        print(f'Total {len(out)} lines read')
        print('-'*50)
