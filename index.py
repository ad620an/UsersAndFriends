from pprint import pprint

from dataset import users, countries
#print(users)
#pprint(countries)

# point1
users_wrong_password = []
for user in users:
    if user['password'].isnumeric():
        users_wrong_password.append({'name': user['name'], 'mail': user['mail']})
print('users_wrong_password =',users_wrong_password)      

#point2
girls_drivers = []
for user in users:
    if 'friends' in user.keys():
        for friend in user['friends']:
            if 'cars' in friend.keys() and friend['sex'] == 'F':
                girls_drivers.append({friend['name']})
print('girls_drivers =', girls_drivers)    

#point3
best_occupation = {}
max_salary = 0
for user in users:
     if 'friends' in user.keys():
         for friend in user['friends']:
            if friend['job']['salary'] > max_salary:
                best_occupation = {'occupation': friend['job']['occupation'], 'salary' : friend['job']['salary']}
                max_salary = friend['job']['salary']
print('best_occupation =',best_occupation) 

#point4
vip_user = ''
sum_salary = 0
max_sum_salary = 0
for user in users:
    if 'friends' in user.keys():
        for friend in user['friends']:
            sum_salary = sum_salary  +  friend['job']['salary']

    if sum_salary > max_sum_salary:
        vip_user = user['name']   
        max_sum_salary = sum_salary
print('vip_user =', vip_user) 

#point5
avg_flights = 0
sum_flights = 0
sum_friends = 0
sum_sum_flights = 0
for user in users:
    if 'friends' in user.keys():
        for friend in user['friends']:
            if 'cars' in friend.keys() and 'flights' in friend.keys():
                sum_friends = sum_friends + 1
                for flight in friend['flights']:
                      sum_flights = sum_flights + 1
                sum_sum_flights = sum_sum_flights + sum_flights      
avg_flights = sum_sum_flights/sum_friends
print('avg_flights = ', round(avg_flights, 5))

#point6
flag_user_removed = False
for user in users:
    if flag_user_removed == False:
        if 'friends' in user.keys():
            for friend in user['friends']:
                if 'flights' in friend.keys():
                    for flight in friend['flights']:
                        if flight['country'] in countries:
                            flag_user_removed = True
    else:
        users.remove(user)

                    
