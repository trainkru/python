def grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

myfile = open("data.txt")

for line in myfile:
    data = line.split()
    name = data[0]
    quiz = int(data[1])
    midterm = int(data[2])
    final = int(data[3])
    print(name, grade(quiz+midterm+final))

myfile.close()
