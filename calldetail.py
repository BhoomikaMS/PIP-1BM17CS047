class CallDetail:
	def __init__(self,ph1,ph2,duration,typeofcall):
		self.caller=ph1
		self.receiver=ph2
		self.duration=duration
		self.typeofcall=typeofcall
class Util:
	def __init__(self):
		self.list_of_call_objects=[]

	def parse_customer(self,list_of_call_string):
		li=[]
		for i in list_of_call_string:
			li=i.split(',')
			c=CallDetail(li[0],li[1],li[2],li[3])
			self.list_of_call_objects.append(c)
	def printdetails(self):
		for i in self.list_of_call_objects:
			print("Calling number: ",i.caller)
			print("Receiving number: ",i.receiver)
			print("Duration: ",i.duration)
			print("Type: ",i.typeofcall)
			print()


call='9990000001,9807654678,23,STD'
call2='9876789876,8907657456,42,Local'
call3='7890671245,8967098745,50,ISD'

list1=[call,call2,call3]

u=Util()
u.parse_customer(list1)	
print("Call Details: ")	
u.printdetails()
