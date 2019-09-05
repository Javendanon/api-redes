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
        rut = request.form.get('rut')
        CompleteRut = rut.split('-')
        rutUsable = CompleteRut[0]
        if (len(rutUsable)<7):
            return {
                'ok': False,
                'msg': 'El rut ingresado '+ rut +' no es válido'
            }
        
        suma = sumaRut(rutUsable)
        dv = (11-(suma%11))
        if (dv == int(CompleteRut[1])):
            if (dv==10):
                return {
                    'ok': True,
                    'msg': 'El rut ingresado' + rut + ' es válido y tiene como digito verificador K'
                }
            if (dv==11):
                return {
                    'ok':True,
                    'msg': 'El rut ingresado '+ rut +' es válido y tiene como digito verificador 0'
                }
            else:
                return {
                    'ok':True,
                    'msg': 'El rut ingresado '+ rut +' es válido y tiene como digito verificador '+ CompleteRut[1]
                }
        return  {
            'ok': False,
            'msg': 'El rut ingresado' + rut +' es inválido o el formato está errado'
        }
def sumaRut(rut):
    suma = 0
    k=2
    rutInvertido = rut[::-1]
    for i in range(len(rut)):
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
        if gender=='M':
            gender='Sr.'
        elif gender=='F':
            gender='Sra.'
        nombreCompleto = gender + ' ' + name + ' ' + apellido_p + ' ' + apellido_m
        return {
            'ok': True,
            'msg': 'Hola '+ nombreCompleto.title()
        }

app.run()
