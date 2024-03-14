from datetime import datetime

class Marcapasos:
    def __init__(self):
        self.__nombre = ""
        self.__num_electrodos = 0
        self.__almbrico_o_inalambrico = ""
        self.__frecuencia_estimulacion = 0.0

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_num_electrodos(self):
        return self.__num_electrodos

    def set_num_electrodos(self, num_electrodos):
        self.__num_electrodos = num_electrodos

    def get_almbrico_o_inalambrico(self):
        return self.__almbrico_o_inalambrico

    def set_almbrico_o_inalambrico(self, almbrico_o_inalambrico):
        self.__almbrico_o_inalambrico = almbrico_o_inalambrico

    def get_frecuencia_estimulacion(self):
        return self.__frecuencia_estimulacion

    def set_frecuencia_estimulacion(self, frecuencia_estimulacion):
        self.__frecuencia_estimulacion = frecuencia_estimulacion


class StentCoronario:
    def __init__(self):
        self.__nombre = ""
        self.__longitud = 0.0
        self.__diametro = 0.0
        self.__material = ""

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_longitud(self):
        return self.__longitud

    def set_longitud(self, longitud):
        self.__longitud = longitud

    def get_diametro(self):
        return self.__diametro

    def set_diametro(self, diametro):
        self.__diametro = diametro

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material


class ImplanteDental:
    def __init__(self):
        self.__nombre = ""
        self.__forma = ""
        self.__sis_fijacion = ""
        self.__material = ""

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_forma(self):
        return self.__forma

    def set_forma(self, forma):
        self.__forma = forma

    def get_sis_fijacion(self):
        return self.__sis_fijacion

    def set_sis_fijacion(self, sis_fijacion):
        self.__sis_fijacion = sis_fijacion

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material


class ImplanteRodilla:
    def __init__(self):
        self.__nombre = ""
        self.__material = ""
        self.__tipo_fijacion = ""
        self.__tamaño = 0.0

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material

    def get_tipo_fijacion(self):
        return self.__tipo_fijacion

    def set_tipo_fijacion(self, tipo_fijacion):
        self.__tipo_fijacion = tipo_fijacion

    def get_tamaño(self):
        return self.__tamaño

    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño


class ImplanteCadera(ImplanteRodilla):
    def __init__(self):
        super().__init__()

class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__edad = 0
        self.__implantes = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_cedula(self):
        return self.__cedula

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def asignar_implante(self, implante, fecha_implantacion, medico_responsable):
        implante_info = {
            "implante": implante,
            "fecha_implantacion": fecha_implantacion,
            "medico_responsable": medico_responsable,
            "fecha_revision": None,
            "estado_implante": "En buen estado"
        }
        self.__implantes.append(implante_info)

    def ver_implantes(self):
        return self.__implantes

    def seguimiento_implante(self, fecha_revision, estado_implante):
        for implante_info in self.__implantes:
            if implante_info['estado_implante'] == "En buen estado":
                implante_info['fecha_revision'] = fecha_revision
                implante_info['estado_implante'] = estado_implante
                return f"\nSeguimiento del implante '{implante_info['implante'].get_nombre()}':\n" \
                    f"Fecha de implantación: {implante_info['fecha_implantacion']}\n" \
                    f"Médico responsable: {implante_info['medico_responsable']}\n" \
                    f"Fecha de revisión: {implante_info['fecha_revision']}\n" \
                    f"Estado actual: {implante_info['estado_implante']}"
            break

    def visualizar_seguimiento_implantes(self):
        if self.__implantes:
            print("-" * 30)
            print(f"Seguimiento de Implantes para el paciente {self.get_nombre()}")
            print("-" * 30)
            for implante_info in self.__implantes:
                print(f"\nImplante: {implante_info['implante'].get_nombre()}")
                print(f"Fecha de implantación: {implante_info['fecha_implantacion']}")
                print(f"Médico responsable: {implante_info['medico_responsable']}")
                print(f"Fecha de revisión: {implante_info['fecha_revision']}")
                print(f"Estado de seguimiento: {implante_info['estado_implante']}")
            print("-" * 30)
        else:
            print("El paciente no tiene asignado ningún implante.")




class Sistema:
    def __init__(self):
        self.__lista_marcapasos = []
        self.__lista_stent_coronario = []
        self.__lista_implante_dental = []
        self.__lista_imp_rodilla = []
        self.__lista_imp_cadera = []
        self.__lista_pacientes = []

    # Métodos para agregar prótesis a las listas
    def ingresar_marcapasos(self, marcapasos):
        self.__lista_marcapasos.append(marcapasos)

    def ingresar_stent_coronario(self, stent):
        self.__lista_stent_coronario.append(stent)

    def ingresar_implante_dental(self, implante_dental):
        self.__lista_implante_dental.append(implante_dental)

    def ingresar_implante_rodilla(self, implante_rodilla):
        self.__lista_imp_rodilla.append(implante_rodilla)

    def ingresar_implante_cadera(self, implante_cadera):
        self.__lista_imp_cadera.append(implante_cadera)

    def ver_implante_por_nombre(self, nombre_implante):
        for marcapasos in self.__lista_marcapasos:
            if marcapasos.get_nombre() == nombre_implante:
                yield marcapasos

        for stent in self.__lista_stent_coronario:
            if stent.get_nombre() == nombre_implante:
                yield stent

        for imp_dental in self.__lista_implante_dental:
            if imp_dental.get_nombre() == nombre_implante:
                yield imp_dental

        for imp_rodilla in self.__lista_imp_rodilla:
            if imp_rodilla.get_nombre() == nombre_implante:
                yield imp_rodilla

        for imp_cadera in self.__lista_imp_cadera:
            if imp_cadera.get_nombre() == nombre_implante:
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

    def ingresar_paciente(self, paciente):
        self.__lista_pacientes.append(paciente)
    # no funciona
    def eliminar_protesis(self, nombre_protesis):
        for lista in [self.__lista_marcapasos, self.__lista_stent_coronario, self.__lista_implante_dental,
                    self.__lista_imp_rodilla, self.__lista_imp_cadera]:
            for protesis in lista[:]:  
                if protesis.get_nombre() == nombre_protesis:
                    lista.remove(protesis)
                    print(f"Prótesis '{nombre_protesis}' eliminada con éxito.")
                    return
        print(f"Prótesis '{nombre_protesis}' no encontrada.")
        

    def editar_protesis(self, nombre_protesis, atributo, nuevo_valor):
        for lista in [self.__lista_marcapasos, self.__lista_stent_coronario, self.__lista_implante_dental,
                    self.__lista_imp_rodilla, self.__lista_imp_cadera]:
            for protesis in lista:
                if protesis.get_nombre() == nombre_protesis:
                    setattr(protesis, atributo, nuevo_valor)
                    print(f"Edición exitosa. Nuevo valor para '{atributo}': {nuevo_valor}")

                    # Actualizar información en el inventario
                    self.actualizar_inventario()

                    # Actualizar la información en la lista de pacientes
                    for paciente in self.__lista_pacientes:
                        for implante_info in paciente.ver_implantes():
                            if implante_info['implante'].get_nombre() == nombre_protesis:
                                implante_info['implante'] = protesis
                    return
        print(f"Prótesis '{nombre_protesis}' no encontrada.")

    def ver_pacientes(self):
        return self.__lista_pacientes

    def hacer_seguimiento_paciente(self, nombre_paciente):
        for paciente in self.__lista_pacientes:
            if paciente.get_nombre() == nombre_paciente:
                print("-" * 30)
                print(f"Seguimiento del paciente {nombre_paciente}")
                print("-" * 30)
                print(f"Cédula: {paciente.get_cedula()}")
                print(f"Edad: {paciente.get_edad()} años")

                implantes_paciente = paciente.ver_implantes()
                if implantes_paciente:
                    print("\nPrótesis asignadas:")
                    for implante_info in implantes_paciente:
                        print(f"Nombre: {implante_info['implante'].get_nombre()}, "
                            f"Fecha de implantación: {implante_info['fecha_implantacion']}, "
                            f"Estado: {implante_info['estado_implante']}, "
                            f"Fecha de revisión: {implante_info.get('fecha_revision', 'No revisado')}")
                else:
                    print("\nEste paciente no tiene prótesis asignadas.")
                print("-" * 30)
                return

        print(f"Paciente '{nombre_paciente}' no encontrado.")

    def actualizar_inventario(self):
        self.__lista_marcapasos = [p for p in self.__lista_marcapasos if p]
        self.__lista_stent_coronario = [s for s in self.__lista_stent_coronario if s]
        self.__lista_implante_dental = [id for id in self.__lista_implante_dental if id]
        self.__lista_imp_rodilla = [ir for ir in self.__lista_imp_rodilla if ir]
        self.__lista_imp_cadera = [ic for ic in self.__lista_imp_cadera if ic]

        # Actualizar información en la lista de pacientes
        for paciente in self.__lista_pacientes:
            for implante_info in paciente.ver_implantes():
                nombre_implante = implante_info['implante'].get_nombre()

                for lista in [self.__lista_marcapasos, self.__lista_stent_coronario, self.__lista_implante_dental,
                            self.__lista_imp_rodilla, self.__lista_imp_cadera]:
                    for protesis in lista:
                        if protesis.get_nombre() == nombre_implante:
                            implante_info['implante'] = protesis
    
    def ver_inventario(self):
        print("-" * 30)
        print("Inventario completo:")

        # Marcapasos
        for marcapasos in self.ver_marcapasos():
            print(f"Tipo: Marcapasos, Nombre: {marcapasos.get_nombre()}, Electrodos: {marcapasos.get_num_electrodos()}, "
                f"Alámbrico/Inalámbrico: {marcapasos.get_almbrico_o_inalambrico()}, Frecuencia: {marcapasos.get_frecuencia_estimulacion()}")

        # Stent Coronario
        for stent in self.ver_stent_coronario():
            print(f"Tipo: Stent Coronario, Nombre: {stent.get_nombre()}, Longitud: {stent.get_longitud()}, "
                f"Diametro: {stent.get_diametro()}, Material: {stent.get_material()}")

        # Implante Dental
        for imp_dental in self.ver_implante_dental():
            print(f"Tipo: Implante Dental, Nombre: {imp_dental.get_nombre()}, Forma: {imp_dental.get_forma()}, "
                f"Sistema de Fijación: {imp_dental.get_sis_fijacion()}, Material: {imp_dental.get_material()}")

        # Implante de Rodilla
        for imp_rodilla in self.ver_implante_rodilla():
            print(f"Tipo: Implante de Rodilla, Nombre: {imp_rodilla.get_nombre()}, Material: {imp_rodilla.get_material()}, "
                f"Tipo de Fijación: {imp_rodilla.get_tipo_fijacion()}, Tamaño: {imp_rodilla.get_tamaño()}")

        # Implante de Cadera
        for imp_cadera in self.ver_implante_cadera():
            print(f"Tipo: Implante de Cadera, Nombre: {imp_cadera.get_nombre()}, Material: {imp_cadera.get_material()}, "
                f"Tipo de Fijación: {imp_cadera.get_tipo_fijacion()}, Tamaño: {imp_cadera.get_tamaño()}")

        print("-" * 30)

def main():
    try:
        sistema = Sistema()
        print("-" * 30)
        print("Bienvenido al sistema de gestión de inventarios de prótesis")
        print("-" * 30)

        while True:
            try:
                # MENÚ
                print("¿Qué desea hacer?\n")
                print("1. Agregar nuevo implante\n2. Eliminar\n3. Editar\n4. Visualizar\n"
                    "5. Asignación de prótesis a paciente\n6. Seguimiento\n7. Visualizar seguimiento\n8. Salir")
                while True:
                                try:
                                    inicio = int(input("Ingrese una opción: "))
                                    break
                                except ValueError:
                                    print("Error: Por favor, ingrese solo números.")
                

                # AGREGAR NUEVA PRÓTESIS
                if inicio == 1:
                    print("-" * 30)
                    print("¿Qué tipo de prótesis desea agregar?")
                    print("-" * 30)
                    print("1. Marcapasos\n2. Stent coronario\n3. Implante dental\n4. Implante de rodilla\n5. Implante de cadera\n")
                    while True:
                                try:
                                    entrada = int(input("Ingrese una opción: "))
                                    break
                                except ValueError:
                                    print("Error: Por favor, ingrese solo números.")
                    

                    if entrada in range(1, 6):
                        nombre = input("Nombre de la prótesis: ")

                        if entrada == 1:
                            
                            while True:
                                try:
                                    num_electrodos = int(input("Número de electrodos: "))
                                    break
                                except ValueError:
                                    print("Error: Por favor, ingrese solo números.")

                            alambrico_inalambrico = input("Alámbrico o inalámbrico: ")
                            while True:
                                try:
                                    frec_estimu = float(input("Frecuencia de estimulación: "))
                                    break
                                except ValueError:
                                    print("Error: Por favor, ingrese solo números.")
                            

                            marcapasos = Marcapasos()
                            marcapasos.set_nombre(nombre)
                            marcapasos.set_num_electrodos(num_electrodos)
                            marcapasos.set_almbrico_o_inalambrico(alambrico_inalambrico)
                            marcapasos.set_frecuencia_estimulacion(frec_estimu)

                            sistema.ingresar_marcapasos(marcapasos)
                            print("¡Registro Exitoso!")

                        elif entrada == 2:
                            while True:
                                try:
                                    longitud = float(input("Longitud: "))
                                    break
                                except ValueError:
                                    print("Error: Por favor, ingrese solo números.")
                            while True:
                                try:
                                    diametro = float(input("Diámetro: "))
                                    break
                                except ValueError:
                                    print("Error: Por favor, ingrese solo números.")
                            
                            material = input("Material: ")

                            stent = StentCoronario()
                            stent.set_nombre(nombre)
                            stent.set_longitud(longitud)
                            stent.set_diametro(diametro)
                            stent.set_material(material)

                            sistema.ingresar_stent_coronario(stent)
                            print("¡Registro Exitoso!")

                        elif entrada == 3:
                            forma = input("Forma: ")
                            sis_fijacion = input("Sistema de fijación: ")
                            material = input("Material: ")

                            imp_dental = ImplanteDental()
                            imp_dental.set_nombre(nombre)
                            imp_dental.set_forma(forma)
                            imp_dental.set_sis_fijacion(sis_fijacion)
                            imp_dental.set_material(material)

                            sistema.ingresar_implante_dental(imp_dental)
                            print("¡Registro Exitoso!")

                        elif entrada == 4:
                            material = input("Material: ")
                            tipo_fijacion = input("Tipo de fijación: ")
                            while True:
                                try:
                                    tamaño = float(input("Tamaño: "))
                                    break
                                except ValueError:
                                    print("Error: Por favor, ingrese solo números.")
                            

                            imp_rodilla = ImplanteRodilla()
                            imp_rodilla.set_nombre(nombre)
                            imp_rodilla.set_material(material)
                            imp_rodilla.set_tipo_fijacion(tipo_fijacion)
                            imp_rodilla.set_tamaño(tamaño)

                            sistema.ingresar_implante_rodilla(imp_rodilla)
                            print("¡Registro Exitoso!")

                        elif entrada == 5:
                            material = input("Material: ")
                            tipo_fijacion = input("Tipo de fijación: ")
                            while True:
                                try:
                                    tamaño = float(input("Tamaño: "))
                                    break
                                except ValueError:
                                    print("Error: Por favor, ingrese solo números.")
                            

                            imp_cadera = ImplanteCadera()
                            imp_cadera.set_nombre(nombre)
                            imp_cadera.set_material(material)
                            imp_cadera.set_tipo_fijacion(tipo_fijacion)
                            imp_cadera.set_tamaño(tamaño)

                            sistema.ingresar_implante_cadera(imp_cadera)
                            print("¡Registro Exitoso!")

                # ELIMINAR PRÓTESIS
                elif inicio == 2:
                    print("-" * 30)
                    print("¿Qué tipo de prótesis desea eliminar?")
                    print("-" * 30)
                    print("1. Marcapasos\n2. Stent coronario\n3. Implante dental\n4. Implante de rodilla\n5. Implante de cadera\n")
                    tipo_protesis = int(input("Ingrese una opción: "))

                    if tipo_protesis in range(1, 6):
                        print("-" * 30)
                        nombre_protesis = input("Ingrese el nombre de la prótesis que desea eliminar: ")

                        sistema.eliminar_protesis(nombre_protesis)

                # EDITAR PRÓTESIS
                elif inicio == 3:
                    print("-" * 30)
                    print("¿Qué tipo de prótesis desea editar?")
                    print("-" * 30)
                    print("1. Marcapasos\n2. Stent coronario\n3. Implante dental\n4. Implante de rodilla\n5. Implante de cadera\n")
                    tipo_protesis = int(input("Ingrese una opción: "))

                    if tipo_protesis in range(1, 6):
                        print("-" * 30)
                        nombre_protesis = input("Ingrese el nombre de la prótesis que desea editar: ")
                        atributo = input("Ingrese el atributo que desea editar: ")

                        # Obtener el nuevo valor
                        nuevo_valor = input(f"Ingrese el nuevo valor para '{atributo}': ")

                        # Editar la prótesis y guardar cambios
                        sistema.editar_protesis(nombre_protesis, atributo, nuevo_valor)
                        sistema.actualizar_inventario()  # Llamamos explícitamente al método de actualización del inventario

                        # Visualizar los cambios en el inventario
                        sistema.ver_inventario()

                # VISUALIZAR INVENTARIO
                elif inicio == 4:
                    print("-" * 30)
                    print("Inventario completo:")

                    # Marcapasos
                    for marcapasos in sistema.ver_marcapasos():
                        print(f"Tipo: Marcapasos, Nombre: {marcapasos.get_nombre()}, Electrodos: {marcapasos.get_num_electrodos()}, "
                            f"Alámbrico/Inalámbrico: {marcapasos.get_almbrico_o_inalambrico()}, Frecuencia: {marcapasos.get_frecuencia_estimulacion()}")

                    # Stent Coronario
                    for stent in sistema.ver_stent_coronario():
                        print(f"Tipo: Stent Coronario, Nombre: {stent.get_nombre()}, Longitud: {stent.get_longitud()}, "
                            f"Diametro: {stent.get_diametro()}, Material: {stent.get_material()}")

                    # Implante Dental
                    for imp_dental in sistema.ver_implante_dental():
                        print(f"Tipo: Implante Dental, Nombre: {imp_dental.get_nombre()}, Forma: {imp_dental.get_forma()}, "
                            f"Sistema de Fijación: {imp_dental.get_sis_fijacion()}, Material: {imp_dental.get_material()}")

                    # Implante de Rodilla
                    for imp_rodilla in sistema.ver_implante_rodilla():
                        print(f"Tipo: Implante de Rodilla, Nombre: {imp_rodilla.get_nombre()}, Material: {imp_rodilla.get_material()}, "
                            f"Tipo de Fijación: {imp_rodilla.get_tipo_fijacion()}, Tamaño: {imp_rodilla.get_tamaño()}")

                    # Implante de Cadera
                    for imp_cadera in sistema.ver_implante_cadera():
                        print(f"Tipo: Implante de Cadera, Nombre: {imp_cadera.get_nombre()}, Material: {imp_cadera.get_material()}, "
                            f"Tipo de Fijación: {imp_cadera.get_tipo_fijacion()}, Tamaño: {imp_cadera.get_tamaño()}")

                    print("-" * 30)

                # ASIGNACIÓN DE PRÓTESIS A PACIENTE
                elif inicio == 5:
                    print("-" * 30)
                    print("Crear Paciente y Asignar Prótesis")
                    print("-" * 30)

                    nombre_paciente = input("Ingrese el nombre del paciente: ")
                    while True:
                                try:
                                    cedula_paciente = int(input("Ingrese la cédula del paciente: "))
                                    break
                                except ValueError:
                                    print("Error: Por favor, ingrese solo números.")
                    
                    while True:
                                try:
                                    edad_paciente = int(input("Ingrese la edad del paciente: "))
                                    break
                                except ValueError:
                                    print("Error: Por favor, ingrese solo números.")
                    

                    # Crear un nuevo objeto de paciente
                    nuevo_paciente = Paciente()
                    nuevo_paciente.set_nombre(nombre_paciente)
                    nuevo_paciente.set_cedula(cedula_paciente)
                    nuevo_paciente.set_edad(edad_paciente)

                    # Agregar el paciente al sistema
                    sistema.ingresar_paciente(nuevo_paciente)
                    print(f"Paciente '{nombre_paciente}' creado exitosamente.")

                    # Asignar prótesis al paciente
                    implante_a_asignar = input("Ingrese el nombre del implante a asignar: ")
                    while True:
                        fecha_implantacion = input("Ingrese la fecha de implantación (AAAA/MM/DD): ")
                        try:
                            datetime.strptime(fecha_implantacion, '%Y/%m/%d')
                            break
                        except ValueError:
                            print("Error: Formato de fecha inválido. Por favor, ingrese la fecha en el formato AAAA/MM/DD.")
                    
                    medico_responsable = input("Ingrese el nombre del médico responsable: ")  # Agregado

                    # Verificar si el implante existe en el inventario
                    implante_existente = None
                    for implante in sistema.ver_implante_por_nombre(implante_a_asignar):
                        implante_existente = implante
                        break

                    if implante_existente:
                        # Asignar implante al paciente
                        nuevo_paciente.asignar_implante(implante_existente, fecha_implantacion, medico_responsable)  # Corregido
                        print(f"Implante '{implante_a_asignar}' asignado exitosamente al paciente '{nombre_paciente}'.")
                    else:
                        print(f"Implante '{implante_a_asignar}' no encontrado en el inventario.")

                # SEGUMIENTO DE PACIENTES E IMPLANTES
                elif inicio == 6:
                    print("-" * 30)
                    print("Seguimiento de Pacientes e Implantes")
                    print("-" * 30)

                    nombre_paciente_seguimiento = input("Ingrese el nombre del paciente: ")
                    fecha_revision = input("Ingrese la fecha de revisión (YYYY/MM/DD): ")
                    estado_implante = input("Ingrese el estado del implante: ")

                    for paciente in sistema.ver_pacientes():
                        if paciente.get_nombre() == nombre_paciente_seguimiento:
                            seguimiento_info = paciente.seguimiento_implante(fecha_revision, estado_implante)
                            if implante_existente:
                                # Asignar implante al paciente
                                nuevo_paciente.asignar_implante(implante_existente, fecha_implantacion, medico_responsable)  # Corregido
                                print(f"Implante '{implante_a_asignar}' asignado exitosamente al paciente '{nombre_paciente}'.")
                            else:
                                print(f"Implante '{implante_a_asignar}' no encontrado en el inventario.")

                # SALIR
                elif inicio == 7:
                    print("-" * 30)
                    print("Visualizar Seguimiento de Implantes")
                    print("-" * 30)

                    nombre_paciente_seguimiento = input("Ingrese el nombre del paciente: ")

                    for paciente in sistema.ver_pacientes():
                        if paciente.get_nombre() == nombre_paciente_seguimiento:
                            paciente.visualizar_seguimiento_implantes()  # Corregido
                            break
                    else:
                        print(f"Paciente '{nombre_paciente_seguimiento}' no encontrado.")

                elif inicio == 8:
                    print("Saliendo del sistema...")
                    break

                else:
                    print("Opción no válida. Intente de nuevo.")

            except ValueError:
                print("Por favor, ingrese una opción válida.")
    except ValueError:
        print("Ingrese un valor valido")

if __name__ == "__main__":
    main()



