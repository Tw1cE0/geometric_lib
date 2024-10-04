# Geometric Calculator

This repository contains a simple Python calculator for calculating the area and perimeter of various geometric shapes.

## General Description

This calculator provides a user-friendly interface for calculating the area and perimeter of:

* **Circle:**  Requires the radius (R) as input.
* **Square:** Requires the side length (a) as input.
* **Rectangle:** Requires the length (l) and width (w) as input.
* **Triangle:** Requires the lengths of all three sides (a, b, c) as input. 

## Function Descriptions

### Area Functions

**`calculate_circle_area(radius)`**

* **Description:** Calculates the area of a circle.
* **Input:** 
    * `radius`:  The radius of the circle (a number representing the distance from the center to the edge).
* **Output:** The area of the circle.
* **Formula:** `S = πR²` where `S` is the area and `R` is the radius.

**`calculate_square_area(side)`**

* **Description:** Calculates the area of a square.
* **Input:**
    * `side`: The length of one side of the square.
* **Output:** The area of the square.
* **Formula:** `S = a²` where `S` is the area and `a` is the side length.

**`calculate_rectangle_area(length, width)`**

* **Description:** Calculates the area of a rectangle.
* **Input:**
    * `length`: The length of the rectangle.
    * `width`: The width of the rectangle.
* **Output:** The area of the rectangle.
* **Formula:** `S = ab` where `S` is the area, `a` is the length, and `b` is the width.

**`calculate_triangle_area(a, b, c)`**

* **Description:** Calculates the area of a triangle using Heron's formula.
* **Input:**
    * `a`, `b`, `c`: The lengths of the three sides of the triangle.
* **Output:** The area of the triangle.
* **Formula:** `S = sqrt(p * (p-a) * (p-b) * (p-c))` where `S` is the area and `p` is the semiperimeter (`p = (a + b + c) / 2`).

### Perimeter Functions

**`calculate_circle_perimeter(radius)`**

* **Description:** Calculates the perimeter of a circle (also known as circumference).
* **Input:** 
    * `radius`:  The radius of the circle.
* **Output:** The circumference of the circle.
* **Formula:** `P = 2πR` where `P` is the perimeter and `R` is the radius.

**`calculate_square_perimeter(side)`**

* **Description:** Calculates the perimeter of a square.
* **Input:**
    * `side`: The length of one side of the square.
* **Output:** The perimeter of the square.
* **Formula:** `P = 4a` where `P` is the perimeter and `a` is the side length.

**`calculate_rectangle_perimeter(length, width)`**

* **Description:** Calculates the perimeter of a rectangle.
* **Input:**
    * `length`: The length of the rectangle.
    * `width`: The width of the rectangle.
* **Output:** The perimeter of the rectangle.
* **Formula:** `P = 2a + 2b` where `P` is the perimeter, `a` is the length, and `b` is the width.

**`calculate_triangle_perimeter(a, b, c)`**

* **Description:** Calculates the perimeter of a triangle.
* **Input:**
    * `a`, `b`, `c`: The lengths of the three sides of the triangle.
* **Output:** The perimeter of the triangle.
* **Formula:** `P = a + b + c` where `P` is the perimeter, `a`, `b`, and `c` are the sides.

## Usage Instructions

1. **Run the script:** `python calculate.py`
2. **Select the figure:** Enter the name of the desired figure (Circle, Square, Rectangle, or Triangle).
3. **Select the function:** Enter the desired function (Area or Perimeter).
4. **Enter the dimensions:**  Enter the required dimensions for the chosen figure (e.g., radius for a circle, side length for a square, length and width for a rectangle, or three sides for a triangle).
5. **View the result:** The calculator will display the calculated area or perimeter.

## Commit History 
commit 351bc225b412d8e4b996fd9115ae415467e96641 (HEAD -> issue_correction)
Author: Artemii Safonov <artemii.e.safonov@gmail.com>
Date:   Thu Oct 3 14:14:34 2024 +0300

    Добавлена документация в файл triangle

commit a5ac406c191d41b0bd89e9862322546d43102801
Author: Artemii Safonov <artemii.e.safonov@gmail.com>
Date:   Thu Oct 3 14:12:26 2024 +0300

    Добавлена документация в файл square

commit dd3916a291892f73331029732fa6fc7064ef82ab
Author: Artemii Safonov <artemii.e.safonov@gmail.com>
Date:   Thu Oct 3 14:10:37 2024 +0300

    Добавленио документирование в файл circle

commit 5e22e6bdadade726ac67a62cf7eccb5cbdc569d6
Author: Artemii Safonov <artemii.e.safonov@gmail.com>
Date:   Thu Oct 3 14:09:16 2024 +0300

    добавлено документирование в файл calculate

commit b5b0fae727ca72c317c383b39c0af73d6adcd81c (origin/develop, develop)
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 18:02:23 2021 +0300

    L-04: Update docs for calculate.py

commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:57:42 2021 +0300

    L-04: Add calculate.py

commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:52:26 2021 +0300

    L-04: Doc updated for triangle

commit d080c7888b81955bad2ed78d58ad910526b5132a
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:48:39 2021 +0300

    L-04: Triangle added

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300
