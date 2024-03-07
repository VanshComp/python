# Create a new file “practice.txt” using python. Add the following data in it:

# with open("sample.txt","w+") as f:
#     text=input("Enter your data here: ")
#     f.write(text)
    
# WAF that replace all occurrences of “java” with “python” in above file.

# with open("sample.txt","w+") as f:
#     text=input("Enter your data here: ")
#     f.write(text)
#     word=input("Enter particular text...u want to replace: ")
#     key=input("Enter changed text: ")
#     data=text.replace(word,key)
#     print(data)

# Search if the word “learning” exists in the file or not.

# with open("sample.txt","w+") as f:
#     text=input("Enter your data here: ")
#     f.write(text)
#     word=input("Enter particular text...u want to search: ")
#     key=text.find(word)
#     if key !=-1:
#         print("%s exists in file" % (word))
#     else:
#         print("%s doesn't exists in file" % (word))    

# WAF to find in which line of the file does the word “learning”occur first.
# Print -1 if word not found.

# def count_line():
#     word=input("Enter particular text...u want to search: ")
#     count=1
#     text=True
#     with open("sample.txt","r") as f:
#         while text:
#             text=f.readline()
#             if word in text:
#                 print(count)
#             count+=1
#     print("-1")
# count_line()    

# From a file containing numbers separated by comma, print the count of even numbers.

with open("numbers.txt", "w+") as f:
    num = input("Enter random numbers here, separated by commas: ")
    f.write(num)

with open("numbers.txt", "r") as f:
    numbers = f.read().split(',')
    count = 0

    for num in numbers:
        if int(num) % 2 == 0:
            count += 1

print("Count of even numbers:", count)
            