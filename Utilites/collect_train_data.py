import pandas as pd

def data_inot_csv(traindata):
        df=pd.DataFrame(traindata)
        df.to_csv('TrainData.csv')