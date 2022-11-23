with open('task_10.1.txt') as file_object:
    massage = file_object.readlines()

lange = input('enter your favorite programming language: ')
for line in massage:
    print(line.replace('Python', lange).strip())