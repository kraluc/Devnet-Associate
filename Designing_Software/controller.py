from abc import ABC, abstractmethod
import model

class UserController(ABC):
    def __init__(self, view):
        self.view = view # a controller tied to a specific view

    @abstractmethod
    def create(self):
        raise NotImplementedError # These methods need to be implemented
                                  # by the strategy implementation

    @abstractmethod
    def get(id):
        raise NotImplementedError


class SimpleController(UserController):
    def create(self, username, email):
        if '@' not in email:
            self.view.update_display(False, 'Email not valid')
        else:
            user = model.User(username, email)
            result = user.store_user()
            if result:
                self.view_update_display(True, 'User created!')

    def get(self, id):
        user = model.User.get_user(id)
        if user:
            self.view.update_display(True, user)
        else:
            self.view.update_display(False, f'User id {id} not found')
