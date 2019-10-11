# Ask a user their name
name = input("Enter your first name: ")

# If their first name starts with A or B
# tell them they go to room AB
eerste_letter1 = name[0:1]

if eerste_letter1.upper() in ('A', 'B'):
    room = 'AB'

# IF their first name starts with C
elif eerste_letter1.upper() == ('C'):
    room = 'C'
# tell them to go to room C
else:
    last_name = input("Enter your last name: ")
    eerste_letter2 = last_name[0:1]
    if eerste_letter2.upper() == ('Z'):
        room = 'Z'
    else:
        room = OTHER

print(f'Go to room {room}')
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z
