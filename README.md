# Sistema_Mercado_Consola

## Descripción
Sistema_Mercado_Consola es una aplicación de consola que administra las operaciones básicas de un negocio pequeño: inventario, contactos, reservas, tareas internas, asistencia del personal y conversión de unidades. El acceso está dividido por roles (Admin, Cajero, Logística y Domiciliario), y cada rol ve solo las opciones que le corresponden.

## Funcionalidades
- **Inventario**: agregar, eliminar, buscar producto, cambiar precio, visualizar.
- **Contactos**: agregar, eliminar, buscar, modificar teléfono/correo, visualizar.
- **Reservas**: agendar, eliminar, visualizar reservas de clientes.
- **Tareas (To-Do)**: el administrador asigna tareas por rol; cada rol ve sus tareas y las marca como completadas.
- **Asistencia**: marcar presente/ausente, ver asistentes, ver ausentes, buscar por nombre.
- **Conversor de unidades**: peso (Kg/Lbs), distancia (Km/Millas), moneda (COP/USD), con historial de conversiones.

## Cómo ejecutar
```bash
python main.py
```
Al iniciar, el sistema pide seleccionar un rol e ingresar la contraseña correspondiente (3 intentos disponibles).

## Tecnologías usadas
- Python 3.10 o superior (se usa la sentencia `match/case`)
- Diccionarios como estructura principal de datos
- No requiere librerías externas