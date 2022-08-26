# Exercise 5: Access the nested key ‘salary’ from the following JSON
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
# # write code to print the value of salary
# Expected Output:

# 7000

import json
a= """
{ "company":{
    "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
b=json.loads(a)
print(b["company"]["employee"]["payble"]["salary"])
