"""
Python Trick
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            new_num = float(s)
        except:
            return False
        return True

"""
DFA
"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        states = [{},
                  {'blank': 1, 'digit': 2, 'sign': 3, 'dot': 4},
                  {'digit': 2, 'dot': 5, 'e': 6, 'blank': 9},
                  {'digit': 2, 'dot': 4},
                  {'digit': 5},
                  {'digit': 5, 'e': 6, 'blank': 9},
                  {'sign': 7, 'digit': 8},
                  {'digit': 8},
                  {'digit': 8, 'blank': 9},
                  {'blank': 9}
        ]
        current_state = 1
        for i in s:
            key = ''
            if i == '.':
                key = 'dot'
            if i == ' ':
                key = 'blank'
            if i >= '0' and i <= '9':
                key = 'digit'
            if i == 'e':
                key = 'e'
            if i == '+' or i == '-':
                key = 'sign'
            else:
                return False
            current_state = states[current_state][key]
        if current_state in [2, 5, 8, 9]:
            return True
        return False