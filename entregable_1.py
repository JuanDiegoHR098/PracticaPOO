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
    
    def ver_forma(self):
        return self.__forma
    
    def ver_sis_fijacion(self):
        return self.__sis_fijacion
    
    def ver_material(self):
        return self.__material
    
    #Setters

    def asignar_nombre(self,nombre):
        self.__nombre = nombre 

    def asignar_forma(self,forma):
        self.__forma = forma

    def asignar_sis_fijacion(self,sis_fijacion):
        self.__sis_fijacion = sis_fijacion
    
    def asignar_material(self,material):
        self.__material= material
        
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
    
    def ver_tipo_fijacion(self):
        return self.__tipo_fijacion
    
    def ver_tamaño(self):
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
        self.__nombre = ""
        self.__cedula = 0
        self.__edad = 0
        self.__implante = None
        self.__fecha_implantacion = None

    def asignar_nombre(self, nombre):
        self.__nombre = nombre

    def asignar_cedula(self, cedula):
        self.__cedula = cedula

    def asignar_edad(self, edad):
        self.__edad = edad

    def asignar_implante(self, implante, fecha_implantacion):
        self.__implante = implante
        self.__fecha_implantacion = fecha_implantacion

    def ver_info_paciente(self):
        return f"Nombre: {self.__nombre}, Cédula: {self.__cedula}, Edad: {self.__edad}, Implante: {self.__implante.ver_nombre()}, Fecha de implantación: {self.__fecha_implantacion}"


    def seguimiento_implante(self, nombre_implante, fecha_revision, estado):
        # Realizar seguimiento del implante
        for implante_info in self.__implantes:
            if implante_info["implante"].ver_nombre() == nombre_implante:
                implante_info["estado"] = estado
                implante_info["fecha_revision"] = fecha_revision
                print(f"Seguimiento exitoso para el implante '{nombre_implante}'. Estado actual: {estado}, "
                    f"Fecha de revisión: {fecha_revision}")
                return
        print(f"Implante '{nombre_implante}' no encontrado para el paciente.")


################################################ SISTEMA  #######################################
class Sistema:
    def __init__(self) -> None:
        self.__lista_marcapasos=[]
        self.__lista_stent_coronario=[]
        self.__lista_implante_dental=[]
        self.__lista_imp_rodilla=[]
        self.__lista_imp_cadera=[]
        self.__lista_pacientes = []

    def ver_lista_marcapasos(self):
        return self.__lista_marcapasos
    def ver_lista_pacientes(self):
        return self.__lista_pacientes

    def ingresar_paciente(self, paciente):
        self.__lista_pacientes.append(paciente)

    def ingresar_Marcapasos(self,protesis):
        self.__lista_marcapasos.append(protesis)

    def ingresar_stent_coronario(self,stent):
        self.__lista_stent_coronario.append(stent)

    def ingresar_implante_dental(self,imp_dental):
        self.__lista_implante_dental.append(imp_dental)

    def ingresar_implante_rodilla(self,imp_rodilla):
        self.__lista_imp_rodilla.append(imp_rodilla)

    def ingresar_implante_cadera(self,imp_cadera):
        self.__lista_imp_cadera.append(imp_cadera)

    def eliminar_protesis(self, protesis):
        if protesis in self.__lista_marcapasos:
            self.__lista_marcapasos.remove(protesis)
        elif protesis in self.__lista_stent_coronario:
            self.__lista_stent_coronario.remove(protesis)
        elif protesis in self.__lista_implante_dental:
            self.__lista_implante_dental.remove(protesis)
        elif protesis in self.__lista_imp_rodilla:
            self.__lista_imp_rodilla.remove(protesis)
        elif protesis in self.__lista_imp_cadera:
            self.__lista_imp_cadera.remove(protesis)
    def editar_protesis(self, nombre_protesis, atributo, nuevo_valor):
        for lista in [self.__lista_marcapasos, self.__lista_stent_coronario, self.__lista_implante_dental,self.__lista_imp_rodilla, self.__lista_imp_cadera]:
            for protesis in lista:
                if protesis.ver_nombre() == nombre_protesis:
                    setattr(protesis, atributo, nuevo_valor)
                    print(f"Edición exitosa. Nuevo valor para '{atributo}': {nuevo_valor}")
                    return
        print(f"Prótesis '{nombre_protesis}' no encontrada.")

    def ingresar_paciente(self, paciente):
        self.__lista_pacientes.append(paciente)

    def ver_implante_por_nombre(self, nombre_implante):
        for marcapasos in self.__lista_marcapasos:
            if marcapasos.ver_nombre() == nombre_implante:
                yield marcapasos

        for stent in self.__lista_stent_coronario:
            if stent.ver_nombre() == nombre_implante:
                yield stent

        for imp_dental in self.__lista_implante_dental:
            if imp_dental.ver_nombre() == nombre_implante:
                yield imp_dental

        for imp_rodilla in self.__lista_imp_rodilla:
            if imp_rodilla.ver_nombre() == nombre_implante:
                yield imp_rodilla

        for imp_cadera in self.__lista_imp_cadera:
            if imp_cadera.ver_nombre() == nombre_implante:
                yield imp_cadera

    def ver_marcapasos(self):
        return self.__lista_marcapasos

    def ver_stent_coronario(self):
        return self.__lista_stent_coronario

    def ver_implante_dental(self):
        return self.__lista_implante_dental

    def ver_implante_rodilla(self):
        return self.__lista_imp_rodilla

    def ver_implante_cadera(self):
        return self.__lista_imp_cadera

sistema= Sistema()
def main():
    print("-"*30)
    print("Bienvenido al sistema de gestion de inventarios de protesis")
    print("-"*30)

    while True:
        try:
            #MENU
            print("¿Que desa hacer?\n")
            print("1.Agregar nuevo implante\n2.Eliminar \n3.Editar\n4.Visualizar\n5. Asignacion de protesis a paciente\n6. Seguimiento")
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

                    sistema.ingresar_Marcapasos(marcapasos)
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
                    forma= (input("Forma:"))
                    sis_fijacion= input("Sistema de fijacion:")
                    material= (input("Material:"))

                    imp_dental= Implante_dental()
                    imp_dental.asignar_nombre(nombre)
                    imp_dental.asignar_forma(forma)
                    imp_dental.asignar_sis_fijacion(sis_fijacion)
                    imp_dental.asignar_material(material)

                    sistema.ingresar_implante_dental(imp_dental)
                    print("¡Registro Exitoso¡")
                
                #IMPLANTE RODILLA
                elif entrada==4:
                    nombre= input("Nombre de la protesis:")
                    material= float(input("Msterial:"))
                    tipo_fijacion= input("Tipo de fijacion:")
                    tamaño= float(input("Tamaño:"))

                    imp_rodilla= Implante_rodilla()
                    imp_rodilla.asignar_nombre(nombre)
                    imp_rodilla.asignar_material(material)
                    imp_rodilla.asignar_tipo_fijacion(tipo_fijacion)
                    imp_rodilla.asignar_tamaño(tamaño)

                    sistema.ingresar_implante_rodilla(imp_rodilla)
                    print("¡Registro Exitoso¡")
                
                elif entrada==5:
                    nombre= input("Nombre de la protesis:")
                    material= float(input("Msterial:"))
                    tipo_fijacion= input("Tipo de fijacion:")
                    tamaño= float(input("Tamaño:"))

                    imp_cadera= Implante_cadera()
                    imp_cadera.asignar_nombre(nombre)
                    imp_cadera.asignar_material(material)
                    imp_cadera.asignar_tipo_fijacion(tipo_fijacion)
                    imp_cadera.asignar_tamaño(tamaño)

                    sistema.ingresar_implante_cadera(imp_cadera)
                    print("¡Registro Exitoso¡")
            

            #################################### ELIMINAR PROTESIS ###############################################

            if inicio == 2:
                print("-" * 30)
                print("¿Qué tipo de prótesis desea eliminar?")
                print("-" * 30)
                print("1. Marcapasos\n2. Stent coronario\n3. Implante dental\n4. Implante de rodilla\n5. Implante de cadera\n")
                tipo_protesis = int(input("Ingrese una opción:"))

                if tipo_protesis in range(1, 6):
                    print("-" * 30)
                    nombre_protesis = input("Ingrese el nombre de la prótesis que desea eliminar: ")

                    if tipo_protesis == 1:
                        sistema.eliminar_protesis(nombre_protesis)

                    elif tipo_protesis == 2:
                        sistema.eliminar_protesis(nombre_protesis)

                    elif tipo_protesis == 3:
                        sistema.eliminar_protesis(nombre_protesis)

                    elif tipo_protesis == 4:
                        sistema.eliminar_protesis(nombre_protesis)

                    elif tipo_protesis == 5:
                        sistema.eliminar_protesis(nombre_protesis)

                    print(f"Prótesis '{nombre_protesis}' eliminada con éxito.")

                else:
                    print("Opción no válida. Intente de nuevo.")

            elif inicio == 3:
                print("-" * 30)
                print("¿Qué tipo de prótesis desea editar?")
                print("-" * 30)
                print("1. Marcapasos\n2. Stent coronario\n3. Implante dental\n4. Implante de rodilla\n5. Implante de cadera\n")
                tipo_protesis = int(input("Ingrese una opción:"))

                if tipo_protesis in range(1, 6):
                    print("-" * 30)
                    nombre_protesis = input("Ingrese el nombre de la prótesis que desea editar: ")
                    atributo = input("Ingrese el atributo que desea editar: ")
                    nuevo_valor = input(f"Ingrese el nuevo valor para '{atributo}': ")

                    sistema.editar_protesis(nombre_protesis, atributo, nuevo_valor)

                else:
                    print("Opción no válida. Intente de nuevo.")

            elif inicio == 4:
                print("-" * 30)
                print("Inventario completo:")
                for marcapasos in sistema.ver_marcapasos():  # Agregar paréntesis aquí
                    print(f"Tipo: Marcapasos, Nombre: {marcapasos.ver_nombre()}, Electrodos: {marcapasos.ver_num_electrodos()}, "
                        f"Alámbrico/Inalámbrico: {marcapasos.ver_almbrico_o_inalambrico()}, Frecuencia: {marcapasos.ver_frecuencia_estimulacion()}")

                for stent in sistema.ver_stent_coronario():  # Agregar paréntesis aquí
                    print(f"Tipo: Stent Coronario, Nombre: {stent.ver_nombre()}, Longitud: {stent.ver_longitud()}, "
                        f"Diametro: {stent.ver_diametro()}, Material: {stent.ver_material()}")

                for imp_dental in sistema.ver_implante_dental():  # Agregar paréntesis aquí
                    print(f"Tipo: Implante Dental, Nombre: {imp_dental.ver_nombre()}, Forma: {imp_dental.ver_forma()}, "
                        f"Sistema de Fijación: {imp_dental.ver_sis_fijacion()}, Material: {imp_dental.ver_material()}")

                for imp_rodilla in sistema.ver_implante_rodilla():  # Agregar paréntesis aquí
                    print(f"Tipo: Implante de Rodilla, Nombre: {imp_rodilla.ver_nombre()}, Material: {imp_rodilla.ver_material()}, "
                        f"Tipo de Fijación: {imp_rodilla.ver_tipo_fijacion()}, Tamaño: {imp_rodilla.ver_tamaño()}")

                for imp_cadera in sistema.ver_implante_cadera():  # Agregar paréntesis aquí
                    print(f"Tipo: Implante de Cadera, Nombre: {imp_cadera.ver_nombre()}, Material: {imp_cadera.ver_material()}, "
                        f"Tipo de Fijación: {imp_cadera.ver_tipo_fijacion()}, Tamaño: {imp_cadera.ver_tamaño()}")

                print("-" * 30)

            elif inicio == 5:
                print("-" * 30)
                print("Crear Paciente y Asignar Prótesis")
                print("-" * 30)

                nombre_paciente = input("Ingrese el nombre del paciente: ")
                cedula_paciente = int(input("Ingrese la cédula del paciente: "))
                edad_paciente = int(input("Ingrese la edad del paciente: "))

                # Crear un nuevo objeto de paciente
                nuevo_paciente = Pacientes()
                nuevo_paciente.asignar_nombre(nombre_paciente)
                nuevo_paciente.asignar_cedula(cedula_paciente)
                nuevo_paciente.asignar_edad(edad_paciente)

                # Agregar el paciente al sistema
                sistema.ingresar_paciente(nuevo_paciente)
                print(f"Paciente '{nombre_paciente}' creado exitosamente.")

                # Asignar prótesis al paciente
                implante_a_asignar = input("Ingrese el nombre del implante a asignar: ")
                fecha_implantacion = input("Ingrese la fecha de implantación (YYYY-MM-DD): ")

                # Verificar si el implante existe en el inventario
                implante_existente = None
                for implante in sistema.ver_implante_por_nombre(implante_a_asignar):
                    implante_existente = implante
                    break

                if implante_existente:
                    # Asignar implante al paciente
                    nuevo_paciente.asignar_implante(implante_existente, fecha_implantacion)
                    print(f"Implante '{implante_a_asignar}' asignado exitosamente al paciente '{nombre_paciente}'.")
                else:
                    print(f"Implante '{implante_a_asignar}' no encontrado en el inventario.")




        except ValueError:
            print("Error:Ingrese un valor valido")


main()