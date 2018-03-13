import csv

dinnerA = []
dinnerB = []
dinnerC = []
linnerD = []
dinnerE = []
linnerF = []
dinnerG = []
dinnerH = []
dessert1 = []
dessert2 = []
dessert3 = []
dessert4 = []
dessert5 = []
dessert6 = []
dessert7 = []

def fillLists():
	lst = []
	with open('prefrosh2021.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader)
		for row in reader:
			rep = ''.join(row)
			if rep == '':
				break

			imgFile = "../static/Prefrosh/" + row[3] + row[1] + ".JPG"
			prefrosh = [row[0], imgFile.replace(" ", "")]

			if 'Fleming' in row[4]:
				dinnerA.append(prefrosh)
			elif 'Fleming' in row[5]:
				dinnerB.append(prefrosh)
			elif 'Fleming' in row[6]:
				dinnerC.append(prefrosh)
			elif 'Fleming' in row[7]:
				linnerD.append(prefrosh)
			elif 'Fleming' in row[8]:
				dinnerE.append(prefrosh)
			elif 'Fleming' in row[9]:
				linnerF.append(prefrosh)
			elif 'Fleming' in row[10]:
				dinnerG.append(prefrosh)
			elif 'Fleming' in row[11]:
				dinnerH.append(prefrosh)

			if 'Fleming' in row[14]:
				dessert1.append(prefrosh)
			elif 'Fleming' in row[15]:
				dessert2.append(prefrosh)
			elif 'Fleming' in row[16]:
				dessert3.append(prefrosh)
			elif 'Fleming' in row[17]:
				dessert4.append(prefrosh)
			elif 'Fleming' in row[18]:
				dessert5.append(prefrosh)
			elif 'Fleming' in row[19]:
				dessert6.append(prefrosh)
			elif 'Fleming' in row[20]:
				dessert7.append(prefrosh)

fillLists()
print "dinnerA"
print dinnerA

print "\ndinnerB"
print dinnerB

print "\ndinnerC"
print dinnerC

print "\nlinnerD"
print linnerD

print "\ndinnerE"
print dinnerE

print "\nlinnerF"
print linnerF

print "\ndinnerG"
print dinnerG

print "\ndinnerH"
print dinnerH

print "\ndessert1"
print dessert1

print "\ndessert2"
print dessert2

print "\ndessert3"
print dessert3

print "\ndessert4"
print dessert4

print "\ndessert5"
print dessert5

print "\ndessert6"
print dessert6

print "\ndessert7"
print dessert7

