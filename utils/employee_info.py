from enum import IntEnum


class GENDER(IntEnum):
    MALE = 0
    FEMALE = 1
    OTHERS = 2

    @classmethod
    def select_gender(cls):
        return [(key.value, key.name) for key in cls]


class MARITAL(IntEnum):
    UNMARRIED = 0
    MARRIED = 1

    @classmethod
    def select_status(cls):
        return [(key.value, key.name) for key in cls]


class Roles(IntEnum):
    """
    Here CEO is a superuser that's why here is not define CEO role.
    """
    HR = 0
    MANAGER = 1
    ACCOUNT = 2
    DEVELOPER = 3
    EMPLOYEE = 4

    @classmethod
    def select_role(cls):
        return [(key.value, key.name) for key in cls]


class Types(IntEnum):
    FULLTIME = 0
    PARTTIME = 1
    INTERN = 2
    TEMP = 3

    @classmethod
    def employee_types(cls):
        return [(key.value, key.name) for key in cls]


class Pay(IntEnum):
    SALARY = 0
    BONUS = 1
    MEDICAL = 2
    LOAD = 3

    @classmethod
    def payment_types(cls):
        return [(key.value, key.name) for key in cls]


class Status(IntEnum):
    REGULAR = 0
    DUE = 1
    ADVANCE = 2
    PAID = 2

    @classmethod
    def pay_status(cls):
        return [(key.value, key.name) for key in cls]


class Evolution(IntEnum):
    PROGRESS = 0
    PENDING = 1
    DONE = 2
    FAILED = 3

    @classmethod
    def task_status(cls):
        return [(key.value, key.name) for key in cls]
