


def input_people():
  id = input("Введите ID: ")
  last_name = input("Введите фамилию: ")
  name = input("Введите имя: ")
  second_name =input("Введите отчество: ")
  job_title=input("Введите должность: ")
  phone_number = input("Введите номер телефона (пример 89111234567): ")
  age=input("Введите дату рождения (пример 11.11.1990) : ")
  list_data=id+";"+last_name+";"+name+";"+second_name+";"+job_title+";"+phone_number+";"+age
  print(list_data)
  file = open("C:\\Users\\Alena\\Desktop\\гикбрейнс\\python\\28.09\\database1.csv", "a", newline='' )
  file.write(list_data+'\n')
  file.close() 
  

def output_people():
  last_name = (input("Введите фамилию, которую надо найти: "))  
  with open("C:\\Users\\Alena\\Desktop\\гикбрейнс\\python\\28.09\\database1.csv") as file:
    all=file.read()
    humans = all.split('\n')
    found=False
    for human in humans:
      elements=human.split(';')
     
      if elements[1]==last_name:
          print(elements)
          found=True
    if found==False:
        print('фамилия не найдена')

def removal():
     last_name = (input("Введите фамилию сотрудника, которого надо удалить: "))
     with open("C:\\Users\\Alena\\Desktop\\гикбрейнс\\python\\28.09\\database1.csv","r+") as file:
      all=file.read()
      humans = all.split('\n')
    
      for human in humans:
       elements=human.split(';')
       if elements[1]==last_name:
          print('удаленный сотрудник',human)
          humans.remove(human)
          str='\n'.join(humans)
          file.seek(0)
          file.write(str)
          file.truncate()   
          break
        
def change():
  with open("C:\\Users\\Alena\\Desktop\\гикбрейнс\\python\\28.09\\database1.csv","r+") as file:
   last_name=input("Введите фамилию сотрудника, которого изменить: ")
   all=file.read()
   humans = all.split('\n')
   for human in humans:
       elements=human.split(';')
       if elements[1]==last_name:
        print('что хотите изменить?: ')
        print('Если должность, введите 1: ')
        print('Если номер телефона, введите 2: ')
        q=(input())
        if q=='1':
         new_job=input('введите новую должность: ')
         elements[4]=new_job
         old_human_index=humans.index(human)
         human=';'.join(elements)
         humans[old_human_index]=human
         str='\n'.join(humans)
         file.seek(0)
         file.write(str)
         file.truncate() 
        elif q=='2': 
         new_numb=input('введите новый номер телефона (пример 89111234567): ')
         elements[5]=new_numb
         old_human_index=humans.index(human)
         human=';'.join(elements)
         humans[old_human_index]=human
         str='\n'.join(humans)
         file.seek(0)
         file.write(str)
         file.truncate() 


   




        

