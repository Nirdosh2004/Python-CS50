students = [
          {
                    "name" : "Nirdosh",
                    "House" : "Nirala Esatate",
                    "Class" : "BCA - B",
          },
          {
                    "name" : "Harry",
                    "House" : "Hawgward",
                    "class" : "BBA",
          },
          {
                    "name" : "what?",
                    "House" : None,
          },
]

for name in students:
          print(name["name"] , name["House"], sep=", ")