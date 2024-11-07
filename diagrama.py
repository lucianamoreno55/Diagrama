from datetime import date
from typing import List

class Consulta:
    def __init__(self, en_linea_o_cita: str, fecha_solicitud: date, cadena_sintomas: str, estado_solicitud: str):
        self.en_linea_o_cita = en_linea_o_cita
        self.fecha_solicitud = fecha_solicitud
        self.cadena_sintomas = cadena_sintomas
        self.estado_solicitud = estado_solicitud
        self.doctor = None  # Relación con Doctor (uno a muchos)
        self.paciente = None  # Relación con Paciente (uno a muchos)


class Paciente:
    def __init__(self, id: str, nombre: str, edad: int, genero: str, email: str, telefono: str, direccion: str):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.consultas: List[Consulta] = []  # Relación con Consulta (uno a muchos)
        
    def crear_perfil_de_paciente(self):
        pass
    
    def editar_perfil_de_paciente(self):
        pass
    
    def eliminar_perfil_de_paciente(self):
        pass
    
    def solicitud_de_consulta(self):
        pass


class Preinscripcion:
    def __init__(self, id_de_prescripcion: int, diagnostico: str, nombre_de_medicina: str, potencia_medicamento: int, 
                 frecuencia_medicamento: int, observaciones: str, prueba_laboratorio: str, laboratorio_de_instrucciones: str, 
                 preinscripcion_entregar: str, solicitudes_de_laboratorio_realizadas: str, monto_de_la_factura: float):
        self.id_de_prescripcion = id_de_prescripcion
        self.diagnostico = diagnostico
        self.nombre_de_medicina = nombre_de_medicina
        self.potencia_medicamento = potencia_medicamento
        self.frecuencia_medicamento = frecuencia_medicamento
        self.observaciones = observaciones
        self.prueba_laboratorio = prueba_laboratorio
        self.laboratorio_de_instrucciones = laboratorio_de_instrucciones
        self.preinscripcion_entregar = preinscripcion_entregar
        self.solicitudes_de_laboratorio_realizadas = solicitudes_de_laboratorio_realizadas
        self.monto_de_la_factura = monto_de_la_factura


class Doctor:
    def __init__(self, id: str, nombre: str, edad: int, genero: str, calificacion: str, experiencia: str, numeroRegistro: str):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.calificacion = calificacion
        self.experiencia = experiencia
        self.numeroRegistro = numeroRegistro
        
    def añadir_medico(self):
        pass
        
    def editar_doctor(self):
        pass
        
    def eliminar_medico(self):
        pass
        
    def proporcionar_consulta(self):
        pass


class Especialista:
    def __init__(self, ssd: str, nombre: str, descripcion: str):
        self.ssd = ssd
        self.nombre = nombre
        self.descripcion = descripcion
        
    def agregar_especialista(self):
        pass
        
    def editar_especialista(self):
        pass
        
    def eliminar_especialista(self):
        pass


class Laboratorio:
    def __init__(self, id: str, nombre: str, direccion: str, email: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
        
    def añadir_laboratorio(self):
        pass
        
    def editar_laboratorio(self):
        pass
        
    def terminar_laboratorio(self):
        pass
        
    def realizar_muestras(self):
        pass
        
    def generar_informe(self):
        pass


class Quimico:
    def __init__(self, id: str, nombre: str, direccion: str, email: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
        
    def añadir_quimico(self):
        pass
        
    def editar_quimico(self):
        pass
        
    def entrega_de_medicamentos(self):
        pass
