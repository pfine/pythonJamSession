class Employee:
    """A sample Employee class - crewate employee instance"""

    raise_mmt = 1.05  # 5%

    def __init__(self, first, last, pay):
        """
        Purpose: Employee, First name, Last name, and his payment after planned raise
        """
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_mmt)
