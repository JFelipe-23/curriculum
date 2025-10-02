# Sistema de Gestión de Currículums Vitae

Sistema web desarrollado con Flask para la gestión de currículums vitae (CV) que permite a los usuarios crear, editar y visualizar sus hojas de vida en línea.

## Características Principales

- Sistema completo de autenticación de usuarios
- Gestión de CV con información personal, experiencia, educación y habilidades
- API REST para acceso a los datos
- Interfaz de usuario intuitiva y responsive

## Tecnologías Utilizadas

- **Framework:** Flask 3.1.2+
- **Autenticación:** Flask-Login 0.6.3+
- **Formularios:** Flask-WTF 1.2.2+
- **Validación de correo:** email-validator 2.3.0+
- **Frontend:** HTML, CSS, Material Icons, Font Awesome

## Estructura del Proyecto

```
src/
└── curriculum/
    ├── __init__.py
    ├── forms.py      # Definición de formularios
    ├── models.py     # Modelos de datos
    ├── run.py        # Aplicación principal y rutas
    ├── static/       # Archivos estáticos (CSS)
    └── templates/    # Plantillas HTML
        ├── admin/    # Plantillas administrativas
        └── ...       # Otras plantillas
```

## Funcionalidades

### Gestión de Usuarios
- Registro de nuevos usuarios
- Inicio de sesión
- Cierre de sesión
- Sistema de autenticación seguro

### Gestión de CVs
- Creación de CV
- Edición de CV existente
- Visualización de CV
- Listado de todos los CVs
- API REST para acceso a los datos

### Estructura del CV
- Información personal
  - Nombre completo
  - Título profesional
  - Sección "Sobre mí"
- Experiencia laboral
  - Empresa
  - Cargo
  - Fechas de inicio y fin
- Educación
  - Institución
  - Título
  - Fechas de inicio y fin
- Habilidades
  - Nombre de la habilidad
  - Nivel de dominio (1-5)

## API REST

### Endpoints disponibles:
- GET `/api/cvs`: Lista todos los CVs
- GET `/api/cvs/<id>`: Obtiene un CV específico

## Seguridad

- Hasheo de contraseñas
- Protección CSRF en formularios
- Sistema de autenticación robusto
- Validación de datos en formularios

## Reglas de Negocio

- Un usuario solo puede tener un CV
- Se requiere autenticación para crear/editar CVs
- Validación de campos obligatorios
- Formato específico para fechas
- Niveles de habilidad del 1 al 5

## Requisitos

- Python >= 3.8
- Dependencias listadas en pyproject.toml

## Instalación

1. Clonar el repositorio
2. Instalar las dependencias:
   ```bash
   pip install .
   ```

## Uso

1. Iniciar la aplicación:
   ```bash
   python -m src.curriculum.run
   ```
2. Abrir el navegador en `http://localhost:5000`

## Desarrollo

El proyecto utiliza Rye para la gestión de dependencias y Hatchling como backend de construcción.
