with open('task_10.1.txt') as file_object:
    massage = file_object.readlines()

for line in massage:
    print(line.strip())
