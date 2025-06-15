'''
The Builder Design Pattern is a creational design pattern that focuses on constructing complex objects step by step.

It separates the construction of an object from its representation, allowing the same construction process to create different representations.

When to Use the Builder Pattern:
The Builder Pattern is most useful in the following situations:

Complex Object Construction: When an object needs numerous optional components or configurations, and a cluttered constructor isn’t practical.
Multiple Representations: When you want to create various object representations using the same construction process.
'''


from abc import ABC, abstractmethod

class Director(ABC):
    """
    The Director class defines the order in which to execute the building steps.
    It is responsible for managing the construction process.
    """
    
    # @abstractmethod
    def construct(self, builder) -> None:
        """
        Construct the product using the builder.
        """
        builder.build_part_a()
        builder.build_part_b()
        builder.build_part_c()


class Builder(ABC):
    """
    The Builder class defines the interface for creating parts of a Product object.
    Concrete builders will implement this interface to construct specific parts.
    """

    @abstractmethod
    def build_part_a(self) -> None:
        """
        Build part A of the product.
        """
        pass

    @abstractmethod
    def build_part_b(self) -> None:
        """
        Build part B of the product.
        """
        pass

    @abstractmethod
    def build_part_c(self) -> None:
        """
        Build part C of the product.
        """
        pass

class ConcreteBuilderA(Builder):
    """
    ConcreteBuilder implements the Builder interface and constructs the parts of the product.
    It keeps track of the product being built.
    """

    def __init__(self):
        self.product = Product()

    def build_part_a(self) -> None:
        self.product.add("Part A")

    def build_part_b(self) -> None:
        self.product.add("Part B")

    def build_part_c(self) -> None:
        self.product.add("Part C")

    def get_product(self):
        return self.product


class ConcreteBuilderB(Builder):
    """
    Another ConcreteBuilder that constructs a different product.
    """

    def __init__(self):
        self.product = Product()

    def build_part_a(self) -> None:
        self.product.add("Part A (B)")

    def build_part_b(self) -> None:
        self.product.add("Part B (B)")

    def build_part_c(self) -> None:
        self.product.add("Part C (B)")

    def get_product(self):
        return self.product
    

class Product:
    """
    The Product class represents the complex object under construction.
    It can have multiple parts that are built by the Builder.
    """
    def __init__(self):
        self.parts = []

    def add(self, part: str) -> None:
        """
        Add a part to the product.
        """
        self.parts.append(part)

class Client:
    """
    The Client class uses the Director to construct a product using a specific builder.
    It can switch between different builders to create different products.
    """

    def construct_product(self, builder: Builder) -> Product:
        """
        Construct a product using the director and the specified builder.
        """
        director = Director()
        director.construct(builder)
        return builder.get_product()


if __name__ == "__main__":
    # Example usage
    client = Client()

    # Constructing a product with ConcreteBuilderA
    builder_a = ConcreteBuilderA()
    product_a = client.construct_product(builder_a)
    print("Product A parts:", product_a.parts)

    # Constructing a product with ConcreteBuilderB
    builder_b = ConcreteBuilderB()
    product_b = client.construct_product(builder_b)
    print("Product B parts:", product_b.parts)




'''
Using Builder in Your Projects
Incorporating the Builder Pattern into your software projects involves the following key steps and best practices:

Integration and Best Practices:

Identify Complex Object Needs: Determine if your project requires the construction of complex objects with multiple components and configurations.
Create Abstract Builder Interface: Define a clear and concise builder interface, specifying the methods for object construction. This interface acts as a contract for concrete builder classes.
Implement Concrete Builders: Develop concrete builder classes that implement the methods outlined in the builder interface. Each concrete builder corresponds to a specific object variation.
Utilize a Director Class: Employ a director class to coordinate the construction process, ensuring that steps are executed in the correct order.
Promote Reusability: Design your builders with reusability in mind. Creating builders that can be used for multiple objects reduces code duplication.
Adopt a Modular Approach: Keep your code modular by breaking down complex object construction into smaller, manageable steps.
Document Your Builders: Maintain comprehensive documentation for your builders to facilitate understanding and usage by other developers.
'''