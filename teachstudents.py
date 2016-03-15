lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for element in students:
    print(element["name"])
    print(element["homework"])
    print(element["quizzes"])
    print(element["tests"])


def average(numbers):
    # sum of the number
    total = sum(numbers)
    # making the integer a float
    total = float(total)
    # find average
    total /= len(numbers)
    # return results
    return total


def get_average(student):
    # average of homework, quizzes and tests
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    # calculate weighted average
    return 0.1 * average(student["homework"]) + 0.3 * average(student["quizzes"]) + 0.6 * average(student["tests"])


print(get_average(lloyd))
print(get_average(alice))
print(get_average(tyler))
