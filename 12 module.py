

money = int(input ("Введите сумму,которую хотите внести ?"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
bank_1 = per_cent ["ТКБ"]
bank_2 = per_cent ["СКБ"]
bank_3 = per_cent ["ВТБ"]
bank_4 = per_cent ["СБЕР"]
deposit = [int((money*bank_1)/100), int((money*bank_2)/100), int((money*bank_3)/100), int((money*bank_4)/100)]
print (deposit)
print ('Максимальная сумма,которую Вы заработаете - ', max(deposit))