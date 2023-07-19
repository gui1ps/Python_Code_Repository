contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
x=input()

achado=False

for contact in contacts:
    if contact[0]==x:
        print(contact[0],'is',contact[1])
        achado=True
    elif contacts.index(contact)==(len(contacts)-1) and not achado:
        print('Not Found')