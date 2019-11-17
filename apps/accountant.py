import datetime
import pandas
columns = ['time', 'operation', 'amount', 'remark']
initial = [[datetime.datetime.now(), 'Initial', 0.0, 'None']]
account = pandas.DataFrame(initial, columns = columns, index = [0])


def credit():
    amount = round(float(input('Введите сумму пополнения: ')), 2)
    account.loc[account.shape[0]] = [datetime.datetime.now(), 'Credit', amount, 'None']


def debit():
    amount = - round(float(input('Введите сумму покупки: ')), 2)
    if - amount <= account['amount'].sum():
        remark = input('Введите описание покупки: ')
        account.loc[account.shape[0]] = [datetime.datetime.now(), 'Debit', amount, remark]
    else:
        print('Недостаточно средств на счете.')


def statement():
    print(account)


def accountant():
    while True:
        print(f"Баланас вашего счета: {round(account['amount'].sum(), 2)}")
        print('1. пополнение счета\n2. покупка\n3. история покупок\n4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            credit()
        elif choice == '2':
            debit()
        elif choice == '3':
            statement()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    accountant()