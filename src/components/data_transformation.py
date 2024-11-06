import sys
from dataclasses import dataclass

import pandas as pd
import numpy as np 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder , StandardScaler
import os 

from src.utils import save_object



@dataclass 
class Datatransformationconfig:
    preprocessor_obj_file = os.path.join('artifacts' ,'preprocessing.pkl')


class Datatransformation :
    def __init__(self):
        self.data_transformation_config = Datatransformationconfig()

    def get_data_transformer_object(self):
        '''
        This function si responsible for data trnasformation
        
        '''
       
        numerical_columns = ["writing_score", "reading_score"]
        categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

        num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

        cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )

           

        preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]


            )

        return preprocessor




def initaie_data_transformation(self , train_path , test_path ):
        
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path) 
        # loaded the the Traning and testing Data into the Function 



        prerpocessing_obj = self.get_data_transformer_obj() # called the Object that will do the preprocessing on the data 

        target_column_name = "math_score" # created the target Column that is supoosed to pe pridicted 
        numerical_column = ["writing_score" , "reading_score"] #  Seperated the numerial coulns 

        input_featue_train_df = train_df.drop(columns= [target_column_name], axis= 1) # seperated the predectied feature just like X_train 
        target_feature_train_df = train_df[target_column_name] # got the True Values in here just like y_train 

        input_featue_test_df = test_df.drop(columns= [target_column_name], axis= 1) # seperated the test Output Feature just like X_test 
    
        target_feature_test_df = test_df[target_column_name] # seperatesd the true value just like y_test 


        input_feature_train_arr = prerpocessing_obj.fit_transform(input_featue_train_df) # now processing the data as we do for  X_train 
        input_feature_test_arr = prerpocessing_obj.transform(input_featue_test_df) # same as we for X_test data 


        # we are now concatinating the Array after doing the Scaling and transforming the Data
        train_arr = np.c_[
            input_feature_test_arr , np.array(target_feature_train_df)
        ]

        test_arr = np.c_[
            input_featue_test_df , np.array(target_feature_test_df)
        ]

        save_object(
            file_path= self.data_transformation_config.preprocessor_obj_file,
            obj= prerpocessing_obj
        )

        return(
            train_arr,
            test_arr,
            self.data_transformation_config.preprocessor_obj_file

        )



   
      

    