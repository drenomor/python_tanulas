#!/usr/bin/env python3

# Logikai operátorok - Logical (boolean) operators

# and, or, not - java (&&, ||, !)

number1 = 6
number2 = 72

print("# and igazság táblája\n")
print("TRUE and TRUE =", True and True)
print("TRUE and FALSE =", True and False)
print("FALSE and TRUE =", False and True)
print("FALSE and FALSE =", False and False)

print("\n# or igazság táblája\n")
print("TRUE or TRUE =", True or True)
print("TRUE or FALSE =", True or False)
print("FALSE or TRUE =", False or True)
print("FALSE or FALSE =", False or False)

print("\n# not igazság táblája\n")
print("NOT TRUE =", not True)
print("NOT FALSE =", not False, "\n")

print("6 < 72 and 6 == 5  ->", number1 < number2 and number1 == 5, "\n")
print("6 < 72 or 6 == 6 and -1 > 0  ->", number1 < number2 or number1 == 6 and -1 > 0, "\n")
print("6 < 72 and 6 == 6  ->", number1 < number2 and number1 == 6, "\n")
print("6 < 72 and not 6 == 6  ->", number1 < number2 and not number1 == 6, "\n")
