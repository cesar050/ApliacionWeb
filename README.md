# botzilla_back
![image](https://github.com/cesar050/ApliacionWeb/assets/166522713/aa96e1cf-e735-4be6-b38a-981fe3d005a6)

# Redaccion: Casos de Uso
### El diagrama UML presentado detalla la estructura de un sistema que implica la interacción entre usuarios, gestión de objetos, control de un brazo robótico y la generación de reportes. A continuación, se describen detalladamente los casos de uso para cada uno de los componentes y relaciones en el diagrama:
## 1. InterfazUsuario

1. 	nombre: String
2.	email: String
## Métodos:
1. 	iniciarSesion(): Permite al usuario iniciar sesión en el sistema.
2.	cerrarSesion(): Permite al usuario cerrar sesión.
3. autentificacion(): Verifica las credenciales del usuario.
4. modificarInformacion(): Permite al usuario modificar su información personal.
## PerfilUsuario
1.	direccion: String
2.horaInicio: Date
3. horaFin: Date
## Métodos:
1.	mostrarInformacion(): Muestra la información del perfil del usuario.
## GestionNotificaciones
## Métodos:
1.mostrarNotificacion(): Muestra notificaciones al usuario.
2. eliminarNotificacion(): Permite al usuario eliminar notificaciones.
## AdministracionUsuario
## Métodos:
1. crearUsuario(): Crea un nuevo usuario.
2. eliminarUsuario(): Elimina un usuario existente.
3. modificarUsuario(): Modifica la información de un usuario.
## HistorialActividad
## Métodos:
1. objetoRecoletado(): Registra cuando un objeto ha sido recolectado.
2. movimientoRealizado(): Registra los movimientos realizados por el usuario o el sistema.
3. tiempoConectado(): Registra el tiempo de conexión del usuario.
## Navegación (Interfaz)
## Métodos:
1. verDatosRecolectados(): Muestra los datos recolectados.
2. verVideo(): Permite al usuario ver videos relacionados.
3. mensajesEstado(): Muestra mensajes de estado del sistema.
4. verMateriales(): Permite al usuario ver los materiales disponibles.
### 2. BrazoRobotico
## Señal
1. remoto: void
2. video: void
3. resolucion: void
## Esp32cam
## Métodos:
1. recibirSeñal(): Recibe y procesa señales de la cámara ESP32.
### ControlBrazoYCarro
## Métodos:
1. moverBrazo(): Controla el movimiento del brazo robótico.
2. abrirPinza(): Abre la pinza del brazo robótico.
3. cerrarPinza(): Cierra la pinza del brazo robótico.
###  3. Datos
## Objeto
## Métodos:
1. almacenarObjeto(): Permite almacenar información sobre un objeto.
2. modificarObjeto(): Permite modificar la información de un objeto.
3. mostrarInformacionObjeto(): Muestra la información de un objeto.
## Reporte
## Métodos:
1. generarReporte(): Genera un reporte sobre los objetos y actividades.
2. exportarReporte(): Exporta el reporte generado a un formato adecuado.
## InformacionObjeto
## Métodos:
1. calcularPesoObjeto(): Calcula el peso del objeto basado en una gráfica estadística.
### 4. ClasificacionObjeto
## Este es un enumerado que clasifica los tipos de objetos en:
1. PELIGROSO
2. CORROSIVO
3. INFLAMABLE
4. ORGANICO
5. INORGANICO
6. QUIRURGICO
## Relaciones Importantes:
1. Un Usuario puede tener múltiples PerfilUsuario.
2. GestionNotificaciones gestiona múltiples notificaciones por usuario.
3. HistorialActividad registra actividades relacionadas con los usuarios.
4. ControlBrazoYCarro controla el brazo robótico y la cámara ESP32.
5. Los Objetos pueden ser clasificados y se almacenan con información específica.
6. Los Reportes se generan y exportan para analizar datos sobre los objetos.

En conjunto, estos componentes colaboran para ofrecer una solución integral que combina gestión de usuarios, control robótico y análisis de datos en un sistema coherente y funcional.










