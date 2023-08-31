# Torus-Volume-Calculator-Using-Monte-Carlo-Technique

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [How to Run](#how-to-run)
5. [Sample Output](#sample-output)
6. [Analysis](#analysis)
7. [Significance](#significance)
8. [Author](#author)
9. [License](#license)

## Introduction
The Python project calculates the volume of a torus using the Monte Carlo technique. A torus is a shape similar to a donut or the inner tube of a tire. Users can specify the major and minor radii and the number of points for the Monte Carlo simulation.

## Features
- User input validation for major and minor radii and the number of random points.
- Utilizes Monte Carlo technique to approximate the volume of a torus.
- Calculates and displays the probability of a point being inside the torus.
- Computes the error between the calculated and actual volume of the torus.

## Technologies Used
- Python
- NumPy for numerical calculations
- Built-in `time` library for displaying the time of execution

## How to Run
1. Clone the repository.
2. Run `main.py`.
3. Follow the on-screen prompts to input the major and minor radii and the number of points for the Monte Carlo simulation.

## Sample Output
```
--------------------------------------------------------------------------------
Enter the major radius of the torus:
Missing input!
Enter the major radius of the torus: true
true is not valid
Enter the major radius of the torus: 0
0 is less than 0!
Enter the major radius of the torus: gello
gello is not valid
Enter the major radius of the torus: 10.5
Enter the minor radius of the torus: 2.5
Enter the number of points to create: 10000000

The probability of a point being in Torus is 0.3831
The approximate volume of the torus is: 1.29474449000000e+03
The actual volume of the torus is: 1.29538557764298e+03
The error in the approximate volume is: 6.410876e-01

Programmed by Farjad Tariq
Date: Wed Aug 30 19:10:15 2023
End of processing.
```

## Analysis
1. **User Input Validation**: The program validates user input thoroughly, ensuring only valid, positive numbers are accepted.
  
2. **Accuracy**: The accuracy of the Monte Carlo technique improves with an increase in the number of points.
  
3. **Error Analysis**: The program calculates and displays the error between the approximate and actual volumes, providing an understanding of the reliability of the Monte Carlo technique.

## Significance
1. **Scientific Computing**: The Monte Carlo technique is fundamental in scientific computing for solving complex geometrical problems like volume calculations.
  
2. **Educational Value**: This project serves as a good introduction to the Monte Carlo technique and its applications.
  
3. **Customization**: The program allows user-defined inputs to tailor the calculations to specific needs.

## Author
- **Farjad Tariq**

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
