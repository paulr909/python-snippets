class ElectricalError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return f"The {self.device} is {self.problem}!"


class PlumbingError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return f"The {self.device} is {self.problem}!"


def cause_error(error_type: str) -> None:
    if error_type == "electrical":
        raise ElectricalError("circuit breaker", "overloaded")

    elif error_type == "plumbing":
        raise PlumbingError("dishwasher", "spraying water")

    else:
        raise Exception("A generic problem")


# cause some problems
try:
    cause_error("yard")

except ElectricalError as e:
    print(e)
    print("Fix it myself")

except PlumbingError as e:
    print(e)
    print("Call the plumber")

except Exception as e:
    print(e)
    print("Call the landlord")
