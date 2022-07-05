number_of_students = int(input("Enter Number Of Students: "))
number_of_subjects = int(input("Enter Number Of Subject: "))
count = 0
student_list = []
subject_list = [input(f'Enter Subject {i + 1}: ') for i in range(number_of_subjects)]


while count != number_of_students:
    name = input("Enter Student Name: ")
    subject_score = [int(input(f"{name}'s score for {subject_name}: ")) for subject_name in subject_list]
    total = sum(subject_score)
    average = total / number_of_subjects
    student = {
        'Name': name,
        'Subject scores': subject_score,
        'Total': total,
        'Average': average

    }

    student_list.append(student)
    count += 1
    print()

average_scores = [i['Average'] for i in student_list]
total_scores = [i['Total'] for i in student_list]
subject_name = [i['Name'] for i in student_list]
scores = [i['Subject scores'] for i in student_list]

def prt(a: list):
    for i in a:
        print(f'{i:>8}', end=' ')
    pass

pos = []
for i in total_scores:
    cou = 1
    for j in total_scores:
        if j > i:
            cou += 1
        else:
            cou = 1
        pos.append(cou)

print('=' * 40 + '\n' '\tWELCOME TO SILICON VALLEY\n'   '231 Black Drive, Bay Central.\n' + '=' * 40)
print(f'Student', end=' ')

for i in subject_list:
    print(f''
          f'{1:>7}', end='')
a, b, c = 'Total', 'Average', 'Position'
print(f'{a:>7} {b:>7} {c:>7}')
for i in range(0, len(student_list)):
    print(f'{subject_name[i]}', end='')
    prt(scores[i])
    print(f'{total_scores[i]:>8} {average_scores[i]:>7} {pos[i]}')