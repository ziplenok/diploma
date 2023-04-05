#import torch
from flask import Flask, request, Response, jsonify, send_from_directory, abort
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def hello_world():
    # create an empty dataframe with columns 'A', 'B', 'C'
    df = pd.DataFrame(columns=['Points', 'Univer_code', 'Status', 'суммабалловсертификата', 'преимущественноеправо', 
                           'среднийбаллаттестата(диплома)',
                          'суммабалловпрофильныхпредметов(творческихэкзаменов)', '2020-2021_Max', '2020-2021_Min', 
                           '2021-2022_Max',
                          '2021-2022_Min', 'difference_Max', 'difference_Min', 'profile subject_1', 'profile subject_2',
                          'Count_difference_per_year'])
    
    status = request.form["status"]
    preimushestvo = request.form["preimushestvo"]
    profile_subj_1 = request.form["profile_subj_1"]
    profile_subj_2 = request.form["profile_subj_2"]
    Points = request.form["Points"]
    Univer_code = request.form["Univer_code"]
    certificate_point = request.form["суммабалловсертификата"]
    average_from_attistat = request.form["среднийбаллаттестата(диплома)"]
    profile_total = request.form["суммабалловпрофильныхпредметов(творческихэкзаменов)"]

    print('status type', type(status))

    print('certificate_point type', type(certificate_point))

    print('average_from_attistat type', type(average_from_attistat))

    # status = 'City'
    # preimushestvo = 'непс'
    # profile_subj_1 = 'Биология'
    # profile_subj_2 = 'География'

    with open('le_status.pkl', 'rb') as f:
        le_status = pickle.load(f)

    with open('le_preimushestvo.pkl', 'rb') as f:
        le_preimushestvo = pickle.load(f)

    with open('le_subj.pkl', 'rb') as f:
        le_subj = pickle.load(f)

    df_s = pd.DataFrame({'Status': [status]})
    encoded_row = le_status.transform(df_s.iloc[0])
    status = int(encoded_row)
    print(status)

    df_s = pd.DataFrame({'преимущественноеправо': [preimushestvo]})
    encoded_row = le_preimushestvo.transform(df_s.iloc[0])
    preimushestvo = int(encoded_row)
    print(preimushestvo)

    df_s = pd.DataFrame({'profile subject_1': [profile_subj_1]})
    encoded_row = le_subj.transform(df_s.iloc[0])
    profile_subj_1 = int(encoded_row)
    print(profile_subj_1)

    df_s = pd.DataFrame({'profile subject_2': [profile_subj_2]})
    encoded_row = le_subj.transform(df_s.iloc[0])
    profile_subj_2 = int(encoded_row)
    print(profile_subj_2)



    Points = int(Points)
    Univer_code = int(Univer_code)
    certificate_point = int(certificate_point)  #request.form["суммабалловсертификата"]
    average_from_attistat = float(average_from_attistat)    #request.form["среднийбаллаттестата(диплома)"]
    profile_total = int(profile_total)  #request.form["суммабалловпрофильныхпредметов(творческихэкзаменов)"]
    

    new_row = pd.Series({'Points': Points, 'Univer_code': Univer_code, 'Status': status, 'суммабалловсертификата' : certificate_point, 
                     'преимущественноеправо' : preimushestvo,
                    'среднийбаллаттестата(диплома)' : average_from_attistat, 'суммабалловпрофильныхпредметов(творческихэкзаменов)' : profile_total,
                    '2020-2021_Max' : 131.0, '2020-2021_Min' : 97.0, '2021-2022_Max' : 138.0, '2021-2022_Min' : 97.0, 
                     'difference_Max' : 7.0, 'difference_Min' : 0.0, 'profile subject_1' : profile_subj_1, 
                     'profile subject_2' : profile_subj_2, 
                     'Count_difference_per_year' : 70.0})

    # add the new row to the dataframe
    df = df.append(new_row, ignore_index=True)

    x_pred = df.values

    with open('nb.pkl', 'rb') as f:
        nb = pickle.load(f)

    y_pred = nb.predict(x_pred)

    with open('le_spec.pkl', 'rb') as f:
        le_spec = pickle.load(f)

    decoded_row = le_spec.inverse_transform(y_pred)

    print(type(decoded_row))
    str_decoded = str(decoded_row)

    # image_in_base64 = request.form["image"]

    #print(f'Cuda gpu is available {torch.cuda.is_available()}')
    #return 'Flask Dockerized Cuda gpu is available mb'# + str(torch.cuda.is_available())

    print('Debugger mode is on babe')

    return jsonify({"spec": str_decoded})




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')