

import collections


class DataMunger:
    
    def __init__(self):
        pass
    
    def create_random_validation_set(self, trainingData, percentSplit = 0.3):
        ''' Splits the given numpy array data into training and validation 
                (random split) 
                inputs:
                @trainingData - numpy array with data and labels
                @percentSplit - number between 1 -100 or 0 - 1 default value 0.3
                
                returns: 
                trainData - tuple (xTrain, yTrain)
                validationData - tuple (xVal, yVal)
            '''
        if percentSplit > 1:
            percentSplit = percent/100
        
        trainData = collections.namedtuple('Train', ['xTrain', 'yTrain'])
        validationData = collections.namedtuple( 'Validation', ['xVal', 'yVal'])
        
        numberOfRecords = trainingData.shape[0]
        traininingRecords = int(numberOfRecords * (1 - percentSplit))
        
        randomLines = randrange(0, numberOfRecords, trainingRecords)
        xTrain = np.zeros((trainData.shape[0] - 1, len(randomLines)))
        yTrain = np.zeros(len(randomLines))
        
        xVal = np.zeros((trainData.shape[0] - 1, numberOfRecords - len(randomLines)))
        yVal = np.zeros(len(numberOfRecords - len(randomLines)))
        
        trainIterator = 0
        valIterator = 0
        for rowNum in range(numberOfRecords):
            if rowNum in randomLines:
                xTrain[trainIterator] = trainingData[rowNum, ::trainingData.shape[1] - 1]
                yTrain[trainIterator] = trainingData[rowNum, trainingData.shape[1] - 1]
                trainIterator += 1
            else:
                xVal[valIterator] = trainingData[rowNum, ::trainingData.shape[1] - 1]
                yVal[valIterator] = trainingData[rowNum, trainingData.shape[1] - 1]
                valIterator += 1
        
        trainData.xTrain = xTrain
        traindata.yTrain = yTrain
        
        validationData.xVal = xVal
        validationData.yVal = yVal
        
        return trainData , validationData
    
    def create_validation_set(self, trainingData, percentSplit):
        ''' Splits the given numpy array data into training and validation 
                (sequential split) 
                inputs:
                @trainingData - numpy array with data and labels
                @percentSplit - number between 1 -100 or 0 - 1  
                
                returns: 
                trainData - tuple (xTrain, yTrain)
                validationData - tuple (xVal, yVal)
            '''
        if percentSplit > 1:
            percentSplit = percent/100
        
        trainData = collections.namedtuple('Train', ['xTrain', 'yTrain'])
        validationData = collections.namedtuple( 'Validation', ['xVal', 'yVal'])
        
        numberOfRecords = trainingData.shape[0]
        traininingRecords = int(numberOfRecords * (1 - percentSplit))
        
        trainData.xTrain = trainingData[::trainingRecords, ::len(trainingData) - 1]
        trainData.yTrain = trainingData[::trainingRecords, len(trainingData) - 1]
        
        validationData.xVal = trainingData[trainingRecords::, ::len(trainingData) - 1]
        validationData.yVal = trainingData[trainingRecords::, len(trainingData) - 1]
        
        
        return trainData , validationData
        
    
if __name__ == "__main__":
    pass