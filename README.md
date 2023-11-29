# Catálogo de Productos API

# Instalacion

Para poder probar correr el siguiente comando 
``` bash
pip install -r requirements.txt
```

## Autenticación y Tokens

Para acceder a los endpoints de la API, se requiere proporcionar un token de autenticación en la cabecera de la solicitud HTTP.

### Tokens Disponibles

- **Token de Administrador**: `myadminsecrettoken`
  - Permite realizar todas las operaciones CRUD en los productos.
- **Token de Solo Lectura**: `myreadonlytoken`
  - Permite únicamente leer información de los productos; no permite crear, actualizar ni eliminar.

## Uso de Tokens

Cada solicitud a la API debe incluir un encabezado `token` con el valor correspondiente al tipo de acceso que se requiera.

### Ejemplos de Uso

#### Crear Producto (Requiere Token de Administrador)

```bash
curl -X POST "http://localhost:8000/products/" -H "Content-Type: application/json" -H "token: myadminsecrettoken" -d '{"sku": "SKU123", "name": "Nombre del Producto", "price": 19.99, "brand": "Marca"}'
```
Obtener Todos los Productos

ADMIN

```bash
curl -X GET "http://localhost:8000/products/" -H "token: myadminsecrettoken"
```
USER

```bash
curl -X GET "http://localhost:8000/products/" -H "token: myreadonlytoken"

```
Actualizar Producto por SKU (Requiere Token de Administrador)

```bash
curl -X PUT "http://localhost:8000/products/SKU123" -H "Content-Type: application/json" -H "token: myadminsecrettoken" -d '{"sku": "SKU123", "name": "Nuevo Nombre", "price": 29.99, "brand": "Nueva Marca"}'

```
Eliminar Producto por SKU (Requiere Token de Administrador)
``` bash
curl -X DELETE "http://localhost:8000/products/SKU123" -H "token: myadminsecrettoken"

```
