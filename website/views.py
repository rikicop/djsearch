from django.shortcuts import render
from .models import Inmueble
import pandas as pd
import json 

def home(request):
    if request.method =="POST":
        
        tipo_form = request.POST['tipof']
        ubicacion_form = request.POST['ubicacionf']
        edo_form = request.POST['edof']

        items = Inmueble.objects.all()
        df= pd.DataFrame(list(Inmueble.objects.all().values()))
        print(df)

        if (tipo_form != '') and (ubicacion_form != '') and (edo_form != ''): 
            newdf = df.loc[((df.tipo == tipo_form) & (df.ubicacion == ubicacion_form) & (df.edo == edo_form))]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 
            

        elif (tipo_form != '') and (ubicacion_form != '') and (edo_form == ''): 
            newdf = df.loc[((df.tipo == tipo_form) & (df.ubicacion == ubicacion_form))]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 

        elif (tipo_form != '') and (ubicacion_form == '') and (edo_form == ''): 
            newdf = df.loc[df.tipo == tipo_form]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 

        elif (tipo_form == '') and (ubicacion_form != '') and (edo_form == ''): 
            newdf = df.loc[df.ubicacion == ubicacion_form]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 

        elif (tipo_form == '') and (ubicacion_form != '') and (edo_form != ''):
            newdf = df.loc[((df.ubicacion == ubicacion_form) & (df.edo == edo_form))]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 

        elif (tipo_form != '') and (ubicacion_form == '') and (edo_form != ''): 
            newdf = df.loc[((df.tipo == tipo_form) & (df.edo == edo_form))]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 

        elif (tipo_form == '') and (ubicacion_form == '') and (edo_form != ''): 
            newdf = df.loc[df.edo == edo_form]
            json_records = newdf.reset_index().to_json(orient ='records')
            data = []
            #data = newdf.to_json(orient='records')
            #print(data)
            print(newdf)
            data = json.loads(json_records) 
            context = {'d': data} 
        
        #context = {'data': data} 
        #return render(request, 'home.html',{'items':items ,'tipo_form' : tipo_form, 'ubicacion_form' : ubicacion_form})
        return render(request, 'home.html', context)

    else:

        return render(request, 'home.html')
    
    return render(request, 'home.html')
