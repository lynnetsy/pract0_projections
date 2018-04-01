# Instalación

## Windows

### Instalar python

* Descargar python 2.7 desde el [sitio oficial](https://www.python.org/downloads/)
* Ejecutar el archivo descargado
* Seguir las instrucciones de instalación 
* Agregar la ruta de instalación de python (C://Python27) a las variables de entorno de windows

### Instalar pip

* Descargar el archivo de instalacion desde [aquí](https://bootstrap.pypa.io/get-pip.py)
* Desde el cmd ir a la ruta donde se descargó el archivo por ejemplo: 
```$ cd Downloads```
* Ejecutar el archivo desde cmd:
```$ python get-pip.py```
* Agregar la ruta de instalación (C:\Python27\Scripts) a las variables de entorno de windows

### Instalar librerias

#### Numpy

* Instalar numpy con pip
```$ pip install numpy```

#### Matplotlib

* Instalar Microsoft Visual C++ 2008
	* [Para windows de 32bits](https://www.microsoft.com/en-us/download/details.aspx?id=29)
	* [Para windows de 64bits](https://www.microsoft.com/en-us/download/details.aspx?id=15336)
* Instalar matplotlib usando pip
```$ pip install matplotlib```

#### Basemap

* Descargar desde [http://www.lfd.uci.edu/~gohlke/pythonlibs/](http://www.lfd.uci.edu/~gohlke/pythonlibs/) el archivo 
	* basemap-1.1.0-cp27-cp27m-win32.whl para windows de 32 bits
	* basemap-1.1.0-cp27-cp27m-win_amd64.whl para windows de 64bits
* Mover el archivo descargado a la carpeta de instalación de python (C://Python27)
* Desde la terminal instalar con pip:
```$ pip install basemap-1.1.0-cp27-cp27m-win32.whl```
O
```$ pip install basemap-1.1.0-cp27-cp27m-win_amd64.whl```

[Webgrafía](https://stackoverflow.com/questions/18109859/how-to-install-matplotlib-basemap-module-on-windows-7-with-winpython-or-any-pyt)
