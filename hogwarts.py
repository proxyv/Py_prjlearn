students = ["Hermione", "Harry", "Ron", "Draco"]
houses = {
    "Hermione" : "Gryffindor", 
     "Harry": "Gryffindor", 
     "Ron": "Gryffindor", 
     "Draco": "Slytherin"
     }

#for i in range(len(students)):
 #   print(i+1, students[i])

for stu in houses:
    print(stu, houses[stu], sep=" - ")

stud = [
    {"Name": "Hermione", "house": "Gryffindor", "Patronas": "Otter"},
    {"Name": "Harry", "house": "Gryffindor", "Patronas": "Stag"},
    {"Name": "Ron", "house": "Gryffindor", "Patronas": "Jack Russel"},
    {"Name": "Draco", "house": "Slytherin", "Patronas": "None"}
]

for st in stud:
    print(st["Name"], st["house"], sep=" - ")