from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
import pandas as pd
import numpy as np
import pickle
#import sklearn
#from sklearn.linear_model import LogisticRegression

# Create your views here.
def home(request):

    if request.method == 'POST':
        Zipcode = request.POST['Zipcode']
        Temperature = request.POST['Temperature']
        Weekday = request.POST['Weekday']
        Month = request.POST['Month']
        Hour = request.POST['Hour']
        Latitude = request.POST['Latitude']
        Longitude = request.POST['Longitude']
        Humidity = request.POST['Humidity']
        Crossings = request.POST['Crossings']
        Weather_Condition = request.POST['Weather_Condition']


        if Zipcode != "":
            
            # Create an empty DataFrame with specified columns
            columns = ['Zipcode','Temperature','Weekday','Month','Hour','Latitude',
                                    'Longitude','Humidity','Crossings','Weather_condition']
            df = pd.DataFrame(columns=columns)

            # Data for the new row
            # 
            new_row = {'Zipcode': int(Zipcode),
                'Temperature': float(Temperature),
                'Weekday': int(Weekday),
                'Month': int(Month),
                'Hour': int(Hour),
                'Latitude': float(Latitude),
                'Longitude': float(Longitude),
                'Humidity': float(Humidity),
                'Crossings': int(Crossings),
                'Weather_condition': int(Weather_Condition)}

            # Append the data from df2 to the DataFrame df
            new_df = pd.DataFrame([new_row])

            # Concatenate the new DataFrame with the original DataFrame
            df = pd.concat([df, new_df], ignore_index=True)



            path_of_file = "AccidentSeverity.pkl"
            rf_model_load = pickle.load(open(path_of_file,'rb'))
            pred_severity = rf_model_load.predict(df)
            
            if int(pred_severity)== 1: 
                prediction ='Least Severe'
            elif int(pred_severity)== 2: 
                prediction ='Moderate Severe'
            elif int(pred_severity)== 3: 
                prediction ='Severe'
            elif int(pred_severity)== 4: 
                prediction ='Extreamely Severe'
            else:
                prediction = 'Data Is Inaccurate'     

        else:
            return redirect('SevirityPrediction.html')
    
    else:
        return render(request,'SevirityPrediction.html')
    
    return render(request,'SevirityPrediction.html',{'result':prediction,"severity":pred_severity})        



    
def about(request):
    return render(request,'about.html')