from enum import IntEnum


class Roles(IntEnum):
    """
    Here CEO is a superuser that's why here is not define CEO role.
    """
    HR = 0
    MANAGER = 1
    ACCOUNT = 2
    DEVELOPER = 3
    EMPLOYEE = 4


class Types(IntEnum):
    FULLTIME = 0
    PARTTIME = 1
    INTERN = 2
    TEMP = 3
