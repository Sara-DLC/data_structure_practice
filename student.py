class Student:
    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already enrolled in {course}")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not in course list")

    def find_in_file(self, filename):
        with open(filename) as f:
            for line in f:
                first_name, last_name, course_details = Student.prep_record(
                    line.strip())
                student_read_in = Student(
                    first_name, last_name, course_details)
                if self == student_read_in:
                    return True
            return False

    def add_to_file(self, filename):
        if self.find_in_file(filename):
            return "Record already exist"
        else:
            record_to_add = Student.prep_to_write(
                self.first_name, self.last_name, self.courses)
            with open(file_name, "a+") as to_write:
                to_write.write(record_to_add+"\n")
            return "Record Added"

    @staticmethod
    def prep_record(line):
        line = line.split(":")
        first_name, last_name = line[0].split(",")
        course_details = line[1].rstrip().split(",")
        return first_name, last_name, course_details

    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        full_name = first_name+','+last_name
        courses = ','.join(courses)
        return full_name+':'+courses

    def __eq__(self, other):
        return self.first_name == other.first_name \
            and self.last_name == other.last_name

    def __len__(self):
        return len(self.courses)


file_name = "data.txt"
new_student = Student("john", "danvers", ["python", "ruby", "javascript"])
print(new_student.find_in_file(file_name))
print(new_student.add_to_file(file_name))
