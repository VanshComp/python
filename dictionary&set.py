# 1. Store following word meanings in a python dictionary :

# input_str = input("Enter word and its meaning: ")
# key_value_pairs = input_str.split()
# a = dict(zip(key_value_pairs[::2], key_value_pairs[1::2]))
# print(a)
#*************************************************************************************************************************************

# 2.You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

# str=input("Enter different courses: ")
# a=str.split()
# b=set(a)     
# print(len(b))
#***********************************************************************************************************************************

# 3.WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

# subject={}
# keys=input("Enter all subjects: ").split()
# values=input("Enter marks for each subject: ").split()
# subject.update(zip(keys,values))
# print(subject)
#*************************************************************************************************************************************

# 4.Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

# x={9,"9.0"}
# print(x)