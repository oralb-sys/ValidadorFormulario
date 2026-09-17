ValidadorFormulario

Proyecto académico desarrollado para el curso Tópicos Avanzados de Construcción de Software. El objetivo es implementar un validador de formulario en Python y aplicar una estrategia de aseguramiento de calidad mediante pruebas unitarias, pruebas de integración, cobertura de código y automatización CI con GitHub Actions.

Repositorio: https://github.com/oralb-sys/ValidadorFormulario

1. Objetivo

El proyecto valida tres datos principales de un formulario de registro:

Correo electrónico.

Contraseña.

DNI.

Además, integra las validaciones mediante un servicio de registro de usuario. La práctica busca comprobar tanto la lógica aislada como el comportamiento conjunto de los validadores.

2. Estructura del proyecto

ValidadorFormulario/
│
├── src/
│   ├── __init__.py
│   ├── validators.py
│   └── registration_service.py
│
├── tests/
│   ├── __init__.py
│   ├── test_validators.py
│   └── test_registration_service.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md

3. Tecnologías utilizadas

Python 3.12

pytest

pytest-cov

Git

GitHub

GitHub Actions

4. Instalación

Clonar el repositorio:

git clone https://github.com/oralb-sys/ValidadorFormulario.git
cd ValidadorFormulario

Crear un entorno virtual:

python -m venv .venv

Activarlo en PowerShell:

.venv\Scripts\Activate.ps1

Instalar las dependencias:

pip install -r requirements.txt

5. Funcionalidades implementadas

Validación de correo electrónico

Comprueba que el valor ingresado siga una estructura válida de correo electrónico y rechaza valores vacíos o con formato incorrecto.

Validación de contraseña

Comprueba que la contraseña:

No sea vacía.

Tenga al menos 8 caracteres.

Contenga una letra mayúscula.

Contenga una letra minúscula.

Contenga al menos un número.

Validación de DNI

Comprueba que el DNI:

No sea vacío.

Contenga únicamente dígitos.

Tenga exactamente 8 caracteres.

Registro de usuario

El servicio register_user() integra las validaciones anteriores. Si alguno de los datos es inválido, genera una excepción; si todos son correctos, devuelve un usuario con estado registered.

6. Pruebas unitarias

Las pruebas unitarias se encuentran en:

tests/test_validators.py

Se verifican casos válidos e inválidos para correo electrónico, contraseña y DNI.

Para ejecutar las pruebas:

python -m pytest

7. Pruebas de integración

Las pruebas de integración se encuentran en:

tests/test_registration_service.py

Estas pruebas comprueban el flujo completo de registro y verifican escenarios como:

Registro exitoso.

Nombre faltante.

Correo inválido.

Contraseña inválida.

DNI inválido.

8. Cobertura de código

La cobertura se mide con pytest-cov:

python -m pytest --cov=src --cov-report=term-missing

Resultado verificado en la etapa actual:

Name                          Stmts   Miss  Cover
-------------------------------------------------
src/__init__.py                   0      0   100%
src/registration_service.py      11      0   100%
src/validators.py                19      1    95%
-------------------------------------------------
TOTAL                            30      1    97%

17 passed

El proyecto supera el umbral mínimo de cobertura del 90 %.

Para exigir automáticamente dicho umbral:

python -m pytest --cov=src --cov-report=term-missing --cov-fail-under=90

9. Integración continua con GitHub Actions

El workflow se encuentra en:

.github/workflows/ci.yml

Se ejecuta automáticamente ante un push o pull request hacia la rama main.

El flujo implementado es:

Push / Pull Request
        │
        ▼
Checkout del repositorio
        │
        ▼
Configuración de Python
        │
        ▼
Instalación de dependencias
        │
        ▼
Ejecución de pruebas
        │
        ▼
Validación de cobertura >= 90 %
        │
        ▼
Pipeline exitoso

El workflow ha sido ejecutado satisfactoriamente en GitHub Actions.

10. Estado actual

Estructura inicial del proyecto.

Validadores de email, contraseña y DNI.

Servicio de registro de usuario.

Pruebas unitarias.

Pruebas de integración.

Cobertura medida con pytest-cov.

Cobertura total verificada: 97 %.

Umbral mínimo de cobertura: 90 %.

Integración continua con GitHub Actions.

Contenerización con Docker.

Publicación automática de imagen en Docker Hub.

Etapa CD completa.

11. Próximos pasos

La siguiente etapa del proyecto consiste en completar el flujo CI/CD mediante:

Creación de un Dockerfile.

Construcción y validación local de la imagen Docker.

Creación del repositorio en Docker Hub.

Configuración de secretos en GitHub Actions.

Incorporación de docker/login-action.

Incorporación de docker/build-push-action.

Publicación automática de la imagen únicamente cuando las pruebas y la cobertura sean satisfactorias.

12. Licencia y finalidad

Proyecto elaborado con fines académicos para demostrar prácticas de pruebas automatizadas, cobertura de código e integración/entrega continua.