import csv


csvfile_write = open('students.csv', 'a', newline='')

students = [{'chat_id': 'K', 'uname': 22},
            {'chat_id': 'A', 'uname': 21, 'pword': 56},
            {'chat_id': 'J', 'uname': 20, 'pword': 60}
            ]
# DICT WRITER
fields = ['chat_id', 'uname', 'pword']
writer_obj = csv.DictWriter(csvfile_write, fieldnames=fields)
writer_obj.writeheader()
for student in students:
    writer_obj.writerow(student)
writer_obj.close()

'''
students = [['L', 22, 45],
            ['A', 12, 54],
            ['B', 21, 44]
            ]
# NORMAL WRITER
writer_obj = csv.writer(csvfile_write)
for student in students:
    writer_obj.writerow(student)
'''
s = "K"
csvfile_read = open('students.csv', 'r', newline='')
reader_obj = csv.DictReader(csvfile_read)
for row in reader_obj:
    if row['chat_id'] == s:
        row['pword'] = 42
