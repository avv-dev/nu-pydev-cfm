import random


def victory():
    QUESTIONNAIRE = [
        {'name': 'Уильям Генри Гейтс III',   'dob_d': '28.10.1955', 'dob_a': 'двадцать восьмое октября 1955 года'},
        {'name': 'Стивен Пол Джобс',         'dob_d': '24.02.1955', 'dob_a': 'двадцать четвертое февраля 1955 года'},
        {'name': 'Бьерн Страуструп',         'dob_d': '30.12.1950', 'dob_a': 'тридцатое декабря 1950 года'},
        {'name': 'Линус Торвальдс',          'dob_d': '28.12.1969', 'dob_a': 'двадцать восьмое декабря 1969 года'},
        {'name': 'Дональд Эрвин Кнут',       'dob_d': '10.01.1938', 'dob_a': 'десятое января 1938 года'},
        {'name': 'Деннис Макалистэйр Ритчи', 'dob_d': '09.09.1941', 'dob_a': 'девятое сентября 1941 года'},
        {'name': 'Эндрю Стюарт Таненбаум',   'dob_d': '16.03.1944', 'dob_a': 'шестнадцатое марта 1944 года'},
        {'name': 'Тимоти Джон Бернерс-Ли',   'dob_d': '08.06.1955', 'dob_a': 'восьмое июня 1955 года'},
        {'name': 'Лотфи Аскар Заде',         'dob_d': '04.02.1921', 'dob_a': 'четвертое февраля 1921 года'},
        {'name': 'Брайан Уилсон Керниган',   'dob_d': '01.01.1942', 'dob_a': 'первое января 1942 года'}
    ]
    ASK = 'Напишите дату рождения данного известного человека в формате "дд.мм.гггг":\n'

    i = 0
    correct = 0
    incorrect = 0
    selection = random.sample(range(10), 5)

    print('Викторина: "Компьютерная история в лицах"\n')

    while True:
        if i == len(selection):
            print(f'Правильных ответов: {correct}.\n'
                  f'Неправильных ответов: {incorrect}.\n'
                  f'Процент правильных ответов: {correct * 100 / i}%.\n'
                  f'Процент неправильных ответов: {incorrect * 100 / i}%.\n\n')
            ans = input('Желаете пройти тест ещё раз? (Да / Нет) ')
            if ans.lower() == 'да':
                i = 0
                correct = 0
                incorrect = 0
            else:
                return [correct, incorrect]
        print(f"{i+1}. {ASK}{QUESTIONNAIRE[selection[i]]['name']}.")
        ans = input('>>>')
        if ans[:2].isdigit() and ans[2] == '.' and ans[3:5].isdigit() and ans[5] == '.' and ans[6:].isdigit():
            if ans == QUESTIONNAIRE[selection[i]]['dob_d']:
                correct += 1
            else:
                incorrect += 1
                print(f"Неверно. Правильный ответ: {QUESTIONNAIRE[selection[i]]['dob_a']}")
            i += 1
        else:
            print('Некорректный формат ввода данных. Попробуйте ещё раз.')


if __name__ == '__main__':
    victory()