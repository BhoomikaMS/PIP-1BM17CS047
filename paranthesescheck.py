class Paranthesescheck:
	def __init__(self,stri):
		self.stri=stri
	def check_validity(self):
		#li=self.stri[:]
		newli=[]
		for x in self.stri:
			if x=='(' or x=='{' or x=='[':
				newli.append(x)
			elif x==')':
				if len(newli)!=0:
					if newli[-1]=='(':
						newli.pop()
				else:
					return False
				
			elif x=='}':
				if len(newli)!=0:
					if newli[-1]=='{':
						newli.pop()
				else:
					return False
				
			elif x==']':
				if len(newli)!=0:
					if newli[-1]=='[':
						newli.pop()
				else:
					return False
						
				
		if len(newli)==0:
			return True
		else:
			return False

bracketstr=input("Enter the parantheses string: ")
ob=Paranthesescheck(bracketstr)
result=ob.check_validity()
if result:
	print("The parantheses string is valid")
else:
	print("The parantheses string is invalid")

					
