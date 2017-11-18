user_name=input('Как вас зовут? \n')
name={'Настя': {'city': 'Владимир', 'temperature': '+2', 'wind': 'восточный'},'Сережа': {'city': 'Владимир', 'temperature': '+2', 'wind': 'восточный'}}
print (name.get(user_name))