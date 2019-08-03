class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.d:
            self.d[number] += 1
        else:
            self.d[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for n in self.d:
            r = value - n
            if r in self.d and (r != n or self.d[r] > 1):
                return True
        return False
        

# class TwoSum:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.numbers = []
#
#     def add(self, number: int) -> None:
#         """
#         Add the number to an internal data structure..
#         """
#         self.numbers.append(number)
#
#     def find(self, value: int) -> bool:
#         """
#         Find if there exists any pair of numbers which sum is equal to the value.
#         """
#         d = dict()
#         for i, n in enumerate(self.numbers):
#             if n in d:
#                 return True
#             d[value-n] = 1
#         return False