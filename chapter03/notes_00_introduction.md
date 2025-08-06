
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

# Changing, Adding, and Removing Elements

### Ejercicios de  `Try It Yourself`
### 🔗 [Ver la solución](/chapter03/tiy_02_changing_adding_and_removing_elements.py)

# Organizing a List

### Ejercicios de  `Try It Yourself`
### 🔗 [Ver la solución](tiy_)


# Avoiding Index Errors When Working with Lists

### Ejercicios de  `Try It Yourself`
### 🔗 [Ver la solución](tiy_)

