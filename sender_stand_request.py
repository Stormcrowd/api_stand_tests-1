import configuration
import requests
import data

#SOLICITUDES GET !!

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


response = get_docs()
print(response.status_code)

'''
EXPLICACION:

import configuration: esta línea importa el archivo configuration.py. Esto significa que ahora puedes acceder a las constantes definidas en configuration.py: URL_SERVICE y DOC_PATH.

import requests: importa la librería Requests.

def get_docs(): define una función llamada get_docs. Cuando se llama a esta función, realiza una solicitud GET a la combinación de URL_SERVICE y DOC_PATH (es decir, la URL completa de la documentación).

response = get_docs(): esta línea llama a la función get_docs() y almacena la respuesta en la variable de respuesta.

print(response.status_code): muestra el código de estado de la respuesta HTTP. Por ejemplo, si todo va bien, debe mostrarse 200, que es el código de estado de "OK".

AL EJECUTAR CUIDADO, recuerda ejecutar cada archivo aparte (7/2)

'''

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)


answer = get_logs()
print(answer.status_code)
print(answer.headers)

def get_logs_params():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,params={"count":20})


answer2 = get_logs_params()
print(answer2.status_code)
print(answer2.headers)

'''
RECUERDA: 

1. Defines la funcion "get_loquesea"
2. Retornas ! request(libreria).get(tipo de solicitud)
3. Entre parentesis la concadenacion del URL mas el PATH necesario
4. Se le otorga a una variable el registro de la funcion antes definida
5. Imprimes el resultado de acuerdo a lo que busques: ".status_code,.headers.ok,etc)

NOTA: al agregar params cambia content-lengt y Etag ¿?
'''


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


answer3 = get_users_table()
print(answer3.status_code)
print(answer3.headers)


#SOLICITUDES POST !!

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud(parametro de la funcion 'body')
                         headers=data.headers)  # inserta los encabezados(de acuerdo al archivo 'data.py')


answer4 = post_new_user(data.user_body)  #dentro del argumento al llamar la funcion invoca 'user_body',
                                        #definido en el archivo 'data.py'
print (answer4.status_code)
print(answer4.json()) #Muestra la respuesta como un DICCIONARIO, legible.


def post_products_kits(IDS):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=IDS, headers=data.headers )


answer5= post_products_kits(data.product_ids)
print(answer5.status_code)
print(answer5.json())