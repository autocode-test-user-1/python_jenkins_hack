# Possible jenkins attack directions

1. Получить переменные окружения и отправить их post запросом
1. Получить переменные окружения и из тестируемой функции выбросить исключение: `raise Exception(os.environ)`   
1. Выбросить исключение на уровне модуля. Во время запуска теста модуль будет импортирован, текст исключения попадет в лог
1. Выполнение любой системной команды с правами Jenkins пользователя
