![imagen del capitulo 2](image.png)

# Capítulo 2: **Introducción a las Variables y Buenas Prácticas de Nombrado**

En programación, una **variable** es como una caja con etiqueta: guarda un dato que el programa podrá consultar, modificar o reemplazar más adelante. Son esenciales para almacenar información que cambia o que queremos reutilizar. Pero no basta con declarar variables: nombrarlas bien es una práctica profesional crucial.

## ¿Por qué importa el nombre de una variable?

Imagina que llegas a revisar un código que escribiste hace seis meses y encuentras esto:

```python
x = 25
y = True
z = "Juan"
```
¿Podrías decir qué representa cada una sin mirar más contexto? Ahora mira esta versión:

```python
user_age = 25
is_registered = True
user_name = "Juan"
```
El significado salta a la vista. *Un buen nombre habla por sí solo* y reduce la necesidad de comentarios o explicaciones innecesarias.

### 1. Usa nombres descriptivos y claros
Un nombre debe reflejar con precisión qué guarda la variable. Ejemplo:
```markdown
✅ total_price
❌ tp
```
Evita abreviaciones innecesarias o confusas. El código no debe requerir traducción.

### 2. Respeta el lenguaje del compilador (y del lector)
Cada lenguaje tiene palabras reservadas que no puedes usar como variables. En Python, por ejemplo:
```python
❌ for = 5 → Error
✅ number_of_loops = 5
```
Además, evita escribir variables con nombres que podrían confundirse con estructuras del lenguaje o abreviaturas ambiguas.

### 3. No uses espacios ni símbolos especiales
Usa guiones bajos (_) para separar palabras. Por ejemplo:
```notebook
✅ user_email
❌ user email
❌ user@email
```

### 4. El nombre debe comenzar correctamente
Los nombres de variables deben comenzar con una letra o un guion bajo. No pueden empezar con un número ni contener caracteres especiales.
```notebook
✅ _backup_version
✅ version1
❌ 1version
❌ @version
```
### 5. Encuentra el equilibrio entre corto y descriptivo
Un nombre debe ser lo suficientemente largo para tener sentido, pero no tan largo que parezca una frase entera.
```notebook
✅ email_subject
❌ e
❌ this_is_the_subject_of_the_email_to_be_sent_later
```

### 6. Sé coherente con el estilo
Elige un estilo de nombrado y úsalo de forma consistente:

- `snake_case` → Recomendado para Python. Ej: user_email
- `camelCase` → Más común en JavaScript. Ej: userEmail

No mezcles estilos en el mismo proyecto:
```notebook
❌ user_email, userEmail, Useremail
✅ user_email, user_age, user_address
```


## Cuando Python detecta un error, muestra:

- Línea del error: Indica en qué línea ocurrió.
- Error de sintaxis: Señala la línea y explica el problema sintáctico.
- Tipo de error: Clasifica el error (sintaxis, tipo, índice, etc.).
- Nombre del error: Breve descripción del problema.

## ¿camel case o snake case?

En Python, se recomienda usar snake_case para la mayoría de los identificadores, especialmente para variables, funciones y nombres de archivos. Esto está respaldado por PEP 8, que es la guía oficial de estilo para Python.

### 🐍 PEP 8 recomienda:
| Elemento           | Convención           | Ejemplo                       |
| ------------------ | -------------------- | ----------------------------- |
| Variables          | `snake_case`         | `user_name`, `total_sum`      |
| Funciones          | `snake_case()`       | `get_data()`, `send_email()`  |
| Métodos            | `snake_case()`       | `calculate_total()`           |
| Constantes         | `UPPER_CASE`         | `MAX_RETRIES`, `DEFAULT_PORT` |
| Clases             | `CamelCase` (Pascal) | `User`, `HttpResponse`        |
| Módulos y archivos | `snake_case.py`      | `my_module.py`                |
| Paquetes           | `snake_case`         | `my_package`                  |


### Ejercicios de variables `Try It Yourself`
### 🔗 [Ver la solución](tiy_01_simple_message.py)

# Capítulo 2: Tipo de datos
## Strings
son una serie de caracteres encerrados entre comillas simples o dobles. Pueden contener letras, números, símbolos y espacios. En Python, los strings son inmutables, lo que significa que no puedes cambiar un carácter específico una vez creado el string.
### Ejemplos de Strings
```python
# String con comillas simples
saludo = 'Hola, mundo!'
# String con comillas dobles
mensaje = "Python es genial"
# String con comillas triples (útil para textos largos)
descripcion = """Python es un lenguaje de programación versátil.
Permite desarrollar desde scripts simples hasta aplicaciones complejas."""
```
### comillas en Strings
Si necesitas incluir comillas dentro de un string, puedes usar diferentes tipos de comillas para evitar conflictos:
```python
# Comillas simples dentro de comillas dobles
frase = "Ella dijo: 'Hola, ¿cómo estás?'"
# Comillas dobles dentro de comillas simples
frase2 = 'El libro se llama "Aprendiendo Python"'
# Comillas triples para incluir comillas simples y dobles
frase3 = """El profesor dijo: 'Python es "fácil" de aprender'"""
```
### Chasing cases
Los strings en Python son sensibles a mayúsculas y minúsculas, lo que significa que `"Python"` y `"python"` se consideran diferentes valores.

Para facilitar la comparación o el formato, puedes usar métodos que convierten las letras del string:

- `.lower()` convierte todas las letras a minúsculas.
- `.upper()` convierte todas las letras a mayúsculas.
- `.title()` convierte la primera letra de cada palabra a mayúscula y las demás a minúsculas (formato título).
```python
texto = "Python es Genial"

print(texto.lower())  # python es genial
print(texto.upper())  # PYTHON ES GENIAL
print(texto.title())  # Python Es Genial

```
### Concatenación de Strings y Formateo básico
Puedes combinar strings usando el operador `+`.Además, puedes incluir caracteres especiales para mejorar la presentación, como:
- `\t` para agregar tabulaciones (espacios horizontales).
- `\n` para saltos de línea:

```python
nombre = "Juan"
apellido = "Pérez"

# Concatenación simple con espacio
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # Salida: Juan Pérez   

# Concatenación con tabulación (\t) y salto de línea (\n)
mensaje = "Nombre:\t" + nombre + "\nApellido:\t" + apellido
print(mensaje)
# Salida:
# Nombre:	Juan
# Apellido:	Pérez

```
### Eliminación de espacios en blanco
En Python, los espacios en blanco al inicio y al final de una cadena pueden interferir con el procesamiento de datos. Para limpiarlos, utiliza:
- `.strip()` para eliminar espacios al inicio y al final.
- `.lstrip()` para eliminar espacios solo al inicio.
- `.rstrip()` para eliminar espacios solo al final.

```python
texto = "   hola mundo   "
print(texto.strip())   # "hola mundo"
print(texto.lstrip())  # "hola mundo   "
print(texto.rstrip())  # "   hola mundo"
```

### Ejercicios de Strings `Try It Yourself`
### 🔗 [Ver la solución](tiy_02_strings.py)


## Numbers
Los numeros son usados en diferentes ocasiones como puntuaciones de juegos, cálculos matemáticos y tambien se usan para almacenar datos en la web. En Python, existen varios tipos de números y son tratados dependiendo como se usan.

### Integer
los enteros nos ayudan a realizar operaciones comos:
- Sumar → `2 + 3`
- Restar → `5 - 2`
- Multiplicar → `4 * 3`
- Dividir → `10 / 2`
- Potenciar → `2 ** 3` # 2 ^ 3

Python maneja enteros de forma ilimitada, por lo que puedes trabajar con números muy grandes sin preocuparte por errores de desbordamiento.

Además, Python respeta el orden de operaciones matemáticas (también conocido como precedencia de operadores):
```python

resultado = 2 + 3 * 4
print(resultado)  # Salida: 14

resultado2 = (2 + 3) * 4
print(resultado2)  # Salida: 20

```

### Floats
Un float es cualquier número con punto decimal, como 0.5, 3.14, o 2.0. Este tipo de número "flota" porque el punto decimal puede estar en cualquier lugar del número.
### Cosas clave que debes saber:
Puedes sumar, restar, multiplicar floats sin problemas:
```python
0.1 + 0.1  →  0.2
2 * 0.1    →  0.2
```
A veces los resultados no son exactos, debido a cómo la computadora representa los decimales internamente:
```python
0.2 + 0.1  →  0.30000000000000004
3 * 0.1    →  0.30000000000000004
```
### ¿Qué hacer con los decimales extra?
No te preocupes. Este comportamiento es *normal en todos los lenguajes de programación.* Más adelante, aprenderás técnicas para redondear o formatear estos resultados si es necesario.

### Evitar errores de tipo con str()
Cuando mezclas texto (strings) y números (int) en un mensaje, Python necesita que todos sean del mismo tipo para poder combinarlos.

*Problema común:*

```python
age = 23
mensaje = "Feliz cumpleaños número " + age + "!"
# ❌ TypeError: no se puede concatenar str e int
```
Python lanza un TypeError, porque no puede juntar directamente un número con texto.

*Solución:*
Convierte el número a texto usando `str()`:
```python
age = 23
mensaje = "Feliz cumpleaños número " + str(age) + "!"
print(mensaje)  
# Salida: Feliz cumpleaños número 23!
```

### División en Python 2
En Python 2, dividir enteros como 3 / 2 da 1, no 1.5, porque trunca el decimal.

Para obtener un resultado decimal, al menos uno de los números debe ser float:
```python
3 / 2.0  →  1.5
3.0 / 2  →  1.5
```
Este comportamiento no ocurre en Python 3, donde 3 / 2 `ya da 1.5.`

### Ejercicios de Numbers `Try It Yourself`
### 🔗 [Ver la solución](tiy_03_numbers.py)
