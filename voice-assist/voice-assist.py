import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.8

commands_dict = {
    'commands': {
        'greeting': ['привет', 'здравствуй'],
        'create_task': ['добавить задачу', 'создать задачу', 'заметка']
    }
}


def listen_command():
    """Функция для оцифровки голоса"""
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)  # прослушивание помех
            audio = sr.listen(source=mic)  # слушает микрофон
            query = sr.recognize_google(audio_data=audio, language='ru-RU')  # отсылает google услышанный текст
            return query
    except speech_recognition.UnknownValueError:
        return 'Что-то не так'


def greeting():
    """Функция приветствия"""

    return "Здравствуйте"


def create_task():
    """Функция для записи в блокнот"""

    print("Что добавить в список дел?")
    query = listen_command()

    # запись текста в файл
    with open('to-do-list.txt', 'a') as file:
        file.write(f'{query}\n')
    return f'Задча "{query}" успешно добавлена в лист задач'


def main():
    while True:
        query = listen_command().lower()
        print('Я услышал: ', query)

        for k, v in commands_dict['commands'].items():
            if query in v:
                print(globals()[k]())
        if query == 'стоп':
            break


if __name__ == '__main__':
    main()
