# Tarea2AlfaroGonzalezHernandezRomero
Segunda tarea del curso de Microprocesadores y Microcontroladores, TEC, carre Mecatronica, Primer semestre 2019


GitHub

“En un nivel más alto, GitHub es un sitio web y un servicio en la nube que ayuda a los desarrolladores a almacenar y administrar su código, al igual que llevar un registro y control de cualquier cambio sobre este código.

Una Versión de Control ayuda a los desarrolladores llevar un registro y administrar cualquier cambio en el código del proyecto de software.

Específicamente, Git es un sistema de control de versión distribuida, lo que quiere decir que la base del código entero y su historial se encuentran disponibles en la computadora de todo desarrollador, lo cual permite un fácil acceso a las bifurcaciones y fusiones.

Git no almacena los datos de forma incremental (guardando sólo diferencias), sino que los almacena como una serie de instantáneas (copias puntuales de los archivos completos, tal y como se encuentran en ese momento).” [1].

Branch (Rama)

“Una rama Git es simplemente un apuntador móvil apuntando a una de esas confirmaciones. La rama por defecto de Git es la rama master. Con la primera confirmación de cambios que realicemos, se creará esta rama principal master apuntando a dicha confirmación. En cada confirmación de cambios que realicemos, la rama irá avanzando automáticamente. Y la rama master apuntará siempre a la última confirmación realizada.”[2].


En conclusión un branch o rama es una bifurcación, a partir de una rama de código, que se abre a otra para poder aplicar cambios sin afectar al resto.

Commit

“Un "commit" es la acción de guardar o subir tus archivos a tu repositorio remoto.
Indica al administrador de transacciones que una unidad de trabajo lógica ha concluido satisfactoriamente, que la base de datos está o debería estar nuevamente en un estado consistente.”[3].

En definitiva, se refiere a cuando “una transacción ha completado su ejecución con éxito, o sea, ingresa en el estado committed o confirmado.
Confirmado significa que los datos están almacenados de manera segura en tu base de datos local”.[4]. 

Staged

“Git tiene tres estados principales en los que se pueden encontrar tus archivos: confirmado (committed), modificado (modified), y preparado (staged). Donde Staged o preparado significa que has marcado un archivo modificado en su versión actual para que vaya en tu próxima confirmación.
El área de preparación es un sencillo archivo, generalmente contenido en tu directorio de Git, que almacena información acerca de lo que va a ir en tu próxima confirmación. A veces se le denomina índice, pero se está convirtiendo en estándar el referirse a ella como el área de preparación.”[5].


Git checkout

“El comando checkout se puede usar para crear ramas o cambiar entre ellas. Por ejemplo, el siguiente comando crea una nueva y se cambia a ella:” [6].
command git checkout -b <banch-name>
Para cambiar de una rama a otra solo usa:
git checkout <branch-name>

Git Stash

“Este es uno de los comandos menos conocidos, pero ayuda a salvar cambios que no están por ser comprometidos inmediatamente, pero si temporalmente.”[6].

“Este comando de guardado rápido (stashing) toma el estado del espacio de trabajo, con todas las modificaciones en los archivos bajo control de cambios, y lo guarda en una pila provisional. Desde allí, se podrán recuperar posteriormente y volverlas a aplicar de nuevo sobre el espacio de trabajo.”[7].

https://www.hostinger.es/tutoriales/comandos-de-git

Git Add

“Este comando puede ser usado para agregar archivos al index. Por ejemplo, el siguiente comando agrega un nombre de archivo temp.txt en el directorio local del index:[6].
git add temp.txt

Pytest

Pytest es una librería de testing para Python.
En Python se describe como: 
“El framework pytest facilita la escritura de pruebas pequeñas, pero se adapta para soportar pruebas funcionales complejas para aplicaciones y bibliotecas”
Pytest se puede utilizar para ejecutar doctests y unittests.

Assert

“Las aserciones son verificaciones que devuelven el estado Verdadero o Falso. En pytest, si una afirmación falla en un método de prueba, entonces la ejecución del método se detiene allí. El código restante en ese método de prueba no se ejecuta, y pytest continuará con el siguiente método de prueba.”[10].

Flake 8

“Mantener la uniformidad del código es un punto importante a considerar sobre todo cuando se trabaja en equipo, asi también para mantener un código legible.
Se recomienda usar la guía PEP8 (ahora llamada pycodestyle) la cual tiene una serie de reglas sobre como escribir código python, por ejemplo usar underscorecase para definir variables, funciones, etc o el orden de importación de módulos entre otras.
flake8 nos permite, además de revisar que se cumpla la PEP8, revisar si existen variables declaradas pero no usadas, imports que no se usan, etc. Lo cual permite que el código resultante sea más limpio” [11].

“Flake8 es una biblioteca de Python que envuelve el script McCabe de PyFlakes, pycodestyle y Ned Batchelder. Es un excelente conjunto de herramientas para verificar su base de código en comparación con el estilo de codificación (PEP8), errores de programación (como "biblioteca importada pero no utilizada" y "nombre no definido") y para verificar la complejidad ciclomática” [12].

Referencias

[1] Kinsta (Agosto, 2018). ¿Qué es GitHub? Una Guía para Principiantes sobre GitHub. https://kinsta.com/es/base-de-conocimiento/que-es-github/
[2] Git. Ramificaciones en Git - ¿Qué es una rama? https://git-scm.com/book/es/v1/Ramificaciones-en-Git-%C2%BFQu%C3%A9-es-una-rama%3F
[3] Pantal, D. Commits - Administrar Tu Repositorio. https://codigofacilito.com/articulos/commits-administrar-tu-repositorio
[4] GlosarioIT. Commit - Sección BD/Programación. https://www.glosarioit.com/Commit
[5] Git. Empezando - Fundamentos de Git
 https://git-scm.com/book/es/v1/Empezando-Fundamentos-de-Git
[6] Gustavo B. (Noviembre 2018). Comandos básicos de GIT. https://www.hostinger.es/tutoriales/comandos-de-git
[7] Git. Las herramientas de Git - Guardado rápido provisional. https://git-scm.com/book/es/v1/Las-herramientas-de-Git-Guardado-r%C3%A1pido-provisional
[8] The Mushroom (Marzo 2017). Desarrollo dirigido por pruebas – Python y Pytest
http://laesporadelhongo.com/desarrollo-dirigido-por-pruebas-python-pytest/
[9] Brian (Enero 2013). Pytest introduction. http://pythontesting.net/framework/pytest/pytest-introduction/
[10] Guru99. PyTest Tutorial: What is, Install, Fixture, Assertions. https://www.guru99.com/pytest-tutorial.html
[11] Gal I (Enero, 2017). What is Flake8 and why we should use it?. https://medium.com/python-pandemonium/what-is-flake8-and-why-we-should-use-it-b89bd78073f2
[12] Feitas V (Agosto, 2016). How to Use Flake8. https://simpleisbetterthancomplex.com/packages/2016/08/05/flake8.html
