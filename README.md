# Proyecto Registro

## 1. Descripción
  
  Sistema web que permite que los miembros de una universidad puedan acceder a la gestion online de distintos tramites realizados por estudiantes y profesores.
  
  
## 2.Funciones

  2.1 En el apartado de ESTUDIANTES , se podrán ver los estudiantes registrados en la base de datos. 
  
  ![image](https://user-images.githubusercontent.com/124483470/217140895-dbcfa6a7-5833-4c44-9eef-e250fd50529c.png)

  Tambien se podra dar alta de nuevos estudiante con las bases nombre, apellido, camada y fecha de nacimiento.
  
  ![image](https://user-images.githubusercontent.com/124483470/217141004-65bc369e-bfb4-4dc4-a16e-1b9accbe4e90.png)

  
  2.2 En el apartado de PROFESORES , se podrán ver los profesores registrados en la base de datos.
  
  ![image](https://user-images.githubusercontent.com/124483470/217141246-17fcc728-4fdf-4bd3-9280-63ba3c6323d2.png)

  Tambien se podra dar alta a un nuevo profesor con las bases nombre, apellido, email y su profesion.
  
  ![image](https://user-images.githubusercontent.com/124483470/217141360-c52f2dbd-7cbb-4907-b6da-db812d58071b.png)

  
  2.3 En el apartado de CURSOS, se podrán ver los cursos registrados en la base de datos.
  
  ![image](https://user-images.githubusercontent.com/124483470/217141398-04ddcd8b-0390-4de7-8df9-a846ca6ad97f.png)

  
  Tambien se podra crear un nuevos cursos con las bases nombre del curso, numero de la camada y por ultimo ID del curso.
  
  ![image](https://user-images.githubusercontent.com/124483470/217141430-ee8f73ff-415b-45ae-b582-6cd46f4feb61.png)

  2.4 En el apartado de ENTREGAS , se podrán ver las entregas registradas en la base de datos. 
  
  ![image](https://user-images.githubusercontent.com/124483470/217141483-ebf6a3b3-4cc9-4952-8a8b-9c8e09d63cd7.png)

  
  Tambien se podra registrar una nueva entrega.
  
  ![image](https://user-images.githubusercontent.com/124483470/217141499-f78dd6c1-d556-4657-bc46-7260e01e6492.png)

  
  2.5 Tambien se podra buscar alguna camada guardada en la base de datos
  
  ![image](https://user-images.githubusercontent.com/124483470/217141546-12f20f93-21b6-4f9a-bf28-5fdfc190b1f4.png)
  

  ![image](https://user-images.githubusercontent.com/124483470/217141603-36b4de66-26f0-487a-a0c0-012b3cdff253.png)

 ## 3.Como usar
 
 3.1 Primero descargar en formato .zip el repositorio, y extraerlo.
 
 3.2 Ejecutar Visual Studio Code, y abrir la carpeta extraida.
 
 ![image](https://user-images.githubusercontent.com/124483470/217134066-1e935639-76bd-409d-bc33-e70f3ad688b7.png)

 3.3 Una vez la carpeta ya se encuentre en nuestro editor, abrimos la consola con CRTL + J. 
 En caso de no tener Django instalado tendremos que tipear en el terminar "pip install django" y esperar que se instale.
 Una vez instalado django procedemos a ver en que carpeta estamos situados. 
 
 ![image](https://user-images.githubusercontent.com/124483470/217137030-ca1bab26-ec6f-4e7a-9988-77c943cc1fc6.png)

En caso de no estar situado en la misma carpeta que el archivo "manage.py" tipearemos "cd 'nombre de la carpeta contenedora del manage.py'".

![image](https://user-images.githubusercontent.com/124483470/217137209-2b2d4e50-beed-4be9-b310-668cd299c0b9.png)

![image](https://user-images.githubusercontent.com/124483470/217137294-4e95e5b4-dc6f-4589-a5eb-046d14519ce6.png)


 Cuando estemos en la misma ruta que el manage.py tipearemos en la terminal "python manage.py runserver"
 
 ![image](https://user-images.githubusercontent.com/124483470/217137792-796c6943-aacc-4eab-af1b-6b1fda0e56af.png)

y ya estaremos listo para poder ingresar a la pagina en forma de servidor local con la siguiente ip:

![image](https://user-images.githubusercontent.com/124483470/217138020-94080f26-1dd5-4e53-9d99-cfe291db8e9a.png)

copiaremos la siguiente ip: http://127.0.0.1:8000/AppRegistros/ y la pegaremos en nuestro navegador favorito.

![image](https://user-images.githubusercontent.com/124483470/217139691-c7f851fb-34ed-4340-b235-3d061ac5d5eb.png)


se podra visualizar en ella todas las URL's disponibles de la pagina web del proyecto.

Para acceder de forma definitiva a nuestra web tendremos que copiar el siguiente url: http://127.0.0.1:8000/AppRegistros/inicio

![image](https://user-images.githubusercontent.com/124483470/217139419-1e106604-8a86-4e41-a51d-681df290e36b.png)

Tambien se puede acceder a la base de datos desde la administracion de django con el siguiente url: http://127.0.0.1:8000/admin/

#usuario = usuario
#contraseña = 12345678

![image](https://user-images.githubusercontent.com/124483470/217140364-851d08ab-ae6a-435f-b5ba-19251785177c.png)


4. Autor de este proyecto: Bruno Emanuel, Montiel Alderete



 
  
  




