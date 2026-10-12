Integración de Sistemas ROS 2
Actividad 3: Mensajes, Servicios, Parámetros y Launch
Descripción

Este proyecto simula un sistema de monitoreo de hardware utilizando ROS 2. Está formado por tres nodos que se comunican mediante un mensaje personalizado y un servicio.

Componentes

1. Hardware Emulator

Publica periódicamente información simulada del hardware.
Envía la temperatura, el estado de los motores y un mensaje de depuración.
Utiliza el tópico /hardware_status.

2. Monitor

Recibe los datos publicados por el emulador.
Utiliza el parámetro umbral_temperatura.
Genera advertencias cuando la temperatura supera el umbral.
Ofrece el servicio /check_system para consultar el estado del sistema.

3. Operator

Consulta periódicamente el servicio /check_system.
Muestra si se autoriza el movimiento o si existe un bloqueo.
Mensaje personalizado

El mensaje HardwareStatus contiene:

int64 temperatura
bool motores_listos
string debug_msg
Servicio

Se utiliza el servicio Trigger de std_srvs para consultar el estado del sistema y recibir una respuesta.

Parámetros y Launch

El archivo hardware_system.launch.py permite iniciar los tres nodos y configura el parámetro umbral_temperatura en 75.

Estructura del proyecto
robx7_interfaces/: definición del mensaje personalizado.
hardware_system_pkg/: nodos y configuración del paquete.
hardware_system_pkg/launch/: archivo para iniciar los nodos.
Observación

El código fuente se prepara para ROS 2. La ejecución, las pruebas de comunicación y la generación de evidencias deben realizarse en un entorno con ROS 2 instalado.
