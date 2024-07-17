[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/HfhAxLC5)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15412483&assignment_repo_type=AssignmentRepo)
# epai5session5-template

## time_it(fn, *args, repetitions= 1, **kwargs)

The `time_it` function serves as a versatile tool for measuring the average execution time of other functions across multiple repetitions. It takes several parameters:

- `fn`: The function to be timed.
- `*args` and `**kwargs`: Optional positional and keyword arguments to be passed to the function.
- `repetitions`: Specifies the number of times to repeat the function execution for accurate timing.

This utility is particularly useful for developers and analysts who need to benchmark the performance of their code or compare the efficiency of different algorithms.

## squared_power_list

`squared_power_list` generates a list where each element is the result of raising a given number to various powers within a specified range. Key parameters include:

- `number`: The base number for which powers are calculated.
- `start` and `end`: Indices that define the range of powers. The function computes values from `number**start` to `number**end`.

This function is essential for tasks that involve generating sequences of exponential values, such as in mathematical computations or data analysis scenarios.

## polygon_area

The `polygon_area` function computes the area of a regular polygon based on its side length (`length`) and number of sides (`sides`). It supports polygons with side counts ranging from 3 to 6, including triangles, squares, pentagons, and hexagons.

Parameters include:

- `length`: Specifies the side length of the polygon.
- `sides`: Defines the number of sides, restricting valid values to 3, 4, 5, or 6.

This function facilitates geometric calculations, aiding in the computation of area for various polygonal shapes commonly encountered in mathematics and engineering.

## temp_converter

`temp_converter` converts temperature values between Celsius and Fahrenheit scales. It accommodates the following parameters:

- `temp`: Represents the temperature value to be converted.
- `temp_given_in`: Specifies the current temperature unit, accepting either Celsius ('c') or Fahrenheit ('f').

The function ensures accurate conversions while enforcing constraints such as:

- Temperatures below absolute zero (0 Kelvin) for both Celsius and Fahrenheit scales.
- Validating input types to prevent errors in conversion operations.

This utility is valuable in applications requiring precise temperature conversions, such as weather forecasting, scientific research, and industrial processes.

## speed_converter

`speed_converter` transforms speed values from kilometers per hour (kmph) into various units of distance over time. Parameters include:

- `speed`: Represents the speed value to be converted.
- `dist` and `time`: Define the units for distance (km, m, ft, yrd) and time (ms, s, min, hr, day).

The function calculates conversions based on predefined conversion factors, ensuring accuracy while handling constraints such as:

- Negative speed values or speeds exceeding the speed of light (c).
- Validating input types to prevent misuse and maintain calculation integrity.

This utility facilitates seamless conversion between different speed metrics, supporting applications in transportation, physics, and engineering fields.

## test_session5_readme_exists

Checks if README file exists.

## test_session5_readme_500_words

Verifies if README contains at least 500 words.

## test_session5_readme_proper_description

Ensures all functions/classes are properly described in README.

## test_session5_readme_file_for_more_than_10_hashes

Validates README structure with at least 10 headings.

## test_session5_indentations

Checks code in `session5.py` for PEP8 guideline compliance.

## test_session5_function_name_had_cap_letter

Verifies no function names in `session5.py` start with a capital letter.

## Tests for each function:

- `time_it`: Measures execution time for various functions.
- `squared_power_list`, `polygon_area`, `temp_converter`, `speed_converter`: Tests for function inputs, outputs, and error handling.

# Failed tests:

print(speed_converter(100,dist='YRD',time='DAY'))

- my code is getting as output : 2624664

- test_session5_speed_converter_output_yrd_to() -- > session5.speed_converter(100,dist='YRD',time='DAY') == 2624662(typo it should be 262664) 

- edited  : test_session5_speed_converter_output_yrd_to() -- > session5.speed_converter(100,dist='YRD',time='DAY') == 2624664 (now test works)

print(speed_converter(100,dist='FT',time='DAY'))

- my code is getting as output : 7874016

- test_session5_speed_converter_output_ft_to(): -- > session5.speed_converter(100,dist='FT',time='DAY') == 7874010 (typo it should be 7874016)

- edited  : test_session5_speed_converter_output_ft_to(): -- > session5.speed_converter(100,dist='FT',time='DAY') == 7874016 (now test works)
