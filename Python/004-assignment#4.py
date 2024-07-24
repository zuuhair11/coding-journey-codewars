class HandleFile:
    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def __read_file(self) -> dict:
        students: dict = {}

        with open(self.__filename, mode='r') as file:
            for line in file:
                if 'Student ID,Student Name,Course,Grade' in line:
                    continue

                parts = line.strip().split(',')
                students[parts[0]] = tuple(parts[1:])

        return students
    
    def __create_file(self, students: dict, new_filename: str) -> None:
        with open(new_filename + '.csv', mode='w') as file:
            file.write('Student ID,Student Name,Course,Grade\n')

            for student_id, values in students.items():
                line = student_id + ',' + ','.join(values)
                file.write(line + '\n')

    def sort_file(self, new_filename: str) -> None:
        students: dict = self.__read_file()
        sorted_students = sorted(students.items(), key=lambda student: student[1][-1], reverse=True)

        self.__create_file(dict(sorted_students), new_filename)
        
        print('=' * 20)
        print('======= Done! ======')
        print('=' * 20)


if __name__ == '__main__':
    students: HandleFile = HandleFile('004student-master-list.csv')
    students.sort_file('004-new_sorted_students')
