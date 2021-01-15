# Una cola de mensajes construida con python, flask y redis

## Como empezar
- Descargar Docker:
https://docs.docker.com/get-docker/
- Descargar Docker Compose:
https://docs.docker.com/compose/install/
- Descargar los archivos del repositorio: https://github.com/mdcamposf/meli_message_queue_redis_api-main.git
- Abrir el repositorio en Docker y luego correr los siguientes comandso en el Terminal en el orden indicado:
    - primero: docker-compose build
    - segundo: docker-compose up
- Instalar POSTMAN para poder hacer las pruebas:
https://www.postman.com/downloads/


## Como probarlo
Usar POSTMAN para probar cada caso, como se podra ver en cada imagen, dependiendo de la prueba que se quiera realizar se debe copiar y pegar las url indicadas en cada caso
y hacer un SEND dentro de POSTMAN:
  - PUSH: localhost:5000/api/queue/push?message=INSERTAR MENSAJE QUE DESEE
      - en mis ejemplos: 
          - localhost:5000/api/queue/push?message=mensaje1
          - localhost:5000/api/queue/push?message=mensaje2
  - GET: localhost:5000/api/queue/count
  - POP: localhost:5000/api/queue/pop
  
### Pruebas realizadas
#### B. PUSH - Envio de mensajes a la queue, status 200
- Envio mensaje1
![image](https://user-images.githubusercontent.com/77359265/104743002-ef992980-5729-11eb-88f4-4de4b9d5999d.png)
- Envio mensaje2
![image](https://user-images.githubusercontent.com/77359265/104743253-39820f80-572a-11eb-81df-677e24e7cdb7.png)

#### C. GET - Obtener cantidad de mensajes, status 200
- Cuenta los 2 mensjaes enviados
![image](https://user-images.githubusercontent.com/77359265/104743549-94b40200-572a-11eb-8276-24359a300251.png)

#### A. POP - Obtener el primer valor de la queue y eliminarlo, Status 200
- Obtiene el primer mensaje (mensaje1),
![image](https://user-images.githubusercontent.com/77359265/104743746-caf18180-572a-11eb-8e8a-58d4a9d83b57.png)
- y verifica con un GET que se elimina haciendo un conteo
![image](https://user-images.githubusercontent.com/77359265/104743930-09873c00-572b-11eb-85cf-4f58bd0decff.png)

- Obtiene el segundo mensaje (mensaje2), 
![image](https://user-images.githubusercontent.com/77359265/104745597-07be7800-572d-11eb-9fa9-d6d7d0cb2b40.png)
- y verifica con un GET que se elimina haciendo un conteo
![image](https://user-images.githubusercontent.com/77359265/104745916-5e2bb680-572d-11eb-9242-e1bb2acc1b9d.png)

#### A. POP - Obtener el primer valor de la queue y eliminarlo, Status 500
- No va a poder eliminar porque la queue esta vacia
![image](https://user-images.githubusercontent.com/77359265/104746228-c24e7a80-572d-11eb-8d62-38b0f87b2b21.png)

#### C. GET - Obtener cantidad de mensajes, status 404
- Cuando no hay mensajes en la queue
![image](https://user-images.githubusercontent.com/77359265/104752622-a8b13100-5735-11eb-9ed9-0f90f7e69f9d.png)

#### B. PUSH - Envio de mensajes a la queue, status 404
- Cuando se envia el parametro message erroneo. En este caso envio mesage con una sola s.
![image](https://user-images.githubusercontent.com/77359265/104756460-9be30c00-573a-11eb-8f6b-9d543f28a4bc.png)

#### B. PUSH - Envio de mensajes a la queue, status 500
- Para probar este status stopee redis en docker
![image](https://user-images.githubusercontent.com/77359265/104756854-1449cd00-573b-11eb-8b70-8719899a3664.png)
