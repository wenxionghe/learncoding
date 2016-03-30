grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades): #print all grades in individual line
    for grade in grades:
        print(grade)

def grades_sum(scores): #sum of all scores
    total = 0
    for n in scores:
        total += n
    return total

def grades_average(grades): #average of all scores
    avg = grades_sum(grades) / float(len(grades)) 
    return avg

def grades_variance(scores): # variance of all scores
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += ((average - score) ** 2) / float(len(scores))
    return variance

def grades_std_deviation(variance): # standard deviation
    return variance ** 0.5

variance = grades_variance(grades) #variance is now a global variable

print(print_grades(grades))
print("Sum:", grades_sum(grades))
print("Average", grades_average(grades))
print("Variance", grades_variance(grades))
print("Standard Deviation", grades_std_deviation(variance)) 