# Aquí almacenarás la URL base de Urban Grocers y la ruta específica para la documentación

'''

URL_SERVICE: Esta es una constante que almacena la URL base del servicio de Urban Grocers. La frase "copia la URL generada sin la barra inclinada al final" es un marcador de posición: reemplázala con la URL real del servidor que iniciaste.
DOC_PATH: Esta constante almacena la ruta específica para acceder a la documentación en la URL base.

'''

URL_SERVICE = "https://cnt-c7c60215-e37b-4ad1-8819-7d71027c27ed.containerhub.tripleten-services.com"
DOC_PATH = "/docs/"

LOG_MAIN_PATH = "/api/logs/main/"
   #logs del servidor principal
USERS_TABLE_PATH = "/api/db/resources/user_model.csv"
   #recuperar informacion de base de datos
CREATE_USER_PATH = "/api/v1/users/"
    #CREAR un usuario
PRODUCTS_KITS_PATH = "/api/v1/products/kits/"
    #BUSCAR kits por sus PRODUCTOS