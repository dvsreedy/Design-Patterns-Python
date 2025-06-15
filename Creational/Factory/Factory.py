from abc import ABC, abstractmethod

class Localizer(ABC):
    @abstractmethod
    def localize(self, text: str) -> str:
        pass

class EnglishLocalizer(Localizer):
    def localize(self, text: str) -> str:
        return f"English: {text}"

class SpanishLocalizer(Localizer):
    def __init__(self):
        self.translations = {
            "Hello": "Hola",
            "Goodbye": "Adiós"
        }
    
    def localize(self, text: str) -> str:
        return f" Spanish : {self.translations.get(text, text)}"

class FrenchLocalizer(Localizer):
    def __init__(self):
        self.translations = {
            "Hello": "Bonjour",
            "Goodbye": "Au revoir"
        }

    def localize(self, text: str) -> str:
        return f"French: {self.translations.get(text, text)}"
    

class LocalizerFactory(ABC):
    @abstractmethod
    def create_localizer(self) -> Localizer:
        pass


class FrenchLocalizerFactory(LocalizerFactory):
    def create_localizer(self) -> Localizer:
        return FrenchLocalizer()

class SpanishLocalizerFactory(LocalizerFactory):
    def create_localizer(self) -> Localizer:
        return SpanishLocalizer()

class EnglishLocalizerFactory(LocalizerFactory):
    def create_localizer(self) -> Localizer:
        return EnglishLocalizer()

def main():
    factories = [
        EnglishLocalizerFactory(),
        SpanishLocalizerFactory(),
        FrenchLocalizerFactory()
    ]

    for factory in factories:
        localizer = factory.create_localizer()
        print(localizer.localize("Hello"))
        print(localizer.localize("Goodbye"))
        

if __name__ == "__main__":
    main()

'''
Real-world Use Cases: Factory in Action
The Factory Method pattern is particularly useful in various scenarios:

1) Library Frameworks: It’s commonly used in library frameworks, allowing developers to extend and customize the behavior of a library.
2) Plug-in Architectures: When building applications with extensible plug-in architectures, the Factory Method pattern simplifies the addition of new plug-ins without modifying existing code.
3) Testing: Factories can be used to create mock objects for unit testing.


Advantages of the Factory Method Pattern
The Factory Method pattern offers several benefits:

1) Decoupling: It decouples client code from the concrete classes, reducing dependencies and enhancing code stability.
2) Flexibility: It allows for the creation of objects without specifying their exact class, making the code more flexible and maintainable.
3) Extensibility: New product classes can be added without modifying existing code, promoting an open-closed principle.

Considerations and Potential Drawbacks
However, like any design pattern, the Factory Method has its drawbacks:

1) Complexity: Introducing multiple Factory Methods and associated classes can lead to increased complexity.
2) Abstraction Overhead: Creating numerous abstract classes and interfaces may add overhead to the codebase.
3) Overkill: In simple scenarios, using the Factory Method pattern might be overkill and add unnecessary complexity.

Conclusion
The Factory Method design pattern offers a systematic way to create objects while keeping code maintainable and adaptable. It excels in scenarios where object types vary or evolve.


'''