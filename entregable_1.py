################################################ MARCAPASOS  #######################################
class Marcapasos:
    def __init__(self) -> None:
        self.__nombre= ""
        self.__num_electrodos=0
        self.__almbrico_o_inalambrico=""
        self.__frecuencia_estimulacion=0.0

    #Getters
    def ver_nombre(self):
        return self.__nombre
    
    def ver_num_electrodos(self):
        return self.__num_electrodos
    
    def ver_almbrico_o_inalambrico(self):
        return self.__almbrico_o_inalambrico
    
    def ver_frecuencia_estimulacion(self):
        return self.__frecuencia_estimulacion
    
    #Setters

    def asignar_nombre(self,nombre):
        self.__nombre = nombre 

    def asignar_num_electrodos(self,num_electrodos):
        self.__num_electrodos = num_electrodos  

    def asignar_almbrico_o_inalambrico(self,almbrico_o_inalambrico):
        self.__almbrico_o_inalambrico = almbrico_o_inalambrico
    
    def asignar__frecuencia_estimulacion(self,frecuencia_estimulacion):
        self.__frecuencia_estimulacion = frecuencia_estimulacion


################################################ STENT CORONARIO  #######################################
class Stent_coronario:
    def __init__(self) -> None:
        self.__nombre= ""
        self.__longitud=0.0
        self.__diametro=0.0
        self.__material=""

        #Getters
    def ver_nombre(self):
        return self.__nombre
    
    def ver_longitud(self):
        return self.__longitud
    
    def ver_diametro(self):
        return self.__diametro
    
    def ver_material(self):
        return self.__material
    
    #Setters
    def asignar_nombre(self,nombre):
        self.__nombre = nombre 

    def asignar_longitud(self,longitud):
        self.__num_electrodos = longitud  

    def asignar_material(self,material):
        self.__material = material
    
    def asignar_diametro(self,diametro):
        self.__diametro = diametro

################################################ IMPLANTE DENTAL  #######################################
class Implante_dental:
    def __init__(self) -> None:
        self.__nombre= ""
        self.__forma=""
        self.__sis_fijacion=""
        self.__material=""

        #Getters
    def ver_nombre(self):
        return self.__nombre
    
    def ver_num_electrodos(self):
        return self.__num_electrodos
    
    def ver_almbrico_o_inalambrico(self):
        return self.__almbrico_o_inalambrico
    
    def ver_frecuencia_estimulacion(self):
        return self.__frecuencia_estimulacion
    
    #Setters

    def asignar_nombre(self,nombre):
        self.__nombre = nombre 

    def asignar_num_electrodos(self,num_electrodos):
        self.__num_electrodos = num_electrodos  

    def asignar_almbrico_o_inalambrico(self,almbrico_o_inalambrico):
        self.__almbrico_o_inalambrico = almbrico_o_inalambrico
    
    def asignar_num_electrodos(self,frecuencia_estimulacion):
        self.__frecuencia_estimulacion = frecuencia_estimulacion
        
################################################ IMPLANTE RODILLA  #######################################

class Implante_rodilla:
    def __init__(self) -> None:
        self.__nombre= ""
        self.__material=""
        self.__tipo_fijacion = ""
        self.__tamaño = 0.0

    #Getters
        
    def ver_nombre(self):
        return self.__nombre
    
    def ver_material(self):
        return self.__material
    
    def ver_material(self):
        return self.__tipo_fijacion
    
    def ver_material(self):
        return self.__tamaño
    
    #Setters
    def asignar_nombre(self,nombre):
        self.__nombre = nombre 

    def asignar_material(self,material):
        self.__material= material

    def asignar_tipo_fijacion(self,tipo_fijacion):
        self.__tipo_fijacion= tipo_fijacion

    def asignar_tamaño(self,tamaño):
        self.__tamaño= tamaño


################################################ IMPLANTE CADERA  #######################################

class Implante_cadera(Implante_rodilla):
    def __init__(self) -> None:
        super().__init__()

################################################ PACIENTES  #######################################
class Pacientes:
    def __init__(self) -> None:
        self.__nombre= ""
        self.__cedula=0
        self.__edad= 0
        self.__implante=""


    #Getters
    def ver_nombre(self):
        return self.__nombre
    
    def ver_cedula(self):
        return self.__cedula
    
    def ver_edad(self):
        return self.__edad
    
    def ver_implante(self):
        return self.__implante
    
    
    #Setters
    def asignar_nombre(self,nombre):
        self.__nombre= nombre

    def asignar_cedula(self,cedula):
        self.__nombre= cedula

    def asignar_edad(self,edad):
        self.__nombre= edad

    def asignar_implante(self,implante):
        self.__nombre= implante


################################################ SISTEMA  #######################################
class Sistema:
    def __init__(self) -> None:
        self.__lista_marcapasos=[]
        self.__lista_stent_cornonario=[]
        self.__lista_implante_dental=[]
        self.__lista_imp_rodilla=[]
        self.__lista_imp_cadera=[]

    def ingresar_Marcapasos(self,protesis):
        self.__lista_marcapasos.append(protesis)

    def ingresar_stent_coronario(self,stent):
        self.__lista_stent_cornonario.append(stent)

    def ingresar_implante_dental(self,imp_dental):
        self.__lista_implante_dental.append(imp_dental)

    def ingresar_implante_rodilla(self,imp_rodilla):
        self.__lista_imp_rodilla.append(imp_rodilla)

    def ingresar_implante_cadera(self,imp_cadera):
        self.__lista_imp_cadera.append(imp_cadera)

sistema= Sistema()
def main():
    print("-"*30)
    print("Bienvenido al sistema de gestion de inventarios de protesis")
    print("-"*30)

    while True:
        try:
            #MENU
            print("¿Que desa hacer?\n")
            print("1.Agregar nuevo implante\n2.Eliminar \n3.Editar\n4.Visualizar")
            inicio=int(input("Ingrese una opcion:"))

            #################################### AGREGAR NUEVA PROTESIS ###############################################

            if inicio ==1:
                print("-"*30)
                print("¿Que tipo de protesis desea agregar?")
                print("-"*30)
                print("1.Marcapasos\n2.Stent cornonario\n3.Implante dental\n4.Implante de rodilla\n5.Implante de cadera\n")
                entrada= int(input("Ingrese una opcion:"))
                if entrada ==1:
                    nombre= input("Nombre de la protesis:")
                    num_electrodos= int(input("Numero de electrodos:"))
                    alambric_inalambric= input("Alambrico o inalambrico:")
                    frec_estimu= float(input("Frecuencia de estimulacion:"))

                    marcapasos= Marcapasos()
                    marcapasos.asignar_nombre(nombre)
                    marcapasos.asignar_num_electrodos(num_electrodos)
                    marcapasos.asignar_almbrico_o_inalambrico(alambric_inalambric)
                    marcapasos.asignar__frecuencia_estimulacion(frec_estimu)

                    sistema.ingresar_protesis(marcapasos)
                    print("¡Registro Exitoso¡")
                
                #INGRESAR STENT CORONARIO
                elif entrada==2:
                    nombre= input("Nombre de la protesis:")
                    longitud= float(input("Longitd:"))
                    diametro= float(input("Diametro:"))
                    material= (input("Material:"))

                    stent= Stent_coronario()
                    stent.asignar_nombre(nombre)
                    stent.asignar_longitud(longitud)
                    stent.asignar_diametro(diametro)
                    stent.asignar__material(material)

                    sistema.ingresar_stent_coronario(stent)
                    print("¡Registro Exitoso¡")

                #IMPLANTE DENTAL
                elif entrada==3:
                    nombre= input("Nombre de la protesis:")
                    num_electrodos= int(input("Numero de electrodos:"))
                    alambric_inalambric= input("Alambrico o inalambrico:")
                    frec_estimu= float(input("Frecuencia de estimulacion:"))

                    marcapasos= Marcapasos()

                    marcapasos.asignar_num_electrodos(num_electrodos)
                    marcapasos.asignar_almbrico_o_inalambrico(alambric_inalambric)
                    marcapasos.asignar__frecuencia_estimulacion(frec_estimu)

                    sistema.ingresar_protesis(marcapasos)
                    print("¡Registro Exitoso¡")
                
                elif entrada==4:
                    nombre= input("Nombre de la protesis:")
                    num_electrodos= int(input("Numero de electrodos:"))
                    alambric_inalambric= input("Alambrico o inalambrico:")
                    frec_estimu= float(input("Frecuencia de estimulacion:"))

                    marcapasos= Marcapasos()
                    marcapasos.asignar_num_electrodos(num_electrodos)
                    marcapasos.asignar_almbrico_o_inalambrico(alambric_inalambric)
                    marcapasos.asignar__frecuencia_estimulacion(frec_estimu)

                    sistema.ingresar_protesis(marcapasos)
                    print("¡Registro Exitoso¡")
                
                elif entrada==5:
                    nombre= input("Nombre de la protesis:")
                    num_electrodos= int(input("Numero de electrodos:"))
                    alambric_inalambric= input("Alambrico o inalambrico:")
                    frec_estimu= float(input("Frecuencia de estimulacion:"))

                    marcapasos= Marcapasos()
                    marcapasos.asignar_num_electrodos(num_electrodos)
                    marcapasos.asignar_almbrico_o_inalambrico(alambric_inalambric)
                    marcapasos.asignar__frecuencia_estimulacion(frec_estimu)

                    sistema.ingresar_protesis(marcapasos)
                    print("¡Registro Exitoso¡")

                else:
                    break
        except ValueError:
            print("Error:Ingrese un valor valido")

main()