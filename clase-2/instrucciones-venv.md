#Instrucciones creación venv

## 1. Crear un venv

Ubicarse en la carpeta de tu proyecto:

```bash
cd mi_proyecto
```

Crear el entorno virtual

```bash
python -m venv <nombre del proyecto>
```
Ejemplo
```
python -m venv venv
```

## 2. Activar el venv
### Windows

```bash
venv\Scripts\activate
```
### macOS / Linux

```bash
source venv/bin/activate
```

## 3. Instalar algunas librería de prueba

```bash
pip install easy_date
```

```bash
pip install cowsay
```


## 4. Ver librerías instaladas

```bash
pip list
```

## 5. Correr el archivo de ejemplo
```bash
python ejemplo-venv.py 
```

## 6. Persistir las librerías instaladas
Crear archivo requirements.txt:

```bash
pip freeze > requirements.txt
```

## 7. Salir o desactivar el ambiente

```bash
deactivate
```

## 8. Si desea volver a activar el ambiente e instalas las dependencias
### Windows

```bash
venv\Scripts\activate
```
### macOS / Linux

```bash
source venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```
