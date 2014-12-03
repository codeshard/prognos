prognos-qt
========
Prognos*(del griego prognostikon)* es una aplicación para monitorear el estado del tiempo en Cuba, usando como orígenes de datos la web del [Instituto de Meteorología de la República de Cuba](www.met.inf.cu).

####Requerimientos
python-lxml  
python-qt4
python-urllib2

####Características
 - Icono de la bandeja y de la ventana se actualizan en dependencia del estado del tiempo.
- Muestra la temperatura en grados Celcius, Fahrenheit y Kelvin(para llenar funcionalidades porque esto no sirve de nada).
- Autenticación mediante proxy(por ahora solamente esta funcionalidad, ya que en nuestra gran mayoría salimos usando proxys).

####Modo de uso
Ejecutar ```python setup.py install``` como **root**.

####TODO
- Validación de la red.
- Systray funcional.
- Guardar tokens de autenticación cifrados.
- Actualización automática de los datos(por ahora solo de forma manual).
- Internacionalización(nada más es para Cuba, pero siempre alguien lo quiere usar en inglés u otro idioma).