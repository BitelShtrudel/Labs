my_string = "ФИО;Возраст;Категория;_Иванов Иван Иванович; 23 года; Студент 3 курса;_Петров Семен Игоревич; 22 года; Студент 2 курса;_Иванов Семен Игоревич; 22 года; Студент 2 курса;_Акибов Ярослав Наумович; 23 года; Студент 3 курса;_Борков Станислав Максимович; 21 год; Студент 1 курса;_Петров Семен Семенович; 21 год;Студент 1 курса;_Романов Станислав Андреевич; 23 года; Студент 3 курса;_Петров Всеволод Борисович; 21 год; Студент 2 курса"
k=my_string.split('_')
for i in range(1,len(k)):
    k1=''.join(k[i].split(';'))
    if k[i].startswith('А') or k[i].startswith('Б'):
        print(k1)