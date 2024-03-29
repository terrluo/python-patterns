#!/usr/bin/python
"""
1. 模式动机
    1）在软件开发中采用类似于电源适配器的设计和编码技巧被称为适配器模式。
    2）通常情况下，客户端可以通过目标类的接口访问它所提供的服务。有时，现有的类可以满足客户类的功能需要，
       但是它所提供的接口不一定是客户类所期望的，这可能是因为现有类中方法名与目标类中定义的方法名不一致等原因所导致的。
    3）在这种情况下，现有的接口需要转化为客户类期望的接口，这样保证了对现有类的重用。如果不进行这样的转化，
       客户类就不能利用现有类所提供的功能，适配器模式可以完成这样的转化。
    4）在适配器模式中可以定义一个包装类，包装不兼容接口的对象，这个包装类指的就是适配器(Adapter)，
       它所包装的对象就是适配者(Adaptee)，即被适配的类。
    5）适配器提供客户类需要的接口，适配器的实现就是把客户类的请求转化为对适配者的相应接口的调用。
       也就是说：当客户类调用适配器的方法时，在适配器类的内部将调用适配者类的方法，而这个过程对客户类是透明的，
       客户类并不直接访问适配者类。因此，适配器可以使由于接口不兼容而不能交互的类可以一起工作。这就是适配器模式的模式动机。

2. 模式定义
    适配器模式(Adapter Pattern) ：将一个接口转换成客户希望的另一个接口，适配器模式使接口不兼容的那些类可以一起工作，
    其别名为包装器(Wrapper)。适配器模式既可以作为类结构型模式，也可以作为对象结构型模式。

3. 模式结构
    适配器模式包含如下角色：
        Target：目标抽象类
        Adapter：适配器类
        Adaptee：适配者类
        Client：客户类

    适配器模式有对象适配器和类适配器两种实现：
        对象适配器：Adapter.jpg
        类适配器：Adapter_classModel.jpg

4. 优点
    1) 将目标类和适配者类解耦，通过引入一个适配器类来重用现有的适配者类，而无须修改原有代码。
    2) 增加了类的透明性和复用性，将具体的实现封装在适配者类中，对于客户端类来说是透明的，而且提高了适配者的复用性。
    3) 灵活性和扩展性都非常好，通过使用配置文件，可以很方便地更换适配器，也可以在不修改原有代码的基础上增加新的适配器类，完全符合“开闭原则”。

    类适配器模式还具有如下优点：
        由于适配器类是适配者类的子类，因此可以在适配器类中置换一些适配者的方法，使得适配器的灵活性更强。
    对象适配器模式还具有如下优点：
        一个对象适配器可以把多个不同的适配者适配到同一个目标，也就是说，同一个适配器可以把适配者类和它的子类都适配到目标接口。

5. 缺点
    类适配器模式的缺点如下：
        对于Java、C#等不支持多重继承的语言，一次最多只能适配一个适配者类，而且目标抽象类只能为抽象类，
        不能为具体类，其使用有一定的局限性，不能将一个适配者类和它的子类都适配到目标接口。
    对象适配器模式的缺点如下：
        与类适配器模式相比，要想置换适配者类的方法就不容易。如果一定要置换掉适配者类的一个或多个方法，
        就只好先做一个适配者类的子类，将适配者类的方法置换掉，然后再把适配者类的子类当做真正的适配者进行适配，实现过程较为复杂。

6. 适用环境
    在以下情况下可以使用适配器模式：
        1) 系统需要使用现有的类，而这些类的接口不符合系统的需要。
        2) 想要建立一个可以重复使用的类，用于与一些彼此之间没有太大关联的一些类，包括一些可能在将来引进的类一起工作。

7. 模式应用
    Sun公司在1996年公开了Java语言的数据库连接工具JDBC，JDBC使得Java语言程序能够与数据库连接，并使用SQL语言来查询和操作数据。
    JDBC给出一个客户端通用的抽象接口，每一个具体数据库引擎（如SQL Server、Oracle、MySQL等）的JDBC驱动软件都是一个介于JDBC
    接口和数据库引擎接口之间的适配器软件。抽象的JDBC接口和各个数据库引擎API之间都需要相应的适配器软件，这就是为各个不同数据库
    引擎准备的驱动程序。

8. 模式扩展
    认适配器模式(Default Adapter Pattern)或缺省适配器模式
        当不需要全部实现接口提供的方法时，可先设计一个抽象类实现接口，并为该接口中每个方法提供一个默认实现（空方法），
        那么该抽象类的子类可有选择地覆盖父类的某些方法来实现需求，它适用于一个接口不想使用其所有的方法的情况。因此也
        称为单接口适配器模式。

9. 总结
    1) 结构型模式描述如何将类或者对象结合在一起形成更大的结构。
    2) 适配器模式用于将一个接口转换成客户希望的另一个接口，适配器模式使接口不兼容的那些类可以一起工作，其别名为包装器。
       适配器模式既可以作为类结构型模式，也可以作为对象结构型模式。
    3) 适配器模式包含四个角色：
           a) 目标抽象类定义客户要用的特定领域的接口；
           b) 适配器类可以调用另一个接口，作为一个转换器，对适配者和抽象目标类进行适配，它是适配器模式的核心；
           c) 适配者类是被适配的角色，它定义了一个已经存在的接口，这个接口需要适配；
           d) 在客户类中针对目标抽象类进行编程，调用在目标抽象类中定义的业务方法。
    4) 在类适配器模式中，适配器类实现了目标抽象类接口并继承了适配者类，并在目标抽象类的实现方法中调用所继承的适配者类的方法；
       在对象适配器模式中，适配器类继承了目标抽象类并定义了一个适配者类的对象实例，在所继承的目标抽象类方法中调用适配者类的相应业务方法。
    5) 适配器模式的主要优点是将目标类和适配者类解耦，增加了类的透明性和复用性，同时系统的灵活性和扩展性都非常好，更换
       适配器或者增加新的适配器都非常方便，符合“开闭原则”；
       类适配器模式的缺点是适配器类在很多编程语言中不能同时适配多个适配者类，对象适配器模式的缺点是很难置换适配者类的方法。
    6) 适配器模式适用情况包括：
           a) 系统需要使用现有的类，而这些类的接口不符合系统的需要；
           b) 想要建立一个可以重复使用的类，用于与一些彼此之间没有太大关联的一些类一起工作。
"""


class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Human(object):
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "'hello'"


class Car(object):
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom{0}".format("!" * octane_level)


class Adapter(object):
    """
    Adapts an object by replacing methods.
    Usage:
    dog = Dog()
    dog = Adapter(dog, make_noise=dog.bark)
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__


def main():
    objects = []
    dog = Dog()
    print(dog.__dict__)

    objects.append(Adapter(dog, make_noise=dog.bark))
    print(objects[0].__dict__['obj'], objects[0].__dict__['make_noise'])

    print(objects[0].original_dict())

    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))
    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))
    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    for obj in objects:
        print(f'A {obj.name} goes {obj.make_noise()}')


if __name__ == '__main__':
    main()
