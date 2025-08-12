
# IMAGEN

# ¿Qué es una lista?
Una **lista** es una colección ordenada de elementos. Puedes almacenar:
- Letras del alfabeto
- Números
- Nombres
- O cualquier tipo de dato (incluso mezclados)
### Ejemplo:
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```
### Salida:
```
['trek', 'cannondale', 'redline', 'specialized']
```
## Índices: las posiciones empiezan desde 0

- El **primer elemento** de una lista tiene índice `0`.
- El **segundo** tiene índice `1`.
- El **cuarto** tiene índice `3`, y así sucesivamente.

### ¿Por qué?
Esto es común en la mayoría de los lenguajes de programación. Tiene que ver con cómo se accede a la memoria internamente.  

### Ejemplo:
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[0])  # trek
print(bicycles[1])  # cannondale
print(bicycles[3])  # specialized
```
## índices negativos
- -1 accede al último elemento
- -2 al penúltimo, etc.
### Ejemplo:
```python
print(bicycles[-1])  # specialized
print(bicycles[-2])  # redline
```
##  Métodos de string con listas
Puedes aplicar métodos como .title(), .upper(), etc., directamente a los elementos si son cadenas.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())  # Trek
```

### Ejercicios de  `Try It Yourself`
### 🔗 [Ver la solución](/chapter03/tiy_01_whatis_a_list.py)

# Cambiando, Agregando y Eliminando Elementos
Las listas en Python suelen ser dinámicas, es decir, cambian mientras el programa se ejecuta.
Puedes agregar o eliminar elementos según las necesidades del programa.
Por ejemplo, en un videojuego donde se disparan alienígenas, podrías:

- Guardar los alienígenas en una lista.
- Eliminar uno cada vez que el jugador le dispara.
- Agregar uno nuevo cada vez que aparece otro en pantalla.
Esto hace que la lista crezca o se reduzca durante el juego.

## Modificar un elemento de la lista es muy similar a acceder a él:
1. Se usa el nombre de la lista.
2. Luego el índice del elemento entre corchetes.
3. Finalmente se asigna el nuevo valor con el operador =.

### Ejemplo:
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)
```
### Salida:
```
['ducati', 'yamaha', 'suzuki']
```
## Agregar elementos al final de una lista con `append()`
El método `append()` agrega un elemento al final de la lista.
### Ejemplo:
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
```
### Salida:
```
['honda', 'yamaha', 'suzuki', 'ducati']
```
## Insertar elementos en cualquier posición con `insert()`
El método `insert()` agrega un elemento en la posición que especifiques.
### Ejemplo:
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
```
### Salida:
```
['ducati', 'honda', 'yamaha', 'suzuki']
```
## Eliminar elementos de una lista con `del`
El comando `del` elimina un elemento en la posición que especifiques.
### Ejemplo:
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)
```
### Salida:
```
['yamaha', 'suzuki']
```
## Eliminar un elemento y usarlo después con `pop()`
El método `pop()` elimina el último elemento de la lista, pero te permite usar ese elemento después.
### Ejemplo:
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)          # ['honda', 'yamaha']
print(popped_motorcycle)    # suzuki
```
### Salida:
```
['honda', 'yamaha']
```
## Eliminar un elemento específico por su valor con `remove()`
El método `remove()` elimina la primera aparición de un valor específico en la lista.
### Ejemplo:
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
```
### Salida:
```
['honda', 'yamaha', 'suzuki']
```
Si necesitas usar el valor eliminado, puedes almacenarlo en una variable antes de eliminarlo.
### Ejemplo:
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)          # ['honda', 'yamaha', 'suzuki']
print(too_expensive)        # ducati
```
> Nota: `remove()` solo elimina la primera aparición del valor. Si el valor aparece varias veces, las demás no se verán afectadas.

### Ejercicios de  `Try It Yourself`
### 🔗 [Ver la solución](/chapter03/tiy_02_changing_adding_removing.py)

# Organizing a List

### Ejercicios de  `Try It Yourself`
### 🔗 [Ver la solución](tiy_)


# Avoiding Index Errors When Working with Lists

### Ejercicios de  `Try It Yourself`
### 🔗 [Ver la solución](tiy_)

