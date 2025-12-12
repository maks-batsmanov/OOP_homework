from abc import ABC, abstractmethod


class BaseCategory(ABC):

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def total_quantity(self):
        pass

    @property
    @abstractmethod
    def total_cost(self):
        pass
