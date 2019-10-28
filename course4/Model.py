class Model():
    '''
    * Parameters
    dataLoader: a Dataloader class

    * Funtion
    preprocess: a function used to preprocess data read from file, it will be called after self.read()
    algorithm : main function used to implement specific algorithm
    run: a function used to run the algoithm, if pass a data, the algorithm will run on the data passed, if not it will
        read data from file you name first than run the algorithm

    '''
    def __init__(self):
        pass

    def preprocess(self):
        pass

    def read(self,dataLoader): # read data from dataLoader
        self.dataLoader = dataLoader
        self.dataLoader.read()
        self.preprocess()

    def model(self):
        pass
