print("You have entered a room where a wizard sits at a large oak desk; he tells you he is checking people in for magical transportation. He requires the following information:")

name = input("Tell the wizard your name:")
age = int(input("Tell the wizard your age:"))
gender = input("What is your gender? M for male or F for female:")
day_time = input("What is the time of day? M for morning, A afternoon, or N for night:")

print(f"The wizard says: 'Why hello, {name}, you look wise for a {age} year old.'")

if str(gender) == "M":
    print(f"He suays: 'Interesting, though, I have a niece about your age - she is {age - 2} years old.'")
elif str(gender) == "F":
    print(f"He says: 'Interesting, though, I have a nephew about your age - he is {age - 2} years old.'")
else:
    print(f"He says: 'That's not a gender I have heard of before, but reminds me of my sister's child... they must be about {age-2} years old by now.'")

day_message = "The sun shines boldly through a window behind the wizard." if day_time == "M" else "The window is hard to see out of, the sun has set for the day."
print(day_message)

num1 = int(input("The wizard asks for 4 numbers. What should number one be?"))
num2 = int(input("What should number two be?"))
num3 = int(input("What should number three be?"))
num4 = int(input("What should number four be?"))

num_list = [num1, num2, num3, num4]

print("The wizard mutters your choice of numbers over to himself 'Which would be suitable...hmmm...'")

i = 0
while i < len(num_list):
    print(num_list[i])
    i += 1

for j in num_list:
     print(j)
#it will automatically define the var letter ie. j here
#this should automatically just iterate through the list


print(f"...maybe {str(num_list[3])} would be most suitable.... Yes, the land of mystery and adventure. Hold onto your hat, {name}, not many {age} year olds have ever been this far before!'")
print("Before you can ask the wizard what on earth he means, you feel the ground slipping and rushing beneath your feet, as the scene around you blurs indistinguishably...")    