class Setting():
    '''
    * Parameters
    dataLoader: a Dataloader class

    * Funtion
    preprocess: a function used to preprocess data read from file, it will be called after self.read()
    model : main function used to implement specific algorithm
    run: a function used to run the algoithm, if pass a data, the algorithm will run on the data passed, if not it will
        read data from file you name first than run the algorithm

    '''
    def __init__(self,dataLoader,model,notopt = False):
        self.inputdataloader = dataLoader
        self.inputmodel = model
        self.res = None
        self.notopt = notopt




    def run(self, data=None): # given data, use data to run algorithm, if not, load data from dataLoader first

        if data:
            self.inputdataLoader.data = data
            self.inputmodel.preprocess()
            self.res = self.model.model()


        else:
            self.inputmodel.read(self.inputdataloader)
            self.res = self.inputmodel.model()
            print(f'result:{self.res}')


        if self.notopt:
            self.inputmodel.read(self.inputdataloader)
            self.res = self.inputmodel.model_notopt()
            print(f'result:{self.res}')
