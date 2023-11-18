subjects = {'python': 5, 'java': 9}
print(subjects)
print(subjects['java']) # access
subjects['go'] = 7 # add
print(subjects)
subjects['java'] = 8 #update
print(subjects)

for subjects in subjects:
    print(subjects)

for subjects in subjects.items():
    print(subjects)

for subject, students in subjects.items():
    print(subjects, students)
    print(f" {subject} 과목을 수강하는 학생의 인원은  {students}명 입니다")

del subjects['java'] # delete
print(subjects)

