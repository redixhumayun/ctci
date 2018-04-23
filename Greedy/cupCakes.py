import pdb

def totalCalories(n, calories):
    calories = reversed(sorted(calories))
    miles = 0
    for index, value in enumerate(calories):
        miles += (2**index) * value
    return miles

if __name__ == "__main__":
    n = 2
    calories = [1,3,2]
    result = totalCalories(n, calories)
    assert result == 11
