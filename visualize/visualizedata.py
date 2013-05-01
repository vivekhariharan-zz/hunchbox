
from pylab import bar

class VisualizeData:
    
    
    def __init__(self):
        pass
    
    
    def visualize_class_labels(self, trainData, labelCol):
        labels = trainData[:, labelCol]
        labelCounts = {}
        for label in labels:
            if labelCounts.has_key(label):
                labelCounts[label] += 1
            else:
                labelCounts[label] = 1
        
        labelKeys = labelCounts.keys()
        labelValues = [v for k, v in labelCounts]
        bar(labelKeys, labelValues, facecolor='#9999ff', edgecolor = 'white')
        ylim(min(labelValues) - 10, max(labelValues) + 10)
        show()
        
        
    def visualize_value_labels(self, trainData, labelCol):
        pass
        
        
if __name__ == '__main__':
    pass
        