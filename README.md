# Sistema de Supermercado por Roles

Sistema en Python que simula la gestión de un supermercado dividido por roles de usuario: *Administrador, **Cajero, **Logística* y *Domiciliario*. Cada rol tiene su propio inicio de sesión y, una vez dentro, accederá a un menú con funciones específicas para su función dentro del negocio.

## Roles y funcionalidades planeadas

### Administrador
- Editar precios de productos
- Agregar y eliminar productos
- Asignar tareas a los demás roles
- Acceso a todas las funciones de los demás roles

### Cajero
- Conversor de moneda
- Conversor de peso/unidades

### Logística
- Consultar precios y puntos de distribución
- Marcar productos agotados (para generar lista de pedidos)
- Ver qué productos están sobrando

### Domiciliario
- Agenda de reuniones con proveedores
- Gestión de horarios de entrega de domicilios

## Cómo funciona el login (ya implementado)

1. Se muestra un menú y el usuario selecciona su rol ingresando un número.
2. La entrada se valida para asegurar que sea un número válido (try/except).
3. Según el rol elegido, match-case dirige al flujo correspondiente.
4. El usuario tiene 3 intentos para ingresar la contraseña de su rol (validación con for + range).
5. Si acierta, ingresa a la sesión de su rol. Si agota los intentos, se le niega el acceso.

## Estado actual del proyecto

- ✅ Login con selección de rol y validación de contraseña (3 intentos) — funcionando.
- 🔲 Menús y funciones específicas de cada rol — pendientes de implementar.

Próximo paso: separar la lógica de cada rol en funciones (def) para no repetir código dentro de cada case, y a partir de ahí construir cada funcionalidad.

## Conceptos de Python aplicados

- input() y validación de errores con try/except
- Condicionales if/elif/else
- match-case
- Bucles for con range()
- (en construcción) Funciones (def) y separación en módulos

## Cómo ejecutarlo

bash
python main.py


## Autores

Andrés Matoma — Julian Yepes -- proyecto de práctica dentro del Tecnólogo en Desarrollo de Software (SENA).