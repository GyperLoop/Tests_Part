#1 Convert Celsius to Fahrengeit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

print(celsius_to_fahrenheit(25))                        #TODO:  77.0

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

#95 Generate an array of random numbers
import random
def generate_array(length):
    return [random.randint(1, 100) for _ in range(length)]
print(generate_array(5))

print(my_pi(5))

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


