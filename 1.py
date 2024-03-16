import csv

# Считываем файлы
with open('astronaut_time.csv', encoding = 'utf-8') as file:
    list_strok = list(csv.reader(file, delimiter=','))
with open('new_time.txt', 'w', newline='', encoding='utf-8') as new_file:
    nf = csv.writer(new_file)


    for i in list_strok[1:]:

        # Вычисляем актуальное время и переводим в нужный формат
        time_hours = i[3][:2]
        act_time_hours = int(time_hours)+int(i[4])
        if act_time_hours >= 24: act_time_hours -= 24
        if len(str(act_time_hours)) == 1: act_time_hours = '0' + str(act_time_hours)

        # Записываем актуальное время в новый файл
        nf.writerow([f'На станции {i[1]} в каюте {i[2]} восстановлено время. Актуальное время: {act_time_hours}{i[3][-6:]}'])


