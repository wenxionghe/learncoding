n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# there are 2 sets of numbers, first we need to join the individual numbers within the set, and then join the 2 sets together

# Add your function here
def flatten(lists):
    # make a list called 'results'
    results = []
    for numbers in lists:
        # join the 2 sets together
        for i in numbers:
            # join the number within the set
            results.append(i)
    return results


print(flatten(n))
