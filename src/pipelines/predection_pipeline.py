import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredticPipeLine :
    def __init__(self):
        pass

    def predict(self , features) :
        try :
            model_path = os.path.join("artifacts" ,"model.pkl")
            preprocessor_path = os.path.join("artifacts" , "proprocessor.pkl")
            print("Before Loading")
            model = load_object(model_path)
            preprocessor = load_object(file_path= preprocessor_path)
            print("after Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e :
            raise CustomException(e ,sys)

class CustomData :
    def __init__(self ,
                 gender : str,
                 pace_ethnicity : int,
                 parental_level_of_education ,
                 lunch : str ,
                 test_prepration_course :str ,
                 reading_score : int ,
                 writing_score :int):
        self.gender = gender
        self.pace_ethnicity = pace_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_prepration_course = test_prepration_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    
 
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)















