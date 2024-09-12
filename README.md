Aquí tienes el **README** para tu proyecto de **Tienda de Ropa** utilizando microservicios.

---

# Tienda de Ropa - Microservicios

Este proyecto implementa una arquitectura de microservicios para gestionar una tienda de ropa. El sistema se divide en dos microservicios independientes: uno para la **gestión de productos de ropa** y otro para la **gestión de pedidos**. Cada microservicio tiene su propia base de datos y se comunica a través de **APIs RESTful**.

## Estructura del Proyecto

```
clothing-store/
├── products/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   └── Dockerfile
│   └── requirements.txt
└── orders/
    ├── app/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── routes.py
    └── Dockerfile
    └── requirements.txt
└── docker-compose.yml
```

### Microservicios

1. **Productos de Ropa**:
   - Se encarga de la creación, actualización y consulta de productos de ropa.
   - Utiliza una base de datos PostgreSQL independiente.

2. **Pedidos**:
   - Permite la creación y modificación de pedidos.
   - Se comunica con el microservicio de productos para verificar que los productos existen antes de realizar un pedido.
   - Utiliza su propia base de datos PostgreSQL.

## Endpoints API

### Microservicio de Productos

- **POST** `/products`: Crear un nuevo producto.
  - Parámetros: `name`, `price`, `stock`, `size`
- **GET** `/products/<id>`: Obtener los detalles de un producto por ID.
- **PUT** `/products/<id>`: Actualizar un producto existente.

### Microservicio de Pedidos

- **POST** `/orders`: Crear un nuevo pedido.
  - Parámetros: `product_id`, `quantity`
- **PUT** `/orders/<id>`: Actualizar un pedido existente.

## Requisitos

- **Docker** y **Docker Compose** deben estar instalados en tu máquina.

## Configuración

1. Clona el repositorio:
   ```bash
   git clone <repositorio-url>
   cd clothing-store
   ```

2. Construye y levanta los servicios usando Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Accede a los microservicios:
   - **Productos**: `http://localhost:5001`
   - **Pedidos**: `http://localhost:5002`

## Bases de Datos

Cada microservicio tiene una base de datos PostgreSQL independiente:
- **Productos**: `clothing_products_db`
- **Pedidos**: `clothing_orders_db`

Las credenciales de base de datos se configuran en el archivo `docker-compose.yml` y se almacenan en volúmenes persistentes.

## Comunicación entre Microservicios

El microservicio de **Pedidos** realiza solicitudes HTTP al microservicio de **Productos** para verificar que el producto existe antes de crear o modificar un pedido.

## Manejo de Errores

Se manejan adecuadamente los errores, como:
- Verificar si un producto existe antes de realizar un pedido.
- Validaciones de parámetros.

## Expansión

Este proyecto es escalable, ya que se pueden agregar nuevos microservicios para otras funcionalidades, como gestión de clientes, pagos, entre otros.

---

### Contacto

Si tienes preguntas o problemas, por favor contacta a [fsinsfran.com](mailto:francosebastianinsfran@gmail.com).

---
