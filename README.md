prognos-qt
========
[Prognos](http://codeshard.github.io/prognos)*(del griego prognostikon)* es una aplicación para monitorear el estado del tiempo en Cuba, usando como orígenes de datos la web del [Instituto de Meteorología de la República de Cuba](www.met.inf.cu).
Prognos está inspirado en [meteo-qt](https://github.com/dglent/meteo-qt)

####Requerimientos
 - python-lxml
 - python-qt4
 - python-urllib2

####Características
- Icono de la bandeja y de la ventana se actualizan en dependencia del estado del tiempo.
- Muestra la temperatura en grados Celcius, Fahrenheit y Kelvin.
- Autenticación mediante proxy(por ahora solamente esta funcionalidad, ya que en nuestra gran mayoría salimos usando proxys).
- Actualiza el pronóstico de la temperatura en dependencia de la hora del día.
- Historial de pronóstico guardado en una base de datos(sqlite3).
- Ventana emergente con pronóstico extendido.(aproximadamente 5 días).

####Modo de uso
Ejecutar ```python setup.py install``` como **root**.

####Historial de cambios
- Los datos son guardados en una base de datos y solo encuestará el sitio del InsMet en caso de que sea necesario.
- Corregidos los errores en Unicode.
- Añadido diálogo de pronóstico extendido.
- Añadidas nuevas escalas de temperatura.
- Añadido tooltip en el icono de la bandeja del sistema.
- Algunos errores corregidos y pequeñas optimizaciones.
- Eliminado selección de lenguaje(provisional).
