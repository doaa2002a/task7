# question 1
my_dict = {'name': 'Ahmed', 'age': 20, 'job': 'Engineer'}
print(my_dict.values())
print(my_dict.keys())
print(my_dict['name'])
my_dict['age'] = 32
my_dict['workplace'] = 'GSG'
print(my_dict)

# question 2
my_tuple = (('name', 'Ahmed'), ('age', 23), ('job', 'Doctor'))
my_dict = {key: value for key, value in my_tuple}
print(my_dict)


# question 3
dic1 = {'name': 'Dema', 'age': 20}
dic2 = {'job': 'Engineer', 'ID': 456367}
dic3 = {'Year': 2003}
new_dict = {}
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)
print(new_dict)


# question 4
my_dict = {'num1': 648, 'num2': 4194, 'num3': 60}
print(max(my_dict.values()))
print(min(my_dict.values()))


# question 5
my_dict2 = {'name': 'Abed', 'age': 31, 'job': 'Teacher'}
print('ID' in my_dict2)


# question 6
Languages2023 = {'Programming Language': ['python', 'Java', 'JavaScript', 'C#'], 'Market Share %': [27.99, 15.9, 9.36, 6.67]}
list_of_dicts = []
for i in range(len(Languages2023['Programming Language'])):
    lang = Languages2023['Programming Language'][i]
    share = Languages2023['Market Share %'][i]
    new_dict = {'Programming Language': lang, 'Market Share %': share}
    list_of_dicts.append(new_dict)
print(list_of_dicts)


print("full mark inshallah ^_^")









