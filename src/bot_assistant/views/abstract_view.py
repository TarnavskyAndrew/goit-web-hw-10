from abc import ABC, abstractmethod


# Клас UserView визачає інтерфейс для всіх видів користувацького інтерфейсу.
class UserView(ABC):  # ABC - базовий клас для визначення абстрактних класів

    @abstractmethod  # Декоратор abstractmethod вказує, що цей метод повинен бути реалізований у підкласах
    def display_contact(self, contact):  # Метод для відображення контактів користувача
        pass

    @abstractmethod
    def display_help(self):  # Метод для відображення довідки з доступними командами
        pass

    @abstractmethod
    def display_message(self, message):  # Метод для відображення повідомлень користувачу
        pass
    
    @abstractmethod
    def display_welcome_commands(self):
        pass
