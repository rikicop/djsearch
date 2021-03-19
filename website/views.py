from django.shortcuts import render
from .models import Inmueble
import pandas as pd

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
            print(newdf)

        elif (tipo_form != '') and (ubicacion_form != '') and (edo_form == ''): 
            newdf = df.loc[((df.tipo == tipo_form) & (df.ubicacion == ubicacion_form))]
            print(newdf)

        elif (tipo_form != '') and (ubicacion_form == '') and (edo_form == ''): 
            newdf = df.loc[df.tipo == tipo_form]
            print(newdf)

        elif (tipo_form == '') and (ubicacion_form != '') and (edo_form == ''): 
            newdf = df.loc[df.ubicacion == ubicacion_form]
            print(newdf)

        elif (tipo_form == '') and (ubicacion_form != '') and (edo_form != ''):
            newdf = df.loc[((df.ubicacion == ubicacion_form) & (df.edo == edo_form))]
            print(newdf)

        elif (tipo_form != '') and (ubicacion_form == '') and (edo_form != ''): 
            newdf = df.loc[((df.tipo == tipo_form) & (df.edo == edo_form))]
            print(newdf)

        elif (tipo_form == '') and (ubicacion_form == '') and (edo_form != ''): 
            newdf = df.loc[df.edo == edo_form]
            print(newdf)
        

        return render(request, 'home.html',{'items':items ,'tipo_form' : tipo_form, 
        'ubicacion_form' : ubicacion_form})
    else:
        return render(request, 'home.html')
    
    return render(request, 'home.html')
