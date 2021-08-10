AITSolutions Django-DRF Skill Test
===========================


### Aplicacion
La aplicacion TODOREMINDER permite a un usuario agregar tareas que debe hacer. Aqui se encuentran los 
requerimientos.
* Un usuario puede agregar, eliminar y consultar sus tareas.
* Las tareas son privadas, un usuario no puede consultar, eliminar o agregar tareas a otros usuarios.
* Un usuario debe estar autenticado para poder agregar/eliminar/consultar tareas.

### Requisitos
* python 3.8
* virtualenv
* sqlite3
* Cuenta en github

### Instalacion de entorno
**⚠ Necesitar crear un fork a partir de este repositorio.** Ver [Como enviar tu trabajo?](#Como enviar tu trabajo?)
```sh
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver 0:8000
```

### Instrucciones
Se te pedira que mejores el codigo de esta aplicacion para que cumpla con los requerimientos antes mencionados,
ademas de implementar las siguientes tareas.

Podes completarlas en el orden que desees.

Separa tus commits por tareas utillizando el siguiente formato para tus mensajes de commit: TASK-{nro. de tarea}: {mensaje}

### Tareas
* TASK 1: Como usuario no puedo agregar una tarea sin descripcion.
* TASK 2: Como usuario puedo marcar una tarea como completada.
* TASK 3: Como usuario puedo consultar una tarea en formato JSON.
    - Ej: /todos/{id} => {id: 1, user_id: 1, title: "Lorem", description: "Lorem Ipsum"}
* TASK 5: Como usuario puedo consultar una lista con todas mis tareas.
    - Considerar ordenamiento por fecha de registro de la más reciente a la más antigua.
* TASK 6: Implementar una capa de acceso a datos separada de las vistas (views.py).

Actividades extra (no obligatorias):
* OP-TASK 1: Paginar los resultados de la TASK-5
* 

### Documentacion
 - Esta aplicacion utiliza [Django 3.2](https://docs.djangoproject.com/en/3.2/releases/3.2/).
 - Se recomienda seguir la [hoja de estilos](https://github.com/HackSoftware/Django-Styleguide) de HackSoft

### ¿Como enviar tu trabajo?

1. Primero debes crear un fork de este repositorio.

2. Luego clona tu fork localmente.

3. Instala tu aplicacion localmente. Ver la [Guia de instalacion](#Instalacion de entorno).

4. Una vez completado tu trabajo, puedes enviar una pull-request a este repositorio.

5. Revisa tus cambios y valida tu pull-request.

Y listo!


Mas documentacion en Github:
* https://help.github.com/articles/fork-a-repo/
* https://help.github.com/articles/using-pull-requests/
