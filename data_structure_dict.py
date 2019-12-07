# dictionary {key: value}

# initialize dictionary
test_dict = {} # or dict()

test_dict['first_name'] = 'Huy'
test_dict['last_name'] = 'Truong'

print(test_dict)

print('value of first_name:', test_dict['first_name']) # throws an error if key exists
print('value of last_name:', test_dict.get('last_name')) # get doesn't throw an error if key doesn't exist

print('default value:', test_dict.get('bad_key', 'bad_value'))


test_dict['date_of_birth'] = 123456
test_dict['address'] = 1234567

# for key in test_dict.keys():
#     print(key)

for key, value in test_dict.items():
    print(key, value)


# JSON format
# it's a giant string