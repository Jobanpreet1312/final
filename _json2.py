d={"Empolyees":[{
    "name": "piyush",
    "height": "174cm",
    "dob": "12-02-2000",
    "city":"mumbai",
    "state":"Maharastra"
},{
    "name": "partap",
    "height": "168cm",
    "dob": "13-12-2000",
    "city":"mumbai",
    "state":"Maharastra"
},{
   "name": "rahul",
    "height": "179cm",
    "dob": "02-12-2000",
    "city":"mumbai",
    "state":"Maharastra"
},{
   "name": "ram",
    "height": "188cm",
    "dob": "13-01-2000",
    "city":"mumbai",
    "state":"Maharastra"
},{
    "name": "sham",
    "height": "197cm",
    "dob": "30-12-2000",
    "city":"mumbai",
    "state":"Maharastra"
} ]}

print("Original dictionary:")
print(d)
print(type(d))
import json
 
with open("dictionary", "w") as f:
   json.dump(d, f, indent = 4, sort_keys = True)
 
print("\nJson file to dictionary:")
with open('dictionary') as f:
 data = json.load(f)
print(data)