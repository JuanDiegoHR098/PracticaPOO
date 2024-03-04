#ESTE DOCUMENTO FUE ELABORADO DESDE CERO


class Persona:
    #Inicializador de clase persona
    def __init__(self) -> None:
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_cedula(self):
        return self.__cedula

    def get_genero(self):
        return self.__genero

    def get_servicio(self):
        return self.__servicio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def set_genero(self, genero):
        self.__genero = genero

    def set_servicio(self, servicio):
        self.__servicio = servicio


class Sistema:
    # Inicializador de la clase sistema donde se almacenaran obejtos tipo paciente
    def __init__(self) -> None:
        self.__lista_paciente = []

    #Getters
    def get_listaPacientes(self):
        return self.__lista_paciente

    def get_numeroPacientes(self):
        return len(self.__lista_paciente)

    #Se utiliza el metodo append() para agregra objetos tipo paciente en la lista de pacientes
    def ingresar_paciente(self, paciente):
        self.__lista_paciente.append(paciente)

    #Se itera sobre la lista pacientes y se busca por la coicidencia con el numero de cedula ingresado por teclado, si el paciente no exites arrojara un mensaje indicandolo
    def buscar_paciente_cedula(self, cedula):
        pacientes_coinciden = []

        for p in self.__lista_paciente:
            if cedula == p.get_cedula():
                paciente_info = (
                    p.get_nombre(), p.get_cedula(), p.get_genero(), p.get_servicio())
                pacientes_coinciden.append(paciente_info)

        if not pacientes_coinciden:
            print("¡Paciente no encontrado!")

        return pacientes_coinciden
    
    #Se itera sobre la lista pacientes y se busca por la coicidencia con el nombre, si hay varios pacientes que coiciden arrojara la informacion de cada uno en forma ordenada
    def buscar_paciente_nombre(self, clave):
        pacientes_coinciden = []

        for p in self.__lista_paciente:
            if clave.lower() in p.get_nombre().lower():
                paciente_info = (
                    p.get_nombre(), p.get_cedula(), p.get_genero(), p.get_servicio())
                pacientes_coinciden.append(paciente_info)

        if not pacientes_coinciden:
            print("¡Paciente no encontrado!")

        return pacientes_coinciden
    
    #Se utliza para conseguir el nombre vinculado a un numero de cedula
    def conseguir_nombre(self,clave):
        for p in self.__lista_paciente:
            if clave == p.get_cedula() :
                return p.get_nombre()

    #Se itera sobre la lista pacientes y se busca coincidencias con numero de cudula para saber si ya hay un paciente vinculado con ese numero
    def Verificar_existente(self,num):
        
        for paciente in self.__lista_paciente:
            if num ==  paciente.get_cedula():
                return True
            else:
                return False

sis = Sistema()

#Menu
while True:
    try:
        print("-"*30)
        print("Menu:")
        print("-"*30)
        print("¿Que desea hacer?\n\n1. Ingresar Paciente\n2. Ver datos del paciente\n3. Ver numero de pacientes\n4. Salir")
        print("-"*30)

        entrada = int(input("Ingrese una opcion:"))

        # Ingresar al paciente
        if entrada == 1:
            
            nombre = input("Ingresar nombre del paciente:")
            
            while True:
                try:
                    cedula = int(input("Ingrese cedula del paciente:"))
                    validar_cedula = sis.Verificar_existente(cedula)
                    if validar_cedula:
                        print(f"¡Número de cédula ya existente, asociado al paciente: {sis.conseguir_nombre(cedula)}!")
                    else:
                        break
                except ValueError:
                    print("\n¡Por favor, ingerse un valor valido.!\n")
            genero = input("Genero:")
            servicio = input("Ingrese servicio donde se encuentra:")

            paciente = Persona()
            paciente.set_nombre(nombre)
            paciente.set_cedula(cedula)
            paciente.set_genero(genero)
            paciente.set_servicio(servicio)

            sis.ingresar_paciente(paciente)
            print(f"¡El paciente {nombre} se ha ingresado satisfactoriamente!")

        #Nos permitira busca al paciente ya sea por numero de cedula o por el nombre
        elif entrada == 2:
            while True:
                try: 
                    print("-"*30)
                    print("Busqueda por:")
                    print("-"*30)
                    print("1. Cedula:\n2. Nombre:\n3. Salir:")

                    opcion=int(input("Ingrese una opcion:"))
                    if opcion == 1:
                        print("-"*30)
                        busqueda_cedula= int(input("Ingrese el numero de cedula:"))
                        print("-"*30)
                        pacientes_encontrados = sis.buscar_paciente_cedula(busqueda_cedula)
                        for paciente_encontrado in pacientes_encontrados:
                            
                            print(( "Nombre: {} | Cedula: {} | Genero:{} | Servicio:{} |").format(
                                *paciente_encontrado))
                            print("-"*30)
                            if busqueda_cedula != paciente_encontrado:
                                continue
                        
                    elif opcion == 2:
                        print("-"*30)
                        busqueda_nombre= input("Ingrese el nombre del paciente:").lower()
                        print("-"*30)
                        pacientes_encontrados = sis.buscar_paciente_nombre(busqueda_nombre)
                        
                        
                        for paciente_encontrado in pacientes_encontrados:
                            print(( "Nombre: {} | Cedula: {} | Genero:{} | Servicio:{} |").format(
                                        *paciente_encontrado))
                            print("-"*30)
                        

                        


                    elif opcion==3:
                        break
                except ValueError:
                    print("\n¡Por favor, ingrese un valor valido!\n")

        #Nos devolvera la cantidad de pacientes registrados en la lista pacientes
        elif entrada == 3:
            print(f"El numero de pacientes registrados es: {sis.get_numeroPacientes()}")

        #Nos permite salir del programa
        elif entrada == 4:
            break
    except ValueError:
        print("¡Por favor, ingrese una opcion valida!")

