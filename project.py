guest_list = ['mat_grandma', 'mat_grandpa', 'pat_grandma', 'pat_grandpa']

# [print(f'Happy to see you {val}') for val in guest_list]
# couldn't make it 
#print(guest_list[3])
# replace object in list
guest_list[3] = 'unc_kam'
#[print(f'I found a bigger venue to accomodate us, maybe I will see you soon, {val}.') for val in guest_list]
uninvite_guest1 = guest_list.pop()
[print(f'Oops! Looks like the new venue has been taken, sorry I have to cancel {uninvite_guest1}.')]
uninvite_guest2 = guest_list.pop()
[print(f'Oops! Looks like the new venue has been taken, sorry I have to cancel {uninvite_guest2}.')]

[print(f'You are still invited for dinner, {val}.') for val in guest_list]

del guest_list[0:]
print(guest_list)