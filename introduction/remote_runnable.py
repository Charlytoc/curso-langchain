# la clase RemoteRunnable nos permite usar una cadena a distancia 
from langserve import RemoteRunnable


# Creamos el enlace a la cadena remota 
remote_chain = RemoteRunnable("http://localhost:8000/tutor/")

# Invocamos la respuesta y listo, ya podemos usar nuestra app desde otro archivo u otra app en nuestro entorno virtual
response = remote_chain.invoke({"language": "spanish", "text": "Suscribe to my channel to learn AI development"})
print(response)
