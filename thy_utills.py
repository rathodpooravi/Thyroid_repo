import pickle
import json
import thy_config
import numpy as np
# import pandas as pd


class Thyroid():
    
    def __init__(self, Age, Gender, Smoking, HxSmoking, HxRadiothreapy, 
                 ThyroidFunction, PhysicalExamination, Adenopathy, Pathology,
                 Focality, Risk, T, N, M, Stage, Response):
        self.Age = Age
        self.Gender = Gender
        self.Smoking = Smoking
        self.HxSmoking = HxSmoking
        self.HxRadiothreapy = HxRadiothreapy
        self.ThyroidFunction = 'ThyroidFunction_' + ThyroidFunction
        self.PhysicalExamination = 'PhysicalExamination_' + PhysicalExamination
        self.Adenopathy = 'Adenopathy_' + Adenopathy
        self.Pathology = 'Pathology_' + Pathology
        self.Focality = Focality
        self.Risk = Risk
        self.T = 'T_' + T
        self.N = N
        self.M = M
        self.Stage = Stage
        self.Response = Response
    
    def load_model(self):
        with open(thy_config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)
            
        with open(thy_config.JSON_FILE_PATH, 'r') as f:
            self.project_data = json.load(f)
            
    def get_prediction(self):
        self.load_model()

        test_array = np.zeros(len(self.project_data['columns']))
        test_array[0] = self.Age
        test_array[1] = self.project_data['Gender'][self.Gender]
        test_array[2] = self.project_data['Smoking'][self.Smoking]
        test_array[3] = self.project_data['HxSmoking'][self.HxSmoking]
        test_array[4] = self.project_data['HxRadiothreapy'][self.HxRadiothreapy]
        test_array[5] = self.project_data['Focality'][self.Focality]
        test_array[6] = self.project_data['Risk'][self.Risk]
        test_array[7] = self.project_data['N'][self.N]
        test_array[8] = self.project_data['M'][self.M]
        test_array[9] = self.project_data['Stage'][self.Stage]
        test_array[10] = self.project_data['Response'][self.Response]
        ThyroidFunction_index = self.project_data['columns'].index(self.ThyroidFunction)
        test_array[ThyroidFunction_index] = 1
        PhysicalExamination_index = self.project_data['columns'].index(self.PhysicalExamination)
        test_array[PhysicalExamination_index] = 1
        Adenopathy_index = self.project_data['columns'].index(self.Adenopathy)
        test_array[Adenopathy_index] = 1
        Pathology_index = self.project_data['columns'].index(self.Pathology)
        test_array[Pathology_index] = 1
        T_index = self.project_data['columns'].index(self.T)
        test_array[T_index] = 1
        print('Test Array:', test_array)
        
        prediction = self.model.predict([test_array])[0]
        print(f'Prediction of Thyroid reccurance model: {prediction}')
        return prediction
    
    
if __name__ == '__main__':
    Age = 45
    Gender = 'M' 
    Smoking = 'Yes' 
    HxSmoking = 'Yes' 
    HxRadiothreapy = 'Yes' 
    ThyroidFunction = 'Clinical Hypothyroidism' 
    PhysicalExamination = 'Multinodular goiter' 
    Adenopathy = 'Extensive' 
    Pathology = 'Micropapillary' 
    Focality = 'Uni-Focal' 
    Risk = 'High' 
    T = 'T4a' 
    N = 'N1b' 
    M = 'M1' 
    Stage = 'III' 
    Response = 'Excellent'
    
    obj = Thyroid(Age, Gender, Smoking, HxSmoking, HxRadiothreapy, 
                  ThyroidFunction, PhysicalExamination, Adenopathy, Pathology, 
                  Focality, Risk, T, N, M, Stage, Response)
    obj.get_prediction()
    