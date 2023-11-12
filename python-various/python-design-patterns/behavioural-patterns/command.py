from abc import ABC, abstractmethod


# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Concrete command
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class Light:
    def turn_on(self):
        print("Light is ON")


# Invoker
class SmartHome:
    def __init__(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()


if __name__ == "__main__":
    light = Light()
    light_on = LightOnCommand(light)
    home = SmartHome(light_on)
    home.press_button()
