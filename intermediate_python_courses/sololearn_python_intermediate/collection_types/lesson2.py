database={
    'user_name':'Gui',
    'user_id': 14125,
    'user_level':8
}

data_type={'user name':'user_name','user id':'user_id','user level':'user_level'}

while True:
    ask=input('Analisar dados [s/n]')
    if ask.lower()=='s':
        ask=input('data type [user name,user id or user level]')
        if ask in data_type:print(database[data_type[ask]]);continue
        else:print('invalid');continue
    elif ask.lower()=='n':exit()
    else:print('invalid');continue