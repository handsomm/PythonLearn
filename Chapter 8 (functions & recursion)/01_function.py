def percent(marks):
    # return ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return sum(marks)/4


marks1 = [45, 78, 86, 77]
percentage = percent(marks1)

marks2 = [55, 40, 50, 70]
percentage2 = percent(marks2)

print(percentage, percentage2)
