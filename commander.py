# Перечисления команд, режимов
from command_enum import Command
#from mode_enum import Mode

# Рабочие модули


class Commander:

    def __init__(self):

        # Текущий, предыдущий режимы
        #self.now_mode = Mode.default
        #self.last_mode = Mode.default

        self.last_command = None

        # Для запомминания ответов пользователя
        self.last_ans = None

        """
    def change_mode(self, to_mode):
        """
        #Меняет режим приема команд
        #:param to_mode: Измененный мод
        """
        self.last_mode = self.now_mode
        self.now_mode = to_mode

        self.last_ans = None
        """

    def input(self, msg):
        """
        Функция принимающая сообщения пользователя
        :param msg: Сообщение
        :return: Ответ пользователю, отправившему сообщение
        """

        # Приветствие
        if msg in Command.hello.value:
            return "Привет!"

        # Фейсбук
        if msg in Command.facebook.value:
            return "пост в fb"

        # Вк
        if msg in Command.vk.value:
            return "пост в vk"

        # Последние
        if msg in Command.last.value:
            return "показать последние"
        
        # На стену
        if msg in Command.wall.value:
            return "пост на стену"

        # В группу
        if msg in Command.group.value:
            return "список групп"

        # Назад
        if msg in Command.back.value:
            return "назад"

        return "Команда не распознана!"






        # Проверка на команду смены мода
        """ 
        if msg.startswith("/"):
            for mode in Mode:
                if msg[1::] in mode.value:
                    self.change_mode(mode)
                    return "Режим изменен на " + self.now_mode.value[0]
            return "Неизвестный мод " + msg[1::]
        """
        # Режим получения ответа
        """
        if self.now_mode == Mode.get_ans:
            self.last_ans = msg
            self.now_mode = self.last_mode
            return "Ok!"

        if self.now_mode == Mode.default:
        """


