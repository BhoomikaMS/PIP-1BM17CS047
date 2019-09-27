class Student:
	def __init__(self):
		self.s_id=None
		self.age=None
		self.marks=None

	def validate_marks(self):
		if self.marks>=0 and self.marks<=100:
			return True
		else:
			return False
	
	def validate_age(self):
		if self.age>20:
			return True
		else: 
			return False

	def check_qualification(self):
		if self.validate_marks() and self.validate_age():
			if self.marks>=65:
				return True
			else:
				return False
		else:
			return False
	
	def setinfo(self):
		sid=input("Enter student id: ")
		a=input("Enter the age: ")
		m=input("Enter the marks scored in qualifying exam: ")
		self.s_id=sid
		self.age=int(a)
		self.marks=int(m)

	def getinfo(self):
		print("Student ID: ",self.s_id)
		print("Age: ",self.age)
		print("Marks: ",self.marks)
	
if __name__=="__main__":
	n=int(input("Enter the number of students: "))
	s=[]
	for i in range(n):
		print("Enter the details of student ",i+1)
		s.append(Student())
		s[i].setinfo()
		print()
			
	print("Qualified students:")
	for i in range(n):
		if s[i].check_qualification():
			s[i].getinfo()
			print()

