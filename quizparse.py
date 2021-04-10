
# Python program to read
#  quiz json file
  
  
import json
  
# Opening JSON file
f = open('quiz.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)

# store result
result =[]

#list1 for parsing 1st bracket in dictionary: list1- ['quiz']
list1 =[]
for key in data.keys():
	list1.append(key)
quizc1 = data[list1[0]]

#list1 for parsing 2nd bracket in dictionary: list1- ['sport','maths']
list2 =[]
for key in quizc1.keys():
	list2.append(key)


########## Template of Quiz ################

print("Let's start the quiz\n")
print("Choose from\nsport\nmaths\n")
c1 = input()
if  c1 in list2:
	# for parsing keys/group choice : data['quiz'][c1]
	for k in data['quiz'][c1]:
		# for parsing each question print : data['quiz'][c1][k]
		for key in data['quiz'][c1][k]:
			# parsing each key in question.
			if key == 'question':
				print(key, data['quiz'][c1][k][key])
			if key =='options':
				print(key)
				for i in data['quiz'][c1][k][key]:
					print(i)
				print("Choose your Option (Write Answer")
				c2 = input()
				if c2 == data['quiz'][c1][k]['answer']:
					result.append("Correct!")
				else:
					result.append("Wrong! "+ "The answer is "+ data['quiz'][c1][k]['answer'])

#printing result
print(result)

# Closing file
f.close()