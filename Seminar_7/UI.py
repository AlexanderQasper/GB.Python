import people
print('что необходимо сделать?')
print('Если внести данные в базу нажите +')
print('Если найти данные сотрудника в базе нажите f')
print('Если изменить данные сотрудника в базе нажите *')
print('Если удалить данные сотрудника в базе нажите d')
ask = (input())
if ask=='+':
  people.input_people()
elif ask=='f':
    people.output_people()
elif ask=='*':
    people.change()
elif ask=='d':
    people.removal()
else: 
    print('выберите действие между "+" "f" "*" и "d" ')

   

