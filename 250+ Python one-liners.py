"""
Welcome to 250+ Python one-liners!
Here are some handy Python one-liners for various tasks.
Thank you for stopping by!
"""
import snoop
from birdseye import eye
from colorama import init, Fore

init()
print(Fore.RED)

@snoop
@eye
#1 Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
print(celsius_to_fahrenheit(25))                        #TODO:  77.0

print(Fore.GREEN)                                                                                                                      #TODO: change color printf

#2 Swap two variables
def swap_without_temp(a, b):
    return b, a
result = swap_without_temp(5, 10)
print(f"After swapping: a = {result[1]}, b = {result[0]}")              #TODO: a = 5, b = 10

#3 Convert RGB to HEX
def rgb_to_hex(r, g, b):
    return f"#{((r<<16) + (g<<8) + b):06X}"
print(rgb_to_hex(0, 51, 255))                               #TODO: #0033FF

#4 Transpose of a matrix
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("\n".join(",".join(map(str, row)) for row in transpose_matrix(matrix)))       #TODO: 1,4,7
                                                                                        #  2,5,8
                                                                                        #  3,6,9
#5 Chack if date is valid
from datetime import datetime
def is_date_valid(val):
    return datetime.strptime(val, "%B %d, %Y %H:%M:%S") if val else False
print(is_date_valid("December 17, 1995 03:24:00"))                      #TODO: 1995-12-17 03:24:00

#6 Find the days of year
from datetime import datetime
def day_of_year(date):
    return date.timetuple().tm_yday
print(day_of_year(datetime(2024, 10, 6)))                        #TODO: 280

#7 Capitalize a sting
def capitalize_string(s):
    return s[0].upper() + s[1:] if s else ""
print(capitalize_string("follow for more"))                     #TODO: Follow for more

#8 Find the number of days between two days
from datetime import datetime
def day_diff(day1, day2):
    return abs((date2 - day1).days) + 1
date1 = datetime(2020, 10, 21)
date2 = datetime(2021, 10, 22)
print(day_diff(date1, date2))                                                    #TODO: 365

#9 Find the frecuecy of character in a string
def character_frequency(string):
    return {char: string.count(char) for char in set(string)}
print(",".join([f"{k}=>{v}" for k, v in character_frequency("hello").items()]))    #TODO: h=>1,l=>2,e=>1,o=>1

#10 Generate random HEX
import random
def random_hex():
    return f"#{random.randint(0, 0xFFFFFF):06X}"
print(random_hex())                                         #TODO: random colour

#11 Create random strings
import random, string
def random_string(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))
print(random_string(5))                                    #TODO: random string

#12 Find the odd occurrence
import random, functools
def find_odd(ar):
    return functools.reduce(lambda x, y: x ^ y, ar)
ar = [random.randint(1, 100) for _ in range(random.randint(10, 20))]

print("Input:", " ".join(map(str, ar)))
print("Result:", find_odd(ar))

#13 Check if a number is even or odd
def is_even(num):
    return num % 2 == 0
print(is_even(3))

#14 Simple sum
def addition(a, b):
    return a + b
result = addition(5, 4)
print(result)

#15 Pyramid pattern
def create_pyramid(rows):
    return [f"{'' * (rows - i)}{'*' * (2 * i - 1)}" for i in range(1, rows + 1)]

pyramis = create_pyramid(22)
for row in pyramis:
    print(row)

#16 Reverse a string
def reverse(string):
    return string[::-1]
print(reverse("hiesh gimno"))

#17 Check if array is empty
def is_not_empty(arr):
    return isinstance(arr, list) and len(arr) > 0
print(is_not_empty([1, 2, 3]))

#18 Matchstick count in steps
def match_houses(steps):
    return steps * 6 - (steps - 1) if steps > 0 else 0
print(match_houses(1))

#19 Shuffle an array
import random
def shuffle_array(arr):
    shuffled = arr[:]
    random.shuffle(shuffled)
    return shuffled
print(",".join(map(str, shuffle_array([1, 2, 3, 4]))))

#20 Validate vowel sandwich
def is_vowel_sandwich(string):
    return len(string) == 3 and string[0] not in 'aeiou' and string[1] in 'aeiou' and string[2] not in 'aeiou'
print((is_vowel_sandwich("bat")))

#21 Count true values in boolean array
def count_true(lst):
    return sum(1 for x in lst if x)
bool_array = [True, False, True, False, True]
count = count_true(bool_array)
print("Number of true values:", count)

#22 Get the length of a string
def get_length(string):
    return len(string)
print(get_length("Hello, World!"))

#23 Calculate the area of a circle
import math
def calculate_circle_area(radius):
    return math.pi * radius ** 2
print(calculate_circle_area(5))

#24 Move capital letters to front
def cap_to_front(s):
    return ''.join(filter(str.isupper, s)) + ''.join(filter(str.islower, s))
print(cap_to_front("MoveCapitalLettersToFront"))

#25 Check if an array is special
def is_special_array(arr):
    return all(arr[i] % 2 == i % 2 for i in range(len(arr)))
arr = [2, 3, 5, 8, 9]
print(is_special_array(arr))

#26 Validate number within bounds
def int_within_bounds(n, lower, upper):
    return lower <= n < upper and n % 1 == 0
print(int_within_bounds(10, 5, 20))

#27 Generate a random number within a range
import random
def random_in_range(min_val, max_val):
    return random.randint(min_val, max_val)
print(random_in_range(1, 10))

#28 Convert seconds to HH:MM:SS format
def seconds_to_hhmmss(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"
print(seconds_to_hhmmss((3667)))

#29 Get the last element of an array
def get_last_element(arr):
    return arr[-1]
print(get_last_element([1, 2, 3, 4]))

#30 Check if all elements in an array are the same
def test_jackpot(result):
    return len(set(result)) == 1
result = "22211"
print(test_jackpot(result))

#31 Jazzify chords
def jazzify(arr):
    return [x if str(x)[-1] == '7' else x + 7 for x in arr]
arr =[1, 2, 3, 4, 5, 6, 7, 8, 9]
jazzified_arr = jazzify(arr)
print(",".join(map(str, jazzified_arr)))

#32 Sum of numbers up to a given number
def add_up(num):
    return num * (num + 1) // 2
print(add_up(5))

#33 Sum all numbers in an array
def sum_array(arr):
    return sum(arr)
print(sum_array([1, 2, 3, 4, 5]))

#34 Find the macimum value in an array
def find_max(arr):
    return max(arr)
print(find_max([11, 5, 56, 53, 4]))

#35 Get the current date in dd/mm/yy format                            #TODO and 41
from datetime import datetime
def get_current_date():
    return datetime.now().strftime("%d/%m/%y")
print(get_current_date())

#36 Calculate the power of a number
def power(base, exponent):
    return base ** exponent
print(power(2, 5))

#37 Convert string to number
def string_to_number(string):
    return float(string)
print(string_to_number("3.14"))

#38 Marathon distance checker
def marathon_distance(distances):
    return sum(map(abs, distances)) >= 25
distances = [1, 2, -3, -6, 4, 5, 7, 7, -9, -6, 10]
print(marathon_distance(distances))

#39 Count the number of words in a string
def count_words(string):
    return len(string.split())
print(count_words("Hello world, how are you?"))

#40 Count ones in binary representation
def count_ones(n):
    return bin(n).count('1')
result = count_ones(12)
print(result)

#41 Get the current yeer                                                    #TODO and 35
from datetime import datetime
def current_year():
    return datetime.now().year
print(current_year())

#42 Generate a random number between 1 and 10
import random
def random_1_to_10():
    return random.randint(1, 10)
print(random_1_to_10())

#43 Check if a string is empty
def empty_string(string):
    return not string.strip()
print(empty_string(" "))

#44 Sum of index multiplied elements
def index_multiplier(arr):
    return sum(value * index for index, value in enumerate(arr))
arr = [1, 2, 3, 4, 5]
print(index_multiplier(arr))

#45 Calculate progress days
def progress_days(runs):
    return sum(runs[i] < runs[i + 1] for i in range(len(runs) -1 ))
runs = [3, 4, 1, 2, 4, 5]
print(progress_days(runs))

#46 Check if a number is a multiple of 5
def is_multiple_of_5(num):
    return num % 5 == 0
print((is_multiple_of_5(10)))

#47 Convert minutes to seconds
def mins_to_secs(mins):
    return mins * 60
print(mins_to_secs(5))

#48 Find the max value in an array of objects
def find_max_value(arr, key):
    return max(item[key] for item in arr)
arr = [
    {"name": "Alice",
     "score": 80},
    {"name": "Bob",
     "score": 95},
    {"name": "Charlie",
     "score": 70}
]
print(find_max_value(arr, "score"))

#49 Check if a string starts with a specific character
def starts_with_char(string, char):
    return string.lower().startswith(char.lower())
print(starts_with_char("Hello, world!", "H"))
print(starts_with_char("Hello, world!", "h"))

#50 Convert DNA to RNA
def dna_to_rna(dna):
    conversion = {'A':'U', 'T':'A', 'C':'G', 'G':'C'}
    return "".join(conversion.get(base,'') for base in dna)
print(dna_to_rna('ATTGC'))

#51 Check if an array contains a specific value
def contains_value(arr, value):
    return value in arr
print(contains_value([1,2,3,4,5], 3))

#52 Convert an array to a comma-separated string
def array_to_csv(arr):
    return ','.join(map(str, arr))
print(array_to_csv([1,2,3,4,5]))

print(','.join(map(str, [1,2,3,4,5])))

#53 Check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(is_leap_year(2024))

#54 Find the index of an element in an array
def find_index(arr, element):
    try:
        return arr.index(element)
    except ValueError:
        return -1

fruits = ['Apple', 'banana', 'orange', 'grape']
print(find_index(fruits, 'orange'))

#55 Convert minutes to hours and minutes
def mins_to_hours_and_mins(mins):
    return f'{mins // 60} hours and {mins % 60} minutes'
print(mins_to_hours_and_mins(150))

#56 Check if an array is sorted in ascending order
def is_sorted_ascending(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) -1))
print(is_sorted_ascending([1,2,3,4,7,9]))
print(is_sorted_ascending([1,2,34,5,6,78,98]))

#57 Remove a specific element from an array
def remove_element(arr, element):
    return [x for x in arr if x != element]
result = remove_element([1,2,3,4,5,], 3)
print(result)

#58 Truncate a string to a given length
def truncate_string(s, max_length):
    return s[:max_length] + '...' if len(s) > max_length else s
print(truncate_string("Hello, world!", 5))

#59 Convert video length from minutes to seconds
def minutes_to_seconds(time):
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(time.split(':'))))
print(minutes_to_seconds("02:54"))

#60 Find the difference between two dates in days
from datetime import datetime
def DateDifferenceInDays(date1, date2):
    return (date2 - date1).days
startDate = datetime(2023, 8, 1)
endDate = datetime(2023, 8, 10)
print(DateDifferenceInDays(startDate, endDate))

#61 Check if a string is a valid email address
import re
def isValiidEmail(email):
    return bool(re.match(r'^[^\5@] + @[^\5@] + \.[^\s@] + $', email))
print(isValiidEmail('user@example.com'))
print(isValiidEmail('garfielfinucky@gmail.com'))

#62 Convert seconds to minutes and seconds
def SecsToMinsAndSecs(seconds):
    return f"{seconds // 60} minutes and {seconds % 60} seconds"
print(SecsToMinsAndSecs(120))

#63 Generate a fibonacci sequence
def Fibonacci(n):
    return n if n <= 1 else Fibonacci(n - 1) + Fibonacci(n - 2)
fibonacci_sequence = [Fibonacci(i) for i in range(8)]
print(','.join(map(str, fibonacci_sequence)))

#64 Spelll out a word
def Spelling(word):
    return [word[:i+1] for i in range(len(word))]
word = 'example'
spelled_word = Spelling(word)
print(",".join(spelled_word))

#65 Check if an array contains only unique values
def HasUniqueValues(arr):
    return len(set(arr)) == len(arr)
print(HasUniqueValues([1,2,34,5,6,7,78,2]))

#66 Get the day of the week from a date
from datetime import datetime
def GetDayOfWeek(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%A')
print(GetDayOfWeek("2025-08-23"))

#67 Check if a number is a power of two
def IsPowerOfTwo(num):
    return num & (num - 1) == 0
print(IsPowerOfTwo(16))

#68 Generate multipication table
def GenerateMultiplicationTable(size):
    table = [[(row + 1) * (col + 1) for col in range(size)] for row in range(size)]
    return table
size = 5
multiplicationTable = GenerateMultiplicationTable(size)
for row in multiplicationTable:
    print(",".join(map(str, row)))

#69 Shhh whisperer
def Shhh(sentence):
    lowered = f'"{sentence[0].lower()}{sentence[1:].lower()}", whispered your friend.'
    return lowered
print(Shhh('HELLO THERE'))

#70 Get the month name from a date
import datetime
def GetMothName(date):
    return date.strftime("%B")
date = datetime.datetime(2025, 8, 23)
print(GetMothName(date))

#71 Find the bomb
import re
def Bomb(s):
    return "Duck!!!" if re.search(r'\bbomb\b', s, re.IGNORECASE) else "There in no bomb, relax."
s = "The bomb is about to explode"
print(Bomb(s))

#72 Convert feet to meters
def FeetToMeters(feet):
    return feet * 0.3048
print(FeetToMeters(10))

#73 Check if a numbers is a perfect square
def IsPerfectSquare(num):
    sqrt = num ** 0.5
    return sqrt.is_integer()
print(IsPerfectSquare(16))

#74 Check if a string contains only numbers
import re
def ContainsOnlyNumbers(s):
    return bool(re.match(r'^\d+$', s))
print(ContainsOnlyNumbers("12345"))

#75 Get the current month
from datetime import datetime
def CurrentMonth():
    return datetime.now().month #-1
print(CurrentMonth())

#76 Century from year
def CenturyFromYear(year):
    return (year + 99) // 100
print(CenturyFromYear(1905))
print(CenturyFromYear(1209))

#77 Check if a number is a prime number
def IsPrime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
print(IsPrime(13))

#78 Get the last n elements or an array
def LastNElements(arr, n):
    return arr[-n:]
result = LastNElements([1,2,3,4,5], 3)
print(",".join(map(str, result)))

#79 Convert degrees to radiand
import math
def DegToRad(degrees):
    return degrees * (math.pi / 180)

print(DegToRad(90))

#80 Bianry letter conberter
def ConvertBinary(s):
    return ''.join(['0' if 'a' <= c <= 'm' else '1' for c in s.lower()])
print(ConvertBinary("Hello"))

#81 Find the intersection of two arrays
def FindIntersection(arr1, arr2):
    return list(set(arr1) & set(arr2))
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
print(FindIntersection(arr1, arr2))

#82 Convert days to years, month, and days
def DaysToYearsMonthsDays(days):
    years = days // 365
    months = (days % 365) // 30
    days = (days % 365) % 30
    return years, months, days
print(DaysToYearsMonthsDays(400))

#83 Check if an object is empty
def IsEmptyObject(obj):
    return len(obj) == 0
print(IsEmptyObject({}))
print(IsEmptyObject({"name": "John", "age": 30}))

#84 Count decimal places
def GetDecimalPlaces(num):
    if "." in num:
        return len(num.split(".")[1])
    else:
        return 0
print(GetDecimalPlaces("3.14159"))
print(GetDecimalPlaces("100"))

#85 Remove whitespace from a string
def RemoveWhitespace(str):
    return "".join(str.split())
print(RemoveWhitespace("  Hello   World  "))

#86 Find the difference between two arrays
def ArrayDifference(arr1, arr2):
    return list(set(arr1) - set(arr2))
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
print(ArrayDifference(arr1, arr2))
difference = ArrayDifference(arr1, arr2)
print(",".join(map(str, difference)))

#87 Check if a number is a fibonacci number
def IsFibonacci(num):
    return IsPerfectSquare(5 * num * num + 4) or IsPerfectSquare(5 * num * num - 4)

def IsPerfectSquare(num):
    sqrt = int(num ** 0.5)
    return sqrt * sqrt == num
 
print(IsFibonacci(21))
print(IsFibonacci(6))
print(IsFibonacci(5))

#88 Convert hours to minutes
def HoursToMinutes(hours):
    return hours * 60
print(HoursToMinutes(2))

#89 Get the first n elements of an array
def FirstNElements(arr, n):
    return arr[:n]  
array = [1,2,3,4,5]
print(",".join(map(str, FirstNElements(array, 3))))

#90 Check if a number is odd
def is_odd(num):
    return num % 2 != 0 
print(is_odd(3))
print(is_odd(4))

#91 Calculate the standard deviation of an array of numbers
import math
def standard_deviation(arr):
    mean = sum(arr) / len(arr)
    sum_of_squared_differences = sum((x - mean) ** 2 for x in arr)
    return math.sqrt(sum_of_squared_differences / len(arr))
print(standard_deviation([10, 12, 23, 23, 16, 23, 21, 16]))

#92 Check if a string ends with a specific substring
def ends_with_substring(s, substring):
    return s.endswith(substring)
print(ends_with_substring("Hello, World!", "World!"))
print(ends_with_substring("Hello, World!", "Hello!"))

#93 Calculate the sum of squares of an array
def sum_of_squares(arr):
    return sum(x ** 2 for x in arr)
print(sum_of_squares([1, 2, 3, 4, 5]))

#94 Calculate pi to n decimal places
import math
def my_pi(n):
    return round(math.pi, n)
print(my_pi(5))

#95 Generate an array of random numbers
import random
def generate_array(length):
    return [random.randint(1, 100) for _ in range(length)]
print(generate_array(5))

#96 join path portions
def join_path(portion1, portion2):
    return f"{portion1.rstrip('/')}/{portion2.lstrip('/')}"
print(join_path("/home/user", "documents/file.txt"))

#97 Convert seconds to hours, minutes, and seconds
def seconds_to_hours_mins_secs(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    return f"{hours} hours, {minutes} minutes, and {seconds} seconds"
print(seconds_to_hours_mins_secs(3661))
print(seconds_to_hours_mins_secs(67))

#98 Simple calculator
def calculator(num1, op, num2):
    return {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else 'Division by zero error'
    }.get(op, 'Invalid operator')
print(calculator(10, '+', 5))
print(calculator(10, '/', 0))
print(calculator(10, '*', 5))
print(calculator(10, '-', 5))

#99 Find nemo
def find_nemo(sentence):
    words = sentence.split()
    index = words.index("Nemo") +1 if "Nemo" in words else -1
    return f"I found Nemo at {index}!" if index != -1 else "I can't find Nemo :("
print(find_nemo("I am finding Nemo !"))

#100 Count the occurrences of a character in a string
def count_occurrences(string, char):
    return string.lower().count(char.lower())
print(count_occurrences("Hello, World!", "o"))

#101 Convert video length to seconds
def minutes_to_seconds(time):
    minutes, seconds = map(int, time.split(':'))
    return minutes * 60 + seconds if 0 <= seconds < 60 else 0
print(minutes_to_seconds("02:30"))

#102 Remove duplicates from a string
def remove_duplicates_from_string(string):
    return ''.join(sorted(set(string), key=string.index))
print(remove_duplicates_from_string("hello world"))

#103 Find the mode of an array of numbers
def mode(arr):
    occurrences = {}
    for num in arr:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1
            max_occurrences = max(occurrences.values())
    return [num for num, count in occurrences.items() if count == max_occurrences]
numbers = [1, 2, 2, 3, 3, 3, 4]
print(f"Mode: {mode(numbers)}")

#104 Check for repdigit
def is_repdigit(num):
    return len(set(str(num))) == 1
print(is_repdigit(1111))
print(is_repdigit(1234))

#105 Convert binary number to decimal
def binary_to_decimal(binary):
    return sum(int(bit) * 2 ** index for index, bit in enumerate(reversed(binary)))
print(binary_to_decimal("1101"))

#106 Check if an array is sorted in descending order
def sorted_descending(arr):
    return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
print(sorted_descending([5, 4, 3, 2, 1]))
print(sorted_descending([5, 4, 3, 2, 2, 1]))
print(sorted_descending([1, 2, 3, 4, 5]))

#107 Find the average of even number in an array
def average_of_even_numbers(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    return sum(even_numbers) / len(even_numbers) if even_numbers else 0
print(average_of_even_numbers([1, 2, 3, 4, 5]))
print(average_of_even_numbers([1, 3, 5]))

#108 Capitalize the first letter of each word in a string
def capitalize_words(string):
    return ' '.join(word.capitalize() for word in string.split())
print(capitalize_words("hello world! this is python."))
print(capitalize_words("python is awesome."))

#109 Check if an array is a subset of another array
def is_subset(arr1, arr2):
    return all(item in arr2 for item in arr1)
print(is_subset([1, 2], [1, 2, 3, 4, 5]))
print(is_subset([1, 6], [1, 2, 3, 4, 5]))

#110 Find the minimum and maximum elements in an array
def min_max(arr):
    return min(arr), max(arr) if arr else (None, None)
result = min_max([1, 2, 3, 4, 5])
print(f'{{min: {result[0]}, max: {result[1]}}}')
print(min_max([1, 2, 3, 4, 5]))
print(min_max([43, 34, 54, 6, 23]))

#111 Validate zip code
import re
def is_valid(zip_code):
    return bool(re.match(r'^\d{5}(-\d{4})?$', zip_code))
print(is_valid("12345"))
print(is_valid("12345-6789"))
print(is_valid("1234"))

#112 Validate email address                                                                                      #ToDo: Find email
def is_valid_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))
print(is_valid_email("garfieldfinucky@gmail.com"))
print(is_valid_email("invalid-email"))

#113 Remove null values from a list
def remove_null(arr):
    return [item for item in arr if item is not None]
array = [1, 2, None, 4, None, 5]
print(f"Array without nulls: {remove_null(array)}")

#114 Maurice`s racing snails
def maurice_wins(m_snails, s_snails):
    wins = sum(m > s for m, s in zip(m_snails, s_snails))
    return wins >= 2
print(maurice_wins([1, 2, 3], [2, 3, 4]))

#115 Calculate the sum of cubes of an array
def sum_of_cubes(arr):
    return sum(x ** 3 for x in arr)
arr = [1, 2, 3, 4, 5]
print(f"Sum of cubes: {sum_of_cubes(arr)}")

#116 Shuffle the characters of a string
import random
def shuffle_string(s):
    shuffle_chars = list(s)
    random.shuffle(shuffle_chars)
    return ''.join(shuffle_chars)
s = 'Hello'
shuffled_string = shuffle_string(s)
print(f"Shuffled string: {shuffled_string}")

#117 Find the nth fibonacci number
def fibonacci(n):
    if n <= 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = 7
result = fibonacci(n)
print(f"Fibonacci({n}): {result}")

#118 Symmetry checker
def is_symmetrical(num):
    return str(num) == str(num)[::-1]
num = 12321
print(is_symmetrical(num))

#119 Maximum triangle edge calculator
def next_edge(side1, side2):
    return (side1 + side2) - 1
side1 = 5
side2 = 7
print(f"Next edge length: {next_edge(side1, side2)}")

#120 Calculate the perimeter of a rectangle
def rectangle_perimeter(width, height):
    return 2 * (width + height)
print(rectangle_perimeter(5, 10))

#121 Find the longest common prefix in an array of string
def longest_common_prefix(strs):
    return "" if not strs else "".join(c for i, c in enumerate(strs[0]) if all(s[i] == c for s in strs))
strs = ["apple", "apricot", "banana"]
print(longest_common_prefix(strs))

#122 Greeting function with conditional message
def say_hello_bye(name, num): 
    return f"Hello {name.capitalize()}" if num == 1 else f"Bye {name.capitalize()}"
name = "Alice"
num = 2
print(say_hello_bye(name, num))

#123 Find the first non-repeating character in a string
def first_non_repeating_char(s):
    return next((c for c in s if s.count(c) == 1), None)
s = "abacasbad"
print(first_non_repeating_char(s))

#124 One-liner bitwise operations in python
def bitwise_operations(a, b):
    return {
        'AND': a & b,
        'OR': a | b,
        'XOR': a ^ b,
        'NOT a': ~a,
        'NOT b': ~b
    }
print(bitwise_operations(5, 3))

#125 Calculate the exponential of a number
def exponential(base, exponent):
    return base ** exponent
result = exponential(2, 3)
print(f"Exponential result: {result}")

#123 Find the first non-repeating character in a string
def first_non_repeating_char(s):
    return next((c for c in s if s.count(c) == 1), None)
s = "abacasbad"
print(first_non_repeating_char(s))

#124 One-liner bitwise operations in python
def bitwise_operations(a, b):
    return {
        'AND': a & b,
        'OR': a | b,
        'XOR': a ^ b,
        'NOT a': ~a,
        'NOT b': ~b
    }
print(bitwise_operations(5, 3))

#125 Calculate the exponential of a number
def exponential(base, exponent):
    return base ** exponent
result = exponential(2, 3)
print(f"Exponential result: {result}")

#126 Check if a string is an anagram of another string
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))

#127 Compact phone number formatter
def format_phone_number(numbers):
    return "(+{}{}{}) {}{}{}-{}{}{}{}".format(*numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(format_phone_number(numbers))

#128 Check if a number is a neon number
def is_neon_number(num):
    sum_of_digits = 0
    square = num * num
    while square:
        sum_of_digits += square % 10
        square //= 10
    return sum_of_digits == num
print(is_neon_number(9))

#129 Recursive right shift mimicker
def shift_to_right(x, y):
    return x if y < 1 else shift_to_right(x // 2, y - 1)
x = 16
y = 2
print(shift_to_right(x, y))

#130 Check if a number is a disarium number
def is_disarium_number(num):
    num_str = str(num)
    disarium_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    return disarium_sum == num
print(is_disarium_number(135))
print(is_disarium_number(123))

#131 Remove vowels from a string
import re
def remove_vowels(s):
    return re.sub(r'[aeiouAEIOU]', '', s)
print(remove_vowels("Hello, World!"))

#132 Generate an array of consecutive numbers
def consecutive_numbers(start, end):
    return list(range(start, end + 1))
result = consecutive_numbers(5, 10)
print(",".join(map(str, result)))

#133 Check if a number is a pronic number
def is_pronic_number(num):
    n = int(num ** 0.5)
    return n * (n + 1) == num
print(is_pronic_number(6))
print(is_pronic_number(10))

#134 Check if a string is a pangram
def is_pangram(s):
    letters = set(c.lower() for c in s if c.isalpha())
    return len(letters) == 26
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello, World!"))

#135 Reverse the order of words in a sentence
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
print(reverse_sentence("Hello, how are you doing?"))

#136 Calculate the hypotenuse of a right-angled triangle
import math
def calculate_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)
print(calculate_hypotenuse(3, 4))

#137 Find the aberage of odd numbers in an array
def aberage_of_odd_numbers(arr):
    odd_numbers = [num for num in arr if num % 2 != 0]
    return sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0
numbers = [1, 2, 3, 4, 5]
print(aberage_of_odd_numbers(numbers))

#138 Count the letters in a string
def count_letters(s):
    return {char: s.lower().count(char) for char in s.lower() if char.isalpha()}
input_string = "Hello, World!"
result = count_letters(input_string)
for char, count in result.items():
    print(f"{char} => {count}")

#139 Convert seconds to days, hours, minutes, and seconds
def secs_to_days_hours_mins_secs(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds"
print(secs_to_days_hours_mins_secs(100000))

#140 Check if a number is a prime factor of another number
def is_prime_factor(num, factor):
    return num % factor == 0 and all(factor % i != 0 for i in range(2, int(factor ** 0.5) + 1)) and factor > 1
num = 28
factor = 7
print(is_prime_factor(num, factor))

#141 Find the second largest prime factor of a number
def largest_prime_factor(num):
    if num == 1:
        return 1
    factor = next((x for x in range(2, int(num ** 0.5) + 1) if num % x == 0 and all(x % y != 0 for y in range(2, int(x ** 0.5) + 1))), 0)
    return num if factor == 0 else factor
print(largest_prime_factor(13195))

#142 Check if a number is a pronic square
def is_pronic_square(num):
    sqrt = num ** 0.5
    return sqrt  == int(sqrt)
print(is_pronic_square(36))
print(is_pronic_square(20))

#143 World landmass proportion calculator
def area_of_country(name, area):
    return f"{name} is {area * 100 / 148940000:.2f}% of the total world's landmass"
country_name = "Finland"
country_area = 338424
print(area_of_country(country_name, country_area))

#144 Loaded die detection
def is_unloaded(frequencies):
    return sum(f * (i + 1) ** (f - 1) for i, f in enumerate(frequencies)) > 11.0705
frequencies = [1, 1, 1, 1, 1, 1]
print(is_unloaded(frequencies))

#145 Hand washing duration calculator
def wash_hands(n, nm):
    total_seconds = nm * n * 21 * 30
    minutes = total_seconds // 60
    seconds = total_seconds % 60    
    return f"{minutes} minutes and {seconds} seconds"
n = 3
nm = 2
print(wash_hands(n, nm))

#146 Billable days bonus calculator
def calculate_bonus(days):
    return 325 * max(days - 32, 0) + 225 * max(days - 40, 0) + 50 * max(days - 48, 0)
billable_days = 45
bonus = calculate_bonus(billable_days)
print(f"Bonus for {billable_days} billable days: ${bonus}")

#147 Check if a number is a happy number
def is_happy_number(num):
    return num == 1 or num == 7 or num == 10 or (num < 100 and num % 10 == 0 and num % 11 == 0) or (num < 1000 and num % 100 == 0 and num % 111 == 0)
print("true" if is_happy_number(19) else "false")

#148 Calculate the volume of a sphere
import math
def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3
volume = sphere_volume(5)
print(volume)

#149 Discounted price calculator
def calculate_final_price(price, discount):
    return price * (100 - discount) * 0.01
final_price = 100
discount = 20
discounted_price = calculate_final_price(final_price, discount)
print(f"Final price after {discount}% discount: ${discounted_price:.2f}")

#150 Double letter checher
import re 
def has_double_letters(word):
    return bool(re.search(r"(\w)\1", word))
word = "book"
print(f"Has double letters in '{word}': {has_double_letters(word)}")
word = "cat"
print(f"Has double letters in '{word}': {has_double_letters(word)}")

#151 Find the length of the longest word in a sentence
def longest_word_length(sentence):
    return max(len(word) for word in sentence.split())
sentence = "The quick brown fox jumps over the lazy dog"
print(longest_word_length(sentence))

#152 Stolen items loss calculator
def calculate_losses(stolen_item):
    total_value = sum(stolen_item.values())
    return "Lucky you!" if total_value == 0 else f"You have lost {total_value}$."
stolen_item = {"tv": 300, "stereo": 100, "laptop": 800}
losses = calculate_losses(stolen_item)
print(f"Losses: {losses}")

#153 Hacker speak converter
import re
def convert_to_hacker_speak(input_str):
    return re.sub('[aeios]', lambda x: '4' if x.group() == 'a' else '3' if x.group() == 'e' else '1' if x.group() == 'i' else '0' if x.group() == 'o' else '5', input_str, flags=re.IGNORECASE)
input_str = "Hello, how are you?"
hacker_speak = convert_to_hacker_speak(input_str)
print(f"Original: {input_str}")
print(f"Hacker Speak: {hacker_speak}")

#154 Find the area of a rectangle
def rectangle_area(length, width):
    return length * width
length = 5
width = 10
area = rectangle_area(length, width)
print(f"Area of rectangle: {area}")

#155 Calculate the sum of even numbers in an array
def sum_of_even_numbers(arr):
    return sum(num for num in arr if num % 2 == 0)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum_of_even_numbers(arr)
print(f"Sum of even numbers: {total}")

#156 Calculate the volume of a cylinder
import math
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height
volume = cylinder_volume(5, 10)
print(f"Volume of cylinder: {volume}")

#157 Bbq slewer analyzer
def bbq_slewers(grill):
    vegetarian_count = sum(1 for item in grill if "-x" not in item)
    meat_count = len(grill) - vegetarian_count
    return [vegetarian_count, meat_count]
grill = ["-o", "-o", "-x", "-o", "-x"]
result = bbq_slewers(grill)
print(f"Vegetarian: {result[0]}, Meat: {result[1]}")

#158 Missing number finder
def find_missing_number(arr):
    return 55 -  sum(arr)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,]
missing_number = find_missing_number(numbers)
print(f"Missing number: {missing_number}")

#159 Convert decimal number to octal
def decimal_to_octal(num):
    return oct(num).lstrip("0o")
print(decimal_to_octal(65))
print(decimal_to_octal(8))

#160 Collatz sequence analyzer
def collatz(num):
    count = 0
    while num != 1:
        num = num // 2 if num % 2 == 0 else 3 * num + 1
        count += 1
    return count
num = 27
steps = collatz(num)
print(f"Collatz steps for {num}: {steps}")

#161 Check if a string is a valid phone number 
import re 
def is_valid_phone_number(phone):
    return bool(re.match(r'^\(\d{3}\) \d{3}-\d{4}$', phone))
print(is_valid_phone_number("(123) 456-7890"))
print(is_valid_phone_number("123-456-7890"))

#162 Find the sum of the first n natural numbers
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2 
print(sum_of_natural_numbers(10))
print(sum_of_natural_numbers(100))

#163 Vowel dasher
import re 
def dashed(string):
    return re.sub(r'[aeiouAEIOU]', lambda x: '-' if x.group() else x.group(), string)
print(dashed("Hello World"))
print(dashed("Python is fun"))

#164 Find the factors of a number
def factors(num):
    result = []
    for i in range(2, num):
        if num % i == 0:
            result.append(i)
    return result
print(",".join(map(str, factors(28))))
print(",".join(map(str, factors(15))))

#165 Calculate the area of a triangle  given the base and height
def triangle_area(base, height):
    return 0.5 * base * height
area = triangle_area(5, 10)
print(f"Area of triangle: {area}")

#166 Check if a string is a valid social security number
import re 
def is_valid_ssn(ssn):
    return bool(re.match(r'^\d{3}-\d{2}-\d{4}$', ssn))
print(is_valid_ssn("123-45-6789"))
print(is_valid_ssn("123-456-789"))

#167 Generate an array pf random numbers within a range
import random 
def rando_array_in_range(min_val, max_val, length):
    return [random.randint(min_val, max_val) for _ in range(length)]
print(rando_array_in_range(1, 100, 5))
print(rando_array_in_range(50, 150, 10))

#168 XO checker
def xo_checker(string):
    x_count = string.lower().count('x')
    o_count = string.lower().count('o')
    return x_count == o_count
print(xo_checker("fsdxXoOsd"))
print(xo_checker("sdfxXoOa"))

#169 Check if a string is a valid ipv4 address
import re
def is_valid_ipv4(ip):
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(pattern, ip))
print(is_valid_ipv4("192.168.1.1"))
print(is_valid_ipv4("256.256.256.256"))

#170 Convert decimal number to hexadecimal
def decimal_to_hex(num):
    return hex(num).lstrip("0x").upper()
print(decimal_to_hex(255))
print(decimal_to_hex(16))
print(decimal_to_hex(4095))

#171 Check if a string is a valid date
import re
def is_valid_date(date):
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', date))
print(is_valid_date("2023-08-23"))
print(is_valid_date("23-08-2023"))

#172 Chinese zodiac sign identifier
def get_chinese_zodiac(birth_year):
    zodiac_signs = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]
    return zodiac_signs[birth_year % 12]
print(get_chinese_zodiac(1990))
print(get_chinese_zodiac(2023))
print(get_chinese_zodiac(1999))

#173 Check is a string is a valid password
import re
def is_valid_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{4,16}$'
    return bool(re.fullmatch(pattern, password))
print(is_valid_password("61kd*"))
print(is_valid_password("<ss@5&+-iH_ih^>O"))
print(is_valid_password("n65\/N.v"))

#174 Find the NTH fibonacci number 
def fibonacci(n):
    return n - 1 if n <= 2 else fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))

#175 Diving minigame checker
def diving_minigame(arr):
    return bool((lambda score: next((False for score_change in arr if score <= 0 or (score_change < 0 and (score:= max(0, score - 2)) < 1) or (score_change >= 0 and (score:= min(score + 4, 10)) > 0)), True))(10))
print(diving_minigame([1, -1, -1, 1, 1, -1, -1, -1, 1, 1]))
print(diving_minigame([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]))
print(diving_minigame([3, 4, 545, 45, 65, 76, 8, 9, 5, 34, ]))

#176 Roger`s shooting score calculator
def roger_shots(arr):
    return sum(0.5 for shot in arr if shot in ["Bang!", "BangBang!"])
print(roger_shots(["Bang!", "Miss", "BangBang!", "Bang!"]))
print(roger_shots(["Miss", "Miss", "Miss"]))
print(roger_shots(["BangBang!", "BangBang!", "Bang!", "Bang!", "Bang!"]))

#177 Middle character of string
def get_middle(s):
    mid = len(s) // 2
    return s[mid] if len(s) % 2 != 0 else s[mid - 1: mid + 1]
print(get_middle("testing"))
print(get_middle("middle"))

#178 Calculate the volume of a cube
def cube_volume(side):
    return side ** 3
print(cube_volume(3))
print(cube_volume(5))

#179 Check if a string is a valid credit card number
import re
def is_valid_credit_card(card_number):
    regex = re.compile(r'^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|6(?:011|5[0-9]{2})[0-9]{12}|(?:2131|1800|35\d{3})\d{11})$')
    return bool(regex.match(card_number.replace(" ", "").replace("-", "")))
print(is_valid_credit_card("4539 1488 0343 6467"))
print(is_valid_credit_card("6011-0009-9013-9424"))

#180 Calculate the perimeter of a triangle
def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3
print(triangle_perimeter(3, 4, 5))
print(triangle_perimeter(5, 12, 13))

#181 Check if a number is a vampire number
def is_vampire_number(num):
    num_str = str(num)
    num_len = len(num_str)
    for factor1 in range(10 ** (num_len // 2 - 1), int(num ** 0.5) + 1):
        if num % factor1 == 0:
            factor2 = num // factor1
            if len(str(factor2)) == num_len // 2 and not (str(factor1).endswith('0') and str(factor2).endswith('0')):
                if sorted(str(factor1) + str(factor2)) == sorted(num_str):
                    return True
    return False
print(is_vampire_number(1260))
print(is_vampire_number(1234))

#182 Obsolete sum converter
def get_abs_sum(arr):
    return sum(abs(num) for num in arr)
print(get_abs_sum([-1, -2, 3, 4, -5]))
print(get_abs_sum([-10, -20, -30]))

#183 Check if a number is a duck number
def is_duck_number(num):
    num_str = str(num)
    return '0' in num_str and num_str[0] != '0'
print(is_duck_number(1023))
print(is_duck_number(5345435))

#184 Generate a random password
import random, string

def random_password(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
print(random_password(8))

#185 Calculate the area of a trapezoid
def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height
print(trapezoid_area(4, 8, 6))

#186 Check if a number is a kaprekar number
def is_kaprekar_number(num):
    square = num ** 2
    square_str = str(square)
    num_str = str(num)
    left = int(square_str[:len(num_str)])
    right = int(square_str[-len(num_str):])
    return left + right == num
print(is_kaprekar_number(9))
print(is_kaprekar_number(34))

#187 Calculate the volume of a cone
import math
def cone_volume(radius, height):
    return (1/3) * math.pi * radius ** 2 * height
print(cone_volume(5, 10))
print(cone_volume(33, 444))

#188 Check if a string is a valid us phone number(US)
import re
def is_valid_us_phone_number(phone):
    pattern = r"^(?:(?:\+1\s?)?(?:\(\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4})$"
    return bool(re.match(pattern, phone))
print(is_valid_us_phone_number("+1 (123) 456-7890"))
print(is_valid_us_phone_number("123-456-7890"))

#189 Sastry number checker
import math
def is_sastry(num):
    return math.sqrt(int(str(num) + str(num + 1))) % 1 == 0
print(is_sastry(183))
print(is_sastry(184))

#190 Factor chain checker
def factor_chain(arr):
    return all(arr[i + 1] % arr[i] == 0 for i in range(len(arr) - 1))
chain1 = [1,2,4,5,7,8]
chain2 = [4,6,7,8,2,5]
print(factor_chain(chain1))
print(factor_chain(chain2))

#191 Calculate boxes in algebra sequence
def box_seq(step):
    return step + (step % 2 * 2)
print(box_seq(5))
print(box_seq(8))

#192 Calculate the volume of a cuboid
def cuboid_volume(lenght, width, height):
    return lenght * width * height
volume = cuboid_volume(5, 10, 8)
print("Volume of the cuboid:", volume)

#193 Triangular number sequence
def triangular(n):
    return n * (n + 1) // 2
print("Triangular equals:", triangular(1), "\n--input data--\n\t->1<-")
print("Triangular equals:", triangular(2), "\n--input data--\n\t->2<-")
print("Triangular equals:", triangular(5), "\n--input data--\n\t->5<-")

#194 Generate a random color
import random
def random_color_hex():
    return '#{0:06x}'.format(random.randint(0, 0xFFFFFF))
print("Your color:", random_color_hex())

#195 Calculate the area of a circle sector
import math
def circle_sector_area(radius, angle):
    return (angle/360) * math.pi * radius ** 2
print("Radius:", circle_sector_area(5, 90), "\n--input data--\n\t->5, 90<-")

#196 Calculate the area of a regular polygon
import math
def regular_polygon_area(side_length, num_of_sides):
    return (num_of_sides * side_length ** 2) / (4 * math.tan(math.pi / num_of_sides))
print("Poligon area:", regular_polygon_area(5, 6), "\n--input data--\n\t->5, 6<-")

#197 Remove duplicates from array
def remove_duplicates(arr):
    return list(dict.fromkeys(arr))
array = [1,2,3,4,5,6,7,7,7,1,1,9,0,9]
result = remove_duplicates(array)
print("Array without duplicates:", ", ".join(map(str, result)), f"\n--input data-->{array}")

#198 Calculate the area of an ellipse
import math
def ellipse_area(a, b):
    return math.pi * a * b
print(ellipse_area(5, 10))
print(ellipse_area(10, 20))

#199 Check if a number is a leyland number
def is_leyland_number(num):
    for x in range(2, int(num ** (1/3)) + 1):
        for y in range(x + 1, num // x + 1):
            if x ** y + y ** x == num:
                return True
            return False
print(is_leyland_number(17))
print(is_leyland_number(30))

#200 Generate a random uuid
import random, string
def random_uuid():
    random_hex = lambda length:''.join(random.choice(string.hexdigits) for _ in range(length))
    return f"{random_hex(8)}-{random_hex(4)}-4{random_hex(3)}-{random_hex(4)}-{random_hex(12)}".lower()
print(random_uuid())

#201 Check if a string is a valid ipv6 address
import re
def is_valid_ipv6(ip):
    pattern = r"^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    return bool(re.match(pattern, ip))
print(is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
print(is_valid_ipv6("2001:0db8:85a3::8a2e:0370:7334"))

#202 Calculate the area of a parallelogram
def parallelogram_area(base_length, height):
    return base_length * height
print(parallelogram_area(5, 10))

#203 Check if a string is a valid mac address
import re
def is_valid_mac_address(mac):
    pattern = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
    return bool(re.match(pattern, mac))
print(is_valid_mac_address("00:1A:2B:3C:4D:5E"))
print(is_valid_mac_address("00:1A:2B:3C:4D"))

#204 Convert rgb to hsl(hue, saturation, lightness)
import colorsys
def rgb_to_hsl(rgb):
    r, g, b = rgb
    h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    return h * 360, s * 100, l * 100
rgb_value = (255, 0, 0) #Red color
hsl_value = rgb_to_hsl(rgb_value)
print(hsl_value)

#205 Check if a number is a pandigital number
def is_pandigital_number(num):
    num_str = str(num)
    return len(set(num_str)) == len(num_str) and '0' not in num_str and max(num_str) == str(len(num_str))
print(is_pandigital_number(123456789))

print(is_pandigital_number(987654321))
