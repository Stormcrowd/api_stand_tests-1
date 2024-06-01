#Creación de autotests a partir de listas de comprobación
#Principios:
#1 Unidad de comprobación
#2 Independencia de datos
#3 Autonomía de las pruebas

import sender_stand_request
import data

'''
NOTA:

El único campo que requiere cambios en todas las comprobaciones es firstName,
por lo que no es necesario crear un cuerpo de solicitud independiente para
cada prueba. En su lugar, es más eficiente modificar el cuerpo de solicitud
ya existente en data.py.

'''


# Esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.user_body.copy()
    # Permite la modificacion de la clave firstname, seteada en el diccionario por el parametro agregado por el usuario al llamar la funcion
    current_body["firstName"] = first_name #(firstName diferente de first_name)
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body


#AUTOMATIZACION:
#De acuerdo a: https://docs.google.com/spreadsheets/d/1O2rwRqmzSwFlWbsYrwSOFBw0C7-pDEl2/edit#gid=446383470
# NOTA: TODOS LOS TEST USAN PARA RELLENAR LA CASILLA EL DOC!
#Prueba 1, Numero permitido de caracteres: 2
'''

def test_create_user_2_letter_in_first_name_get_success_response():
    # Utilizamos la funcion anterior para definir el firstName! "Aa"
    user_body = get_user_body("Aa")
    # Tomamos lo creado(user_body) para POSTEAR una solicitud al servidor
    # presentando dicho escenario(Aa)
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprobamos si la respuesta a nuestro POST es 201 :O
    assert user_response.status_code == 201 #¿Es user_response 201?
    print(user_response.status_code) #Innecesario, no mas pa verlo en consola
    # Comrpobamos si el autoToken en el BODY es DIFERENTE de VACIO
    # es decir: que si posea uno !
    assert user_response.json()["authToken"] != ""
    print(user_response.json()) #Innecesario, no mas pa verlo en consola

    # Con esto creado, es importante comprobar que el usuario EXISTE en
    # y quedo registro en la tabla! (users)
    # Para esto utilizamos la funcion antes creada en sender_stand_request.py
    # get_users_table(), para conseguir la tabla de informacion de usuarios
    # guardandola en una nueva variable:
    users_table_response = sender_stand_request.get_users_table()
    # Creamos una variable a la que le asignaremos COMO DEBERIAN VERSE
    # los datos del usuario:
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    # Usamos la variable con la tabla, y la variable de como deberian verse
    # PARA COMPARACION! y CONFIRMACION:
    assert users_table_response.text.count(str_user) == 1
    
'''

# Ahora tomaremos el test anterior, que realiza la accion requerida y la
# automatizaremos. Es decir, volveremos dicho "TEST" una funcion! , y la
# usaremos para hacer MULTIPLES TEST! sin repetir tanto CODIGO.

# Para ello modificaremos el "get_user_body" original, retirando la prueba
# ESPECIFICA y suplantandola con una variable que pueda ser AJUSTADA por
# el test! (FUNCION: variable y TEST: Espcifico) Veamos:

def positive_assert(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # Tomamos lo creado(user_body) para POSTEAR una solicitud al servidor
    # presentando dicho escenario(Aa)
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprobamos si la respuesta a nuestro POST es 201 :O
    assert user_response.status_code == 201 #¿Es user_response 201?
    print(user_response.status_code) #Innecesario, no mas pa verlo en consola
    # Comrpobamos si el autoToken en el BODY es DIFERENTE de VACIO
    # es decir: que si posea uno !
    assert user_response.json()["authToken"] != ""
    print(user_response.json()) #Innecesario, no mas pa verlo en consola

    # Con esto creado, es importante comprobar que el usuario EXISTE en
    # y quedo registro en la tabla! (users)
    # Para esto utilizamos la funcion antes creada en sender_stand_request.py
    # get_users_table(), para conseguir la tabla de informacion de usuarios
    # guardandola en una nueva variable:
    users_table_response = sender_stand_request.get_users_table()
    # Creamos una variable a la que le asignaremos COMO DEBERIAN VERSE
    # los datos del usuario:
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    # Usamos la variable con la tabla, y la variable de como deberian verse
    # PARA COMPARACION! y CONFIRMACION:
    assert users_table_response.text.count(str_user) == 1

# Ahora la prueba 1, se resumio, ya que LLAMA a la funcion creada.
# NOTA: La funcion creada se denomina POSSITIVE ASSERT ya que comprueba
# que el OBJETO que probamos funcione de forma POSITIVA, existe el
# NEGATIVE ASSERT, para comprobar que FALLE debidamente.

def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

# Prueba 2, 15 caracteres, por esto AUTOMATIZAMOS! Ahora solo llamamos el
# POSSITIVE ASSERT, en vez de escribir lo mismo 2 veces! ¡Genial!

def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

# AHORA VEAMOS EL NEGATIVE ASSERT!

def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)

    # Esto verifica el CODIGO del msj
    assert user_response.status_code == 400 #¿Es user_response 404?
    print(user_response.status_code) #Innecesario, no mas pa verlo en consola

    # Esto verifica que el CODIGO, que se le muestre al usuario sea 400
    # en el TEXTO(string), por eso usamos json!
    assert user_response.json()["code"] == 400
    print(user_response.json()["code"])  # Innecesario, no mas pa verlo en consola

    # Por ultimo comprobamos que el atributo "message" presente en string
    # el mensaje deseado por el area de diseño:
    assert user_response.json()["message"] == "Has introducido un nombre de usuario no válido. El nombre solo puede " \
                                              "contener letras del alfabeto latino, la longitud debe ser de 2 a 15 " \
                                               "caracteres."
    print(user_response.json()["message"])  # Innecesario, no mas pa verlo en consola

# Prueba 3, 1 caracter DEBE FALLAR !
def test_create_user_1_letter_in_first_name_get_error_response():
    #USAMOS EL NEGATIVE ASSERT !
    negative_assert_symbol("A")

# Prueba 4, 16 caracteres
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")


# Prueba 5, Un espacio (ERRONEA)
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")
    # Después de iniciarla, se devolverá un error; pero no te preocupes.
    # a API permite espacios en el nombre de usuario o usuaria, pero la
    # lista de comprobación no. Aún así, utiliza la lista de comprobación
    #  como guía. Esto se lo reportarias al equipo de desarrollo !!!!

# Prueba 6, caracteres especiales
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")
    # \ andes de cada " para poder comprobar de forma efectiva: "№%@"

# Prueba 7, Numeros
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")


# Para las pruebas 8 y 9, si evaluas el documento poseen mensajes de error
# DIFERENTES, se recomienda crear otra funcion con el nuevo msj integrado
# asi de manera sencilla se automatiza en el codigo


def negative_assert_no_first_name(first_name):
    # Al ser pruebas en las cuales no se va a cambiar el nombre del
    # usuario, no es requerido el paso en el igualamos el parametro
    # a un string (revisa pruebas 8 y 9)
    user_response = sender_stand_request.post_new_user(first_name)

    assert user_response.status_code == 400
    print(user_response.status_code) #Innecesario, no mas pa verlo en consola

    assert user_response.json()["code"] == 400
    print(user_response.json()["code"])  # Innecesario, no mas pa verlo en consola

    assert user_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"
    print(user_response.json()["message"])  # Innecesario, no mas pa verlo en consola


# Prueba 8, NO SE ENVIA NINGUN dato!
def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    # De lo contrario, se podrían perder los datos del diccionario de origen
    user_body = data.user_body.copy()
    # El parámetro "firstName" se elimina de la solicitud
    user_body.pop("firstName")
    # Comprueba la respuesta
    negative_assert_no_first_name(user_body)

# Prueba 9. Error
# El parámetro "firstName" contiene un string vacío
def test_create_user_empty_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body("") #VACIO!
    # Comprueba la respuesta
    negative_assert_no_first_name(user_body)

# Prueba 10, al pasar un tipo de dato diferente no parece poder utilizarse
# las pruebas previas: mandar un INT (numero)

def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400  # ¿Es user_response 404?
    print(user_response.status_code)  # Innecesario, no mas pa verlo en consola


'''
NOTA:

Por ahora el factor CLAVE para separar automatizaciones parece ser:
EL MENSAJE, si el mensaje que entrega al usuario es DIFERENTE, la prueba
sera DIIFERENTE.

'''