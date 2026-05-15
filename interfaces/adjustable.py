from abc import ABC, abstractmethod


class Adjustable(ABC):

    @abstractmethod
    def set_value(self, value):
        pass