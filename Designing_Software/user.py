from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self): # Update method must be implemented by the concrete observer
        raise NotImplementedError


class User(Observer):
    def __init__(self, username):
        self.username = username
        self.tracklist = []

    def update(self, publisher): # Fetching the state from the observable object
                                 # that was passed to the method
        print(f'> Updating user {self.username}')
        state = publisher.get_state()
        self.tracklist.append(state)

    def play_songs(self):
        print(f'> Playing {self.tracklist} to {self.username}')

