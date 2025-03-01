# Enunciado entrega extraordinaria del Laboratorio de Sistemas Distribuidos 24/25

El siguiente documento es el enunciado para la entrega de convocatoria extraordinaria
de la práctica de Sistemas Distribuidos del curso 2024/2025.

## Introducción

Se quiere implementar un servicio de cálculo remoto utilizando _remote method invocation_ usando **ZeroC Ice**.
Para el prototipo, únicamente se considerarán las operaciones aritméticas básicas.

Para garantizar un acceso regulado al servicio, se implementará además un mecanismo de serialización de
operaciones a través de canales de eventos implementados como _topics_ de **Apache Kafka**.

## Requisitos

### Servicio de calculadora

El servicio de calculadora permitirá realizar las operaciones de suma, resta, multiplicación y división, conforme
a lo especificado en la interfaz. Siempre se realizarán las operaciones sobre números reales (punto flotante).

### Serialización de operaciones

Se desarrollará un programa que sea capaz de recibir peticiones de operación a través de un _topic_ de Kafka. Dicho
programa se encargará de:

1. Deserializar la petición recibida conforme al formato especificado más adelante.
2. Si el formato **no es correcto**, se enviará una respuesta de error al _topic_ de respuestas.
3. Si el formato **es correcto**, se enviará una petición al servicio de calculadora, devolviendo el resultado
    a través del _topic_ de respuestas.


## Entregable

La práctica se deberá realizar y almacenar en un repositorio de Git privado. La entega consistirá en enviar
la URL a dicho repositorio, por lo que el alumno deberá asegurarse de que los profesores tengan acceso a
dicho repositorio.

El repositorio deberá contener al menos lo siguiente:

- `README.md` con una explicación mínima de cómo configurar y ejecutar el servicio, así como sus dependencias
    si las hubiera.

- El fichero o ficheros de configuración necesarios para la ejecución.
- Algún sistema de control de dependencias de Python: fichero `pyproject.toml`, `setup.cfg`, `setup.py`, Pipenv,
    Poetry, `requirements.txt`... Su uso debe estar también explicado en el fichero `README.md`

### Fecha de entrega

## Repositorio plantilla

En CampusVirtual se compartirá un repositorio plantilla en GitHub que los alumnos podrán utilizar para crear
su propio repositorio o para clonarlo y comenzar uno nuevo desde "cero".

Dicho repositorio plantilla contiene todos los requisitos especificados en la sección anterior:

- Fichero `README.md`
- Fichero `pyproject.toml` con la configuración del proyecto y de algunas herramientas de evaluación de código.
- El fichero Slice.
- Un paquete Python llamado `remotetpes` con la utilería necesaria para cargar el Slice.
- Módulos dentro de dicho paquete para cada tipo de datos remoto, con la definición del esqueleto de la clase.
- Un módulo `customset.py` con la implementación de un `set` que sólo admite objetos `str` vista en clase.
- Módulo `remoteset.py` con la implementación del objeto `RSet` completa, por lo que sólo sería necesario
    implementar `Rlist`, `RDict`, `Iterable` y `Factory`.
- Módulo `server.py` con la implementación de una `Ice.Application` que permite la ejecución del servicio y añadir
    el objeto factoría existente (en la plantilla, sin implementar sus métodos).
- Módulo `command_handlers.py` con el manejador del comando principal (el equivalente a la función `main`).
- Paquete `tests` con una batería mínima de pruebas unitarias para que sirva de inspiración para realizar más.
- Fichero de configuración necesario para ejecutar el servicio.
- Directorio `.github/workflows` con la definición de algunas "Actions" de la integración continua de GitHub que
    realizan un análisis estático de tipos y de la calidad del código.

Se recomienda encarecidamente utilizar dicha plantilla y leer bien el `README.md` para entender el funcionamiento,
aunque no es obligatorio su uso.
