## List of comprehension
# Structure: new_list =[new_item for item in list]
import pandas
student_dict ={
    "student": ["Angela","James", "Lily"],
    "score": [56, 76, 98]
}
student_dataFrame = pandas.DataFrame(student_dict)
print(student_dataFrame)
# for (key, value) in student_dataFrame.items():
#     print(value)

for (index, row) in student_dataFrame.iterrows():
    print(row.score)

# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass