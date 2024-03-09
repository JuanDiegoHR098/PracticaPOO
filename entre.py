from datetime import datetime

class Marcapasos:
    def __init__(self):
        self.__nombre = ""
        self.__num_electrodos = 0
        self.__almbrico_o_inalambrico = ""
        self.__frecuencia_estimulacion = 0.0

    # Getters
    def ver_nombre(self):
        return self.__nombre

    def ver_num_electrodos(self):
        return self.__num_electrodos

    def ver_almbrico_o_inalambrico(self):
        return self.__almbrico_o_inalambrico

    def ver_frecuencia_estimulacion(self):
        return self.__frecuencia_estimulacion

    # Setters
    def asignar_nombre(self, nombre):
        self.__nombre = nombre

    def asignar_num_electrodos(self, num_electrodos):
        self.__num_electrodos = num_electrodos

    def asignar_almbrico_o_inalambrico(self, almbrico_o_inalambrico):
        self.__almbrico_o_inalambrico = almbrico_o_inalambrico

    def asignar_frecuencia_estimulacion(self, frecuencia_estimulacion):
        self.__frecuencia_estimulacion = frecuencia_estimulacion


class StentCoronario:
    def __init__(self):
        self.__nombre = ""
        self.__longitud = 0.0
        self.__diametro = 0.0
        self.__material = ""

    # Getters
    def ver_nombre(self):
        return self.__nombre

    def ver_longitud(self):
        return self.__longitud

    def ver_diametro(self):
        return self.__diametro

    def ver_material(self):
        return self.__material

    # Setters
    def asignar_nombre(self, nombre):
        self.__nombre = nombre

    def asignar_longitud(self, longitud):
        self.__longitud = longitud

    def asignar_diametro(self, diametro):
        self.__diametro = diametro

    def asignar_material(self, material):
        self.__material = material


class ImplanteDental:
    def __init__(self):
        self.__nombre = ""
        self.__forma = ""
        self.__sis_fijacion = ""
        self.__material = ""

    # Getters
    def ver_nombre(self):
        return self.__nombre

    def ver_forma(self):
        return self.__forma

    def ver_sis_fijacion(self):
        return self.__sis_fijacion

    def ver_material(self):
        return self.__material

    # Setters
    def asignar_nombre(self, nombre):
        self.__nombre = nombre

    def asignar_forma(self, forma):
        self.__forma = forma

    def asignar_sis_fijacion(self, sis_fijacion):
        self.__sis_fijacion = sis_fijacion

    def asignar_material(self, material):
        self.__material = material


class ImplanteRodilla:
    def __init__(self):
        self.__nombre = ""
        self.__material = ""
        self.__tipo_fijacion = ""
        self.__tamaño = 0.0

    # Getters
    def ver_nombre(self):
        return self.__nombre

    def ver_material(self):
        return self.__material

    def ver_tipo_fijacion(self):
        return self.__tipo_fijacion

    def ver_tamaño(self):
        return self.__tamaño

    # Setters
    def asignar_nombre(self, nombre):
        self.__nombre = nombre

    def asignar_material(self, material):
        self.__material = material

    def asignar_tipo_fijacion(self, tipo_fijacion):
        self.__tipo_fijacion = tipo_fijacion

    def asignar_tamaño(self, tamaño):
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

    def asignar_nombre(self, nombre):
        self.__nombre = nombre

    def asignar_cedula(self, cedula):
        self.__cedula = cedula

    def asignar_edad(self, edad):
        self.__edad = edad


    def ver_nombre(self):
        return self.__nombre

    def ver_cedula(self):
        return self.__cedula

    def ver_edad(self):
        return self.__edad

    def asignar_implante(self, implante, fecha_implantacion):
        self.__implantes.append({"implante": implante, "fecha_implantacion": fecha_implantacion})

    def ver_implantes(self):
        return self.__implantes

    def ver_info_paciente(self):
        if self.__implantes:
            info_implantes = ""
            for implante_info in self.__implantes:
                info_implantes += f"\n  - Nombre de la prótesis: {implante_info['implante'].ver_nombre()}\n"
                info_implantes += f"    Fecha de implantación: {implante_info['fecha_implantacion']}\n"
            return f"Nombre: {self.__nombre}, Cédula: {self.__cedula}, Edad: {self.__edad}, Implantes:{info_implantes}"
        else:
            return f"Nombre: {self.__nombre}, Cédula: {self.__cedula}, Edad: {self.__edad}, Este paciente no tiene prótesis asignadas."

    def seguimiento_implante(self, fecha_revision, estado):
        if self.__implantes:
            for implante_info in self.__implantes:
                print(f"\nEl paciente tiene asignado el implante '{implante_info['implante'].ver_nombre()}'.\n"
                    f"Fecha de implantación: {implante_info['fecha_implantacion']}\n"
                    f"Estado actual: {estado}\nFecha de revisión: {fecha_revision}")
        else:
            print("El paciente no tiene asignado un implante.")

# class Protesis_asignadas:
    

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

    def ingresar_paciente(self, paciente):
        self.__lista_pacientes.append(paciente)

    def eliminar_protesis(self, protesis):
        for lista in [self.__lista_marcapasos, self.__lista_stent_coronario, self.__lista_implante_dental,
                    self.__lista_imp_rodilla, self.__lista_imp_cadera]:
            if protesis in lista:
                lista.remove(protesis)

    def editar_protesis(self, nombre_protesis, atributo, nuevo_valor):
        for lista in [self.__lista_marcapasos, self.__lista_stent_coronario, self.__lista_implante_dental,
                    self.__lista_imp_rodilla, self.__lista_imp_cadera]:
            for protesis in lista:
                if protesis.ver_nombre() == nombre_protesis:
                    setattr(protesis, atributo, nuevo_valor)
                    print(f"Edición exitosa. Nuevo valor para '{atributo}': {nuevo_valor}")
                    return
        print(f"Prótesis '{nombre_protesis}' no encontrada.")

    def ver_pacientes(self):
        return self.__lista_pacientes

    def hacer_seguimiento_paciente(self, nombre_paciente):
        for paciente in self.__lista_pacientes:
            if paciente.ver_nombre() == nombre_paciente:
                print("-" * 30)
                print(f"Seguimiento del paciente {nombre_paciente}")
                print("-" * 30)
                print(f"Cédula: {paciente.ver_cedula()}")
                print(f"Edad: {paciente.ver_edad()} años")

                implantes_paciente = paciente.ver_nombre()
                if implantes_paciente:
                    print("\nPrótesis asignadas:")
                    for implante, fecha_implantacion in paciente.ver_implantes():
                        print(f"Nombre: {implante.ver_implantes()}, Fecha de implantación: {fecha_implantacion}")
                else:
                    print("\nEste paciente no tiene prótesis asignadas.")
                print("-" * 30)
                return

        print(f"Paciente '{nombre_paciente}' no encontrado.") 

    


def main():
    sistema = Sistema()
    print("-" * 30)
    print("Bienvenido al sistema de gestión de inventarios de prótesis")
    print("-" * 30)

    while True:
        try:
            # MENÚ
            print("¿Qué desea hacer?\n")
            print("1. Agregar nuevo implante\n2. Eliminar\n3. Editar\n4. Visualizar\n5. Asignación de prótesis a paciente\n6. Seguimiento")
            inicio = int(input("Ingrese una opción: "))

            # AGREGAR NUEVA PRÓTESIS
            if inicio == 1:
                print("-" * 30)
                print("¿Qué tipo de prótesis desea agregar?")
                print("-" * 30)
                print("1. Marcapasos\n2. Stent coronario\n3. Implante dental\n4. Implante de rodilla\n5. Implante de cadera\n")
                entrada = int(input("Ingrese una opción: "))

                if entrada in range(1, 6):
                    nombre = input("Nombre de la prótesis: ")

                    if entrada == 1:
                        num_electrodos = int(input("Número de electrodos: "))
                        alambrico_inalambrico = input("Alámbrico o inalámbrico: ")
                        frec_estimu = float(input("Frecuencia de estimulación: "))

                        marcapasos = Marcapasos()
                        marcapasos.asignar_nombre(nombre)
                        marcapasos.asignar_num_electrodos(num_electrodos)
                        marcapasos.asignar_almbrico_o_inalambrico(alambrico_inalambrico)
                        marcapasos.asignar_frecuencia_estimulacion(frec_estimu)

                        sistema.ingresar_marcapasos(marcapasos)
                        print("¡Registro Exitoso!")

                    elif entrada == 2:
                        longitud = float(input("Longitud: "))
                        diametro = float(input("Diámetro: "))
                        material = input("Material: ")

                        stent = StentCoronario()
                        stent.asignar_nombre(nombre)
                        stent.asignar_longitud(longitud)
                        stent.asignar_diametro(diametro)
                        stent.asignar_material(material)

                        sistema.ingresar_stent_coronario(stent)
                        print("¡Registro Exitoso!")

                    elif entrada == 3:
                        forma = input("Forma: ")
                        sis_fijacion = input("Sistema de fijación: ")
                        material = input("Material: ")

                        imp_dental = ImplanteDental()
                        imp_dental.asignar_nombre(nombre)
                        imp_dental.asignar_forma(forma)
                        imp_dental.asignar_sis_fijacion(sis_fijacion)
                        imp_dental.asignar_material(material)

                        sistema.ingresar_implante_dental(imp_dental)
                        print("¡Registro Exitoso!")

                    elif entrada == 4:
                        material = input("Material: ")
                        tipo_fijacion = input("Tipo de fijación: ")
                        tamaño = float(input("Tamaño: "))

                        imp_rodilla = ImplanteRodilla()
                        imp_rodilla.asignar_nombre(nombre)
                        imp_rodilla.asignar_material(material)
                        imp_rodilla.asignar_tipo_fijacion(tipo_fijacion)
                        imp_rodilla.asignar_tamaño(tamaño)

                        sistema.ingresar_implante_rodilla(imp_rodilla)
                        print("¡Registro Exitoso!")

                    elif entrada == 5:
                        material = input("Material: ")
                        tipo_fijacion = input("Tipo de fijación: ")
                        tamaño = float(input("Tamaño: "))

                        imp_cadera = ImplanteCadera()
                        imp_cadera.asignar_nombre(nombre)
                        imp_cadera.asignar_material(material)
                        imp_cadera.asignar_tipo_fijacion(tipo_fijacion)
                        imp_cadera.asignar_tamaño(tamaño)

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
                    nuevo_valor = input(f"Ingrese el nuevo valor para '{atributo}': ")

                    sistema.editar_protesis(nombre_protesis, atributo, nuevo_valor)

                else:
                    print("Opción no válida. Intente de nuevo.")

            # VISUALIZAR INVENTARIO
            elif inicio == 4:
                print("-" * 30)
                print("Inventario completo:")
                for marcapasos in sistema.ver_marcapasos():
                    print(f"Tipo: Marcapasos, Nombre: {marcapasos.ver_nombre()}, Electrodos: {marcapasos.ver_num_electrodos()}, "
                        f"Alámbrico/Inalámbrico: {marcapasos.ver_almbrico_o_inalambrico()}, Frecuencia: {marcapasos.ver_frecuencia_estimulacion()}")

                for stent in sistema.ver_stent_coronario():
                    print(f"Tipo: Stent Coronario, Nombre: {stent.ver_nombre()}, Longitud: {stent.ver_longitud()}, "
                        f"Diametro: {stent.ver_diametro()}, Material: {stent.ver_material()}")

                for imp_dental in sistema.ver_implante_dental():
                    print(f"Tipo: Implante Dental, Nombre: {imp_dental.ver_nombre()}, Forma: {imp_dental.ver_forma()}, "
                        f"Sistema de Fijación: {imp_dental.ver_sis_fijacion()}, Material: {imp_dental.ver_material()}")

                for imp_rodilla in sistema.ver_implante_rodilla():
                    print(f"Tipo: Implante de Rodilla, Nombre: {imp_rodilla.ver_nombre()}, Material: {imp_rodilla.ver_material()}, "
                        f"Tipo de Fijación: {imp_rodilla.ver_tipo_fijacion()}, Tamaño: {imp_rodilla.ver_tamaño()}")

                for imp_cadera in sistema.ver_implante_cadera():
                    print(f"Tipo: Implante de Cadera, Nombre: {imp_cadera.ver_nombre()}, Material: {imp_cadera.ver_material()}, "
                        f"Tipo de Fijación: {imp_cadera.ver_tipo_fijacion()}, Tamaño: {imp_cadera.ver_tamaño()}")

                print("-" * 30)

            # ASIGNACIÓN DE PRÓTESIS A PACIENTE
            elif inicio == 5:
                print("-" * 30)
                print("Crear Paciente y Asignar Prótesis")
                print("-" * 30)

                nombre_paciente = input("Ingrese el nombre del paciente: ")
                cedula_paciente = int(input("Ingrese la cédula del paciente: "))
                edad_paciente = int(input("Ingrese la edad del paciente: "))

                # Crear un nuevo objeto de paciente
                nuevo_paciente = Paciente()
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
                            
            elif inicio == 6:
                print("-" * 30)
                print("Seguimiento de Pacientes")
                print("-" * 30)

                nombre_paciente_seguimiento = input("Ingrese el nombre del paciente: ")
                for paciente in sistema.ver_pacientes():
                    if paciente.ver_nombre() == nombre_paciente_seguimiento:
                        paciente.seguimiento_implante(datetime.now().strftime("%Y/%m/%d"), "En buen estado")
                        break
                else:
                    print(f"Paciente '{nombre_paciente_seguimiento}' no encontrado.")

        except ValueError:
            print("Error: Ingrese un valor válido")


if __name__ == "__main__":
    main()
