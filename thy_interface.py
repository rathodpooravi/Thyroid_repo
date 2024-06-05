from flask import Flask, jsonify, request, render_template
import thy_config
from thy_utills import Thyroid

app = Flask(__name__)


@app.route('/')
def thyroid_model():
    print('Welcome to the thyroid recurance model')
    return render_template('index.html')

@app.route('/predict_prediction', methods=['POST'])
def Thy_prediction():
    # if request.method == 'POST':
        print('We are in POST Method')
        data = request.form       
        Age = int(data['Age'])
        Gender = data['Gender']
        Smoking = data['Smoking']
        HxSmoking = data['HxSmoking']
        HxRadiothreapy = data['HxRadiothreapy']
        ThyroidFunction = data['ThyroidFunction']
        PhysicalExamination = data['PhysicalExamination']
        Adenopathy = data['Adenopathy']
        Pathology = data['Pathology']
        Focality = data['Focality']
        Risk = data['Risk']
        T = data['T']
        M = data['M']
        N = data['N']
        Stage = data['Stage']
        Response = data['Response']
        thy_pr=Thyroid(Age, Gender, Smoking, HxSmoking, HxRadiothreapy, 
                   ThyroidFunction, PhysicalExamination, Adenopathy, Pathology, 
                   Focality, Risk, T, N, M, Stage, Response)
        predict = thy_pr.get_prediction()
    
        if predict == 'Yes':
    
            return jsonify({'Result': f'Prediction {predict} Thyroid will not be reccured '})
        else:
            return jsonify({'Result': f'Prediction is:{predict} Thyroid will be  reccured'})
    
# else:
#         print('We are in Get Method')
#         data1 = request.args       
#         Age = data1.get('Age') 
#         Gender = data1.get('Gender')
#         Smoking = data1.get('Smoking')
#         HxSmoking = data1.get('HxSmoking')
#         HxRadiothreapy = data1.get('HxRadiothreapy')
#         ThyroidFunction = data1.get('ThyroidFunction')
#         PhysicalExamination = data1.get('PhysicalExamination')
#         Adenopathy = data1.get('Adenopathy')
#         Pathology = data1.get('Pathology')
#         Focality = data1.get('Focality')
#         Risk = data1.get('Risk')
#         T = data1.get('T')
#         M = data1.get('M')
#         N = data1.get('N')
#         Stage = data1.get('Stage')
#         Response = data1.get('Response')
        
            
    
#     thy_pr1=Thyroid(Age, Gender, Smoking, HxSmoking, HxRadiothreapy, 
#                    ThyroidFunction, PhysicalExamination, Adenopathy, Pathology, 
#                    Focality, Risk, T, N, M, Stage, Response)
#     predict1 = thy_pr1.get_prediction()
    
#     if predict1 == 'Yes':
    
#         return jsonify({'Result': f'Prediction {predict1} Thyroid will not be reccured '})
#     else:
#         return jsonify({'Result': f'Prediction is:{predict1} Thyroid will be  reccured'})
    

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = thy_config.PORT_NUMBER,debug=True)