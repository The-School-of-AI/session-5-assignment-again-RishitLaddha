"""
This module contains functions to perform various calculations such as generating a power list,
calculating the area of polygons, converting temperatures, and converting speeds.
It also provides a timing function to measure the execution time of other functions.
"""
import time
import math
def time_it(fn, *args, repetitions=1, **kwargs):
    """This is a generalized function to call any function
    user specified number of times and return the average
    time taken for calls"""
    if not isinstance(repetitions, int) or repetitions < 0:  # Check if repetitions is a positive integer
        raise ValueError("Repetitions must be a non-negative integer")
    if repetitions == 0:  # if repetitions is 0 then return 0
        return 0
    start_time = time.time()
    for _ in range(repetitions):
        fn(*args, **kwargs)
    end_time = time.time()
    average_time = (end_time - start_time) / repetitions
    print(f"Average time per call: {average_time:.10f} seconds")
    return average_time
#time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=5)
def squared_power_list(number, *args, start=0, end=5, **kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""
    # Validations "if" block
    if not isinstance(number, int):
        raise TypeError("Only integer type arguments are allowed")
    if number >= 10:
        raise ValueError("Value of number should be less than 10")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end should be integers")
    if start < 0 or end < 0:
        raise ValueError("Value of start or end can't be negative")
    if start > end:
        raise ValueError("Value of start should be less than end")
    if len(args) > 0:
        raise TypeError("it takes maximum 1 positional arguments")
    if len(kwargs) > 0:
        raise TypeError("it takes maximum 2 keyword/named arguments")
    # Return the list of number to the power of numbers from start to end
    return [number**i for i in range(start, end)]
#time_it(squared_power_list, 2, start=0, end=5, repetitions=5) #2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]
def polygon_area(length, *args, sides=3, **kwargs):
    """Returns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""
    # Validations
    if not isinstance(length, (int, float)) or isinstance(length, complex):
        raise TypeError("Length should be a real number")
    if length <= 0:
        raise ValueError("Length should be greater than 0")
    if not isinstance(sides, int) or isinstance(sides, complex):
        raise TypeError("Sides should be an integer")
    if sides not in [3, 4, 5, 6]:
        raise ValueError("Sides should be between 3 and 6 (inclusive)")
    if len(args) > 0:
        raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 0:
        raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided")
    # Return area
    return (sides * length**2) / (4 * math.tan(math.pi / sides))
#time_it(polygon_area, 15, sides = 3, repetitions=10) # 15 is the side length. This polygon supports area calculations of upto a hexagon
def temp_converter(temp, *args, temp_given_in='f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""
    # Validations
    if not isinstance(temp, (int, float)) or isinstance(temp, complex):
        raise TypeError("Temperature should be a real number")
    if not isinstance(temp_given_in, str):
        raise TypeError("Charcater string expected")
    if temp_given_in.lower() not in ['f', 'c']:
        raise ValueError("Only f or c is allowed")
    if temp_given_in.lower() == 'c' and temp < -273.15:
        raise ValueError("Temprature can't go below -273.15 celsius = 0 Kelvin")
    if temp_given_in.lower() == 'f' and temp < -459.67:
        raise ValueError("Temprature can't go below -459.67 fahrenheit = 0 Kelvin")
    if len(args) > 0:
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 0:
        raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")
    # Return the converted temperature
    if temp_given_in.lower() == 'c':
        return (temp * 9/5) + 32
    else:  # temp_given_in.lower() == 'f'
        return (temp - 32) * 5/9
#time_it(temp_converter, 100, temp_given_in = 'f', repetitions=100) # 100 is the base temperature given to be converted    
def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """
    # Validations
    if not isinstance(speed, (int, float)) or isinstance(speed, complex):
        raise TypeError("Speed can be int or float type only")
    if speed <= 0.0:
        raise ValueError("Speed can't be negative")
    if speed >= 300001:
        raise ValueError("Speed can't be greater than speed of light")
    if not isinstance(dist, str):
        raise TypeError("Charcater string expected for distance unit")
    if dist.lower() not in ['km', 'm', 'ft', 'yrd']:
        raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")
    if not isinstance(time, str):
        raise TypeError("Charcater string expected for distance unit")
    if time.lower() not in ['ms', 's', 'min', 'hr', 'day']:
        raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")
    if len(args) > 0:
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 0:
        raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")
    # Conversion factors
    dist_factors = {
        'km': 1,
        'm': 1000,
        'ft': 3280.84,
        'yrd': 1093.61
    }
    time_factors = {
        'ms': 60 * 60 * 1000,
        's': 60 * 60,
        'min': 60,
        'hr': 1,
        'day': 1/24
    }
    # Conversion
    converted_speed = (speed * dist_factors[dist.lower()]) / time_factors[time.lower()]
    # Return the converted speed
    return round(converted_speed)
#time_it(speed_converter, 100, dist='km', time='min', repetitions=200) #dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by the user is in kmph.
