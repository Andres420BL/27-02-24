import os
participante1Str = input('Nombre del corredor 1 ')
numeroP1int = input('NUMERO DEL CORREDOR')

participante2Str = input('Nombre del corredor 2')
numeroP2int = input('Numero del corredor')
var_acumuladoP1int = 0
var_acumuladoP2int = 0
controlInt = True
while controlInt == True:

    print('<<<<<<<<<<< MENU DE OPCIONES>>>>>>>>>>>>>>>>>>>>>>>>')
    print('1.',participante1Str,'no',numeroP1int,' ',var_acumuladoP1int,'Km\n2.',participante2Str,'NO.',numeroP2int,' ',var_acumuladoP2int,'KM\n3.Finalizar')
    opcionint = int(input('\nselccione una opcion->'))
    if opcionint >= 1 and opcionint <= 2:
        var_recorridoetapaint= int(input('Ingrese los km recorridos->'))
        if opcionint == 1:
            var_acumuladoP1int += var_recorridoetapaint
        if opcionint == 2:
            var_acumuladoP2int += var_recorridoetapaint
    if opcionint == 3:
        os.system('cls')
        print('<<<<<<<<<<<<<<<< MENU DE OPCIONES >>>>>>>>>>>>>>>')
        print('Participante no.1',participante1Str,'Recorrido',var_acumuladoP1int,'KM')
        print('Participante no.2',participante2Str,'Recorrido',var_acumuladoP2int,'km')
        enter = input('\enter para continuar')
        controlInt = False
