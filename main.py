from flask import (
    Flask,
    request,
    jsonify
)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/verificaRut',methods=['POST'])
def digitoVerificador():

    if (request.method=='POST'):
        ValueDv = False    # verificación 
        if ('rut' not in request.form):
            return {
                'ok': False,
                'msg': 'Error de ingreso de datos'
            }
        
        rut = request.form.get('rut') 
        CompleteRut = rut.split('-')  
        rutUsable = CompleteRut[0]
        if (len(rutUsable)<7):
            return {
                'ok': False,
                'msg': 'El rut ingresado '+ rut +' no es valido'
            }
        suma = sumaRut(rutUsable)
        if (suma==0):
            return {
                'ok':False,
                'msg': 'El rut ingresado ' + rut + ' es invalido o el formato esta errado'
            }
        dv = (11-(suma%11))
        if (CompleteRut[1] in (0,1,2,3,4,5,6,7,8,9,'1','2','3','4','5','6','7','8','9','K','k','0')):
            ValueDv = True
        if (CompleteRut[1]=='K' or CompleteRut[1]=='k'):
                CompleteRut[1]=10
        elif (CompleteRut[1]=='0' or CompleteRut[1]==0):
                CompleteRut[1]=11
        if (ValueDv == True):
            if (dv == int(CompleteRut[1])):
                if (dv==10):
                    return {
                        'ok': True,
                        'msg': 'El rut ingresado ' + rut + ' es valido y tiene como digito verificador K'
                    }
                elif (dv==11):
                    return {
                        'ok':True,
                        'msg': 'El rut ingresado '+ rut +' es valido y tiene como digito verificador 0'
                    }
                else:
                    return {
                        'ok':True,
                        'msg': 'El rut ingresado '+ rut +' es valido y tiene como digito verificador '+ CompleteRut[1]
                }
        else:
            return {
                'ok': False,
                'msg': 'El rut ingresado ' + rut + ' es invalido o el formato esta errado'
            }
        return  {
            'ok': False,
            'msg': 'El rut ingresado ' + rut +' es invalido o el formato esta errado',
        }
def sumaRut(rut):
    suma = 0
    k=2
    rutInvertido = rut[::-1]
    for i in range(len(rut)):
        if rutInvertido[i] not in (0,1,2,3,4,5,6,7,8,9,'1','2','3','4','5','6','7','8','9','0'):
            suma=0
            return suma
        if (i<6):
            suma = suma + int(rutInvertido[i])*k
            k+=1
        elif (i==6):
            k=2
            suma += int(rutInvertido[i])*k
        else:
            k+=1
            suma += int(rutInvertido[i])*k
    return suma

@app.route('/nombrePropio',methods=['POST'])
def nombrePropio():
    if request.method=='POST':
        name = request.form.get('name')
        apellido_m = request.form.get('apellido_m')
        apellido_p = request.form.get('apellido_p')
        gender = request.form.get('gender')
        if (gender not in ('M','m','F','f')):
            return {
                'ok': False,
                'msg': 'El genero no coincide con lo permitido, ingrese (M,F,m,f)'
            }
        if gender=='M' or gender=='m':
            gender='Sr.'
        elif gender=='F' or gender=='f':
            gender='Sra.'
        nombreCompleto = gender + ' ' + name + ' ' + apellido_p + ' ' + apellido_m
        return {
            'ok': True,
            'msg': 'Hola '+ nombreCompleto.title()
        }

app.run()
