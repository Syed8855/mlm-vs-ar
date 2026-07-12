from abc import ABC,abstractmethod

class BaseBenchmark(ABC):
    @abstractmethod
    def run(self,text:str):
        pass