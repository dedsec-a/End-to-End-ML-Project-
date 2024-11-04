import os
import sys
import pandas as pd
from sklearn.model_selection import  train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig :
    train_data_path = os.path.join('artifact', "train.csv")
    test_data_path = os.path.join('artifact' , "test.csv")
    raw_data_path = os.path.join('artifact', "data.csv")
   



class DataIngestion :
    def __init__(self):
        self.ingestionconfig = DataIngestionConfig()

    def initiate_data_ingestion(self):
       
       
        
        df = pd.read_csv('Notebook\data\stud.csv')
        os.makedirs(os.path.dirname(self.ingestionconfig.train_data_path), exist_ok= True)

        df.to_csv(self.ingestionconfig.raw_data_path,index= False , header= True)

       
        train_set , test_set = train_test_split(df , test_size= 0.2 , random_state= 42 )
        train_set.to_csv(self.ingestionconfig.train_data_path, index = False )
        test_set.to_csv(self.ingestionconfig.test_data_path , index = False )
       

        

        return(
                self.ingestionconfig.train_data_path,
                self.ingestionconfig.test_data_path,
                self.ingestionconfig.raw_data_path
                
            )

     



if __name__ == "__main__" :
    obj = DataIngestion()
    obj.initiate_data_ingestion()