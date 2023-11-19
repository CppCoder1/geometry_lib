# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = 0.5 * a * h

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Functions
### Triangle module:
This module contains 2 functions: *area* and *parimeter*
#### Area
```Python
def area(a : float, h : float) -> float # return area of triangle
```

Example of use this function:
```Python
from triangle import area

triangle_area = area(5, 6)
print(triangle_area) # output: 15
```

#### Perimeter
```python
def perimeter(a : float, b : float, c : float) -> float #return perimeter of triangle
```

Example of use this function:
```python
from triangle import perimeter

triangle_perimeter = perimeter(5, 6, 7)
print(triangle_perimeter) # output: 18
```

## Circle module
This module contains 2 functions: *area* and *parimeter*
#### Area
```Python
def area(r : float) -> float # return area of circle
```

Example of use this function:
```Python
from circle import area

circle_area = area(5)
print(circle_area) # output: 25pi
```
#### Perimeter
```python
def perimeter(r : float) -> float #return perimeter of circle
```

Example of use this function:
```python
from circle import perimeter

circle_perimeter = perimeter(5)
print(circle_perimeter) # output: 10pi
```
### Square module:
This module contains 2 functions: *area* and *parimeter*
#### Area
```Python
def area(a : float) -> float # return area of square
```

Example of use this function:
```Python
from square import area

square_area = area(5)
print(square_area) # output: 25
```
#### Perimeter
```python
def perimeter(a : float) -> float #return perimeter of square
```

Example of use this function:
```python
from square import perimeter

square_perimeter = perimeter(5)
print(square_perimeter) # output: 20

```
### Rectangle module:
This module contains 2 functions: *area* and *parimeter*
#### Area
```Python
def area(a : float, b : float) -> float # return area of rectangle
```

Example of use this function:
```Python
from rectangle import area

rectangle_area = area(5, 6)
print(rectangle_area) # output: 30
```
#### Perimeter
```python
def perimeter(a : float, b : float) -> float #return perimeter of rectangle
```

Example of use this function:
```python
from rectangle import perimeter

rectangle_perimeter = perimeter(5, 6)
print(rectangle_perimeter) # output: 22
```

#### Testing protocol
* Bug report #1: when the function in square module perimeter is called with a negative argument, a negative perimeter is returned
* Bug report #2: when the function in square module perimeter is called with a "Простите, а где здесь туалет?" argument, it is returned string instead of return exception
* Bug report #3: when the function in rectangle module perimeter is called with a number and string arguments, it is crashed
* Bug report #4: when the function in square module perimeter is called with a zero argument, it return 20 instead of 0
* 