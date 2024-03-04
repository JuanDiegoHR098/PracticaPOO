#ESTE PROGRAMA SE HIZO DESDE CERO

from datetime import datetime

# Se cre la clase mascota 
class Mascota:
    #Se crea el constructo de cla clase
    def __init__(self) -> None:
        self.__nombre= ""
        self.__num_historia= int
        self.__tipo= ""
        self.__peso=""
        self.__fecha_ingreso= ""
        self.__medicamento= ""


    # Se crean los getters para acceder a la informacion privada
    def ver_nombre(self):
        return self.__nombre
    
    def ver_tipo(self):
        return self.__tipo
    
    def ver_peso(self):
        return self.__peso
    
    def ver_num_historia(self):
        return self.__num_historia
    
    def ver_fecha_ingreso(self):
        return self.__fecha_ingreso
    
    def ver_medicamento(self):
        return self.__medicamento
    
    # Se crean los setter para asignar la informacion  
    def asignar_nombre(self,nombre):
        self.__nombre= nombre

    def asignar_tipo(self,tipo):
        self.__tipo= tipo

    def asignar_peso(self,peso):
        self.__peso= peso
    
    def asignar_num_historia(self,num):
        self.__num_historia= num

    def asignar_fecha_ingreso(self,ingreso):
        self.__fecha_ingreso= ingreso

    def asignar_medicamento(self,medicamento):
        self.__medicamento= medicamento

#Se crea la clase sistema con sus respectivas funciones para poder utilizar la informacion de la clase paciente
class Sistema:
    #Se crea el constructor de la clase sistema con las listas para almacenar los objetos tipo mascotas y los objetos tipo medicamentos
    def __init__(self) -> None:
        self.lista_mascotas= []
        self.lista_medicamentos=[]

    #Se itera sobre la lista de mascotas y para obtener un objeto tipo mascota y utilizar sus metodos para conseguir nombre
    def conseguir_nombre(self,num):
        for i in self.lista_mascotas:
            if num == i.ver_num_historia():
                return i.ver_nombre()
    
    #Se itera sobre la lista de mascotas y para obtener un objeto tipo mascota y utilizar sus metodos para conseguir el numero de historia para saber si existe
    def Verificar_existente(self,num):
        for mascota in self.lista_mascotas:
            if num ==  mascota.ver_num_historia():
                return True
            else:
                return False


    #Funcion para guardar un objeto tipo mascora en lista de mascotas
    def ingresar_mascota(self,mascota):
        self.lista_mascotas.append(mascota)

    #Se itera sobre la lista de mascotas y para obtener un objeto tipo mascota y utilizar sus metodos para conseguir la fecha de ingreso
    def ver_fecha_ingreso(self,nombre):
        for mascota in self.lista_mascotas:
            if nombre == mascota.ver_nombre() :
                return mascota.ver_fecha_ingreso()
        return None
    
    #Se utiliza la funcion len() para conocer la longitud de la lista de mascotas
    def ver_num_mascotas(self):
        return len(self.lista_mascotas)

    #Se itera sobre la lista de mascotas y para obtener un objeto tipo mascota y utilizar sus metodos para conseguir el medicamento que esta usando una mascota en especico
    def ver_medicamento(self,codigo):
        for mascota in self.lista_mascotas:
            if codigo == mascota.ver_num_historia():
                return mascota.ver_medicamento()
            
            
        
    #Se itera sobre la lista de mascotas y se filtra por numero de de registro para identificar a la mascota y luego se utilizar la funcion remove() para eliminarla de la lista
    def eliminar_mascota(self,mascota_eliminar):
        for mascota in self.lista_mascotas:
            if mascota_eliminar == mascota.ver_num_historia():
                self.lista_mascotas.remove(mascota)

#Se crea la clase medicamento
class Medicamento:
    #Se crean los constructores la clase medicamento
    def __init__(self) -> None:
        self.__nombre= ""
        self.__dosis= 0

    #Se crean los getters para ver la informacion privada 
    def verNombre_Medicamento(self):
        return self.__nombre
    
    def VerDosis_Medicamento(self):
        return self.__dosis
    
    #Se crean los setter para asignar la informacion
    def asignar_medicamento(self,medicamento):
        self.__nombre= medicamento

    def asignar_dosis(self,medicamento):
        self.__dosis= medicamento

# Intenta convertir la fecha a un objeto datetime
def validar_fecha(fecha):
    try:
        
        fecha_obj = datetime.strptime(fecha, '%d/%m/%Y')
        return True
    except ValueError:
        print("Fecha inválida. Por favor, ingrese la fecha en formato dd/mm/aaaa.")
        return False

#Se crea el objeto tipo sistema para utilizar sus metodos en el menu principal
sis= Sistema()

#Menu principal
while True:
    try:
        print("Menu:")
        print("-"*30)
        print("¿Que desea hacer?\n1. Ingresar Mascota\n2. Ver fecha de ingreso\n3.Ver numero de mascotas registradas\n4.Ver medicamento suministrado(Filtrado por # de historia clinica)\n5.Eliminar mascota\n6.Salir")
        print("-"*30)

        entrada = int(input("Ingrese una opcion:"))
        # Si se ingresa a la opcion 1 ingresara una mascota y validara que no se ingresen mas de 10 mascotas, ademas validara los datos numericos para que no saque errores y no saldra del ciclo hasta que se ingrese un numero
        if entrada==1:

            try:

                if len(sis.lista_mascotas) < 10:
                    
                    while True:
                        try:
                            num_historia = int(input("Ingrese el numero de historia: "))
                            break  
                        except ValueError:
                            print("Error: Por favor, ingrese solo números.")
                    f= sis.Verificar_existente(num_historia)
                    if f == True:
                        print("¡Ya existe una mascota registrada con ese numero de historia!")
                    else:
                        
                    
                        nombre= input("Ingrese el nombre de la mascota:") 
                        tipo=input("Que tipo de mascota es (Canino/Felino):")
                        while True:
                            try:
                                peso = int(input("Ingrese el peso de la mascota: "))
                                break  
                            except ValueError:
                                print("Error: Por favor, ingrese solo números.")
                        
                        while True:
                            fecha_ingreso = input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")
                            if validar_fecha(fecha_ingreso):
                                break
                        
                        medicamento= int(input("Cantidad de medicamentos suministrados:"))
                        lista_medicamentos= []

                        for i in range(0,medicamento):
                            med= Medicamento()
                            nom_medicamento= input("Ingrese el nombre del medicamento:")
                            dosis= int(input("Ingrese la dosis del medicamento:"))
                            med.asignar_medicamento(nom_medicamento)
                            med.asignar_dosis(dosis)
                            lista_medicamentos.append(med)



                        mascota= Mascota()
                        mascota.asignar_nombre(nombre)
                        mascota.asignar_num_historia(num_historia)
                        mascota.asignar_tipo(tipo)
                        mascota.asignar_peso(peso)
                        mascota.asignar_fecha_ingreso(fecha_ingreso)
                        mascota.asignar_medicamento(lista_medicamentos)
                        sis.ingresar_mascota(mascota)
                    
                else:
                    print("¡Capacidad de mascotas registradas excedida, solo se permiten 10 mascotas")
            except ValueError:
                print("Ingrese un valor valido")

        #Se utilizan los metodos de sistema para interar en la lista mascota y buscar el nombre y conseguir la fecha de ingreso asociada
        if entrada==2:
            nombre= input("Ingrese el nombre de la mascota:")
            busqueda= sis.ver_fecha_ingreso(nombre)
            print(f"La fecha de ingreso de la mascota {nombre} es : {busqueda}")

        #Se utiliza los metodos de la clase sistema para conseguir la longitud de la lista de mascotas
        if entrada ==3:
            print(f"el numero de mascotas ingresadas es :{sis.ver_num_mascotas()}")

        #Se utiliza el numero de historia para buscar en la lista de mascotas y buscar la mascota asociada y asi poder buscar los medicamentos asociados a la mascota
        if entrada==4:
            codigo= int(input("Ingrese el # de historia clinica de la mascota:"))
            f= sis.Verificar_existente(codigo)
            if f == False:
                    print("¡Mascota no existente!")
            else:
                nom= sis.conseguir_nombre(codigo)
                verificar= sis.ver_medicamento(codigo)
                for i in verificar:
                    print(f"Medicamento: {i.verNombre_Medicamento()} - Dosis:{i.VerDosis_Medicamento()} ")
                
                
        #Se filtra por numero de historia para encontrar a la mascota asociada y asi poder eliminarla con los metodos de Sistema
        if entrada== 5:
            entrada1=int(input("Ingresa el # de historia del paciente:"))
            f= sis.Verificar_existente(entrada1)
            if f == False:
                print("La historia clinica no existe")
            else:
                print(f"¡La mascota {sis.conseguir_nombre(entrada1)} fue eliminada con exito!")
                masc_eliminar= sis.eliminar_mascota(entrada1)
                
        #Esta seccion me permite finalizar el programa
        if entrada== 6:
            
                try:
                    validar=input("¿Esta seguro que desea salir Y/N: ").lower()
                    if validar == "y":
                        print("Saliendo...")
                        break
                    elif validar == "n":
                        continue
                    else:
                        print("Ingrese un valor valido")
                except ValueError:
                    print("Ingrese un valor valido")

            
    except ValueError:
        print("Ingrese un valor valido.")