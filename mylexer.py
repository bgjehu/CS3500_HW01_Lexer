#   Metadata
__author__ = 'fullstackpug'


#   Imports
import sys


#   Global constants
#   Accept State = INT_MAX
accept_state = sys.maxint
#   Fault State = -1
fault_state = -1


#   Utilities
def output(index, tokenType):
    sign = "!"
    if tokenType != "Invalid":
        sign = "."
    result = "{0}: {1}{2}\n".format(index, tokenType, sign)
    sys.stdout.write(result)


def isHex(char):
        value = ord(char)
        # from 0-9 or A-F
        if 48 <= value <= 57 or 65 <= value <= 70:
            return True
        else:
            return False


def runRecognizer(token, recognizer, isAutomata):
    if isAutomata:
        #   init
        #   State = 0
        s = 0
        #   index = 0
        i = 0

        while (i < len(token)):
            c = token[i]
            s = recognizer(s, c)
            i += 1

        if s == accept_state:
            return True
        else:
            return False
    else:
        return recognizer(token)


def recognize(token):   #   run all recognizer in order
    recognizers = [[integer_constant_recognizer,True,"Integer"],
                   [decimal_constant_recognizer,True,"Decimal"],
                   [scientific_constant_recognizer,True,"Scientific"],
                   [hexadecimal_recognizer,True,"Hexadecimal"],
                   [keyword_recognizer,False,"Keyword"],
                   [identifier_recognizer,True,"Identifier"]]
    for i in range(0,len(recognizers)):
        recognizer = recognizers[i]
        if runRecognizer(token,recognizer[0],recognizer[1]):
            return recognizer[2]
    return "Invalid"


#   Recognizers
def integer_constant_recognizer(state, char):   #   is automata
    if state == 0:
        if char == '+' or char == '-':
            return 1
        elif char.isdigit():
            return accept_state
    elif state == 1 or state == accept_state:
        if char.isdigit():
            return accept_state
    #   no match
    return fault_state


def decimal_constant_recognizer(state, char):   #   is automata
    if state == 0:
        if char == '+' or char == '-':
            return 1
        elif char.isdigit():
            return 2
    elif state == 1:
        if char.isdigit():
            return 2
    elif state == 2:
        if char == '.':
            return 3
        elif char.isdigit():
            return 2
    elif state == 3 or state == accept_state:
        if char.isdigit():
            return accept_state
    #   no match
    return fault_state


def scientific_constant_recognizer(state, char):   #   is automata
    if state == 0:
        if char == '+' or char == '-':
            return 1
        elif char.isdigit():
            return 2
    elif state == 1:
        if char.isdigit():
            return 2
    elif state == 2:
        if char.isdigit():
            return 2
        elif char == '.':
            return 3
    elif state == 3:
        if char.isdigit:
            return 4
    elif state == 4:
        if char.isdigit():
            return 4
        elif char == 'E':
            return 5
    elif state == 5:
        if char.isdigit():
            if char == '0':
                return 7
            else:
                return accept_state
        elif char == '+' or char == '-':
            return 6
    elif state == 6:
        if char.isdigit():
            if char == '0':
                return 7
            else:
                return accept_state
    elif state == 7:
        if char.isdigit():
            if char == '0':
                return 7
            else:
                return accept_state
    elif state == accept_state:
        if char.isdigit():
            return accept_state
    #   no match
    return fault_state


def hexadecimal_recognizer(state, char):   #   is automata
    if state == 0:
        if isHex(char):
            return 1
    elif state == 1:
        if isHex(char):
            return 1
        elif char == 'H':
            return accept_state
    #   no match
    return fault_state


def keyword_recognizer(token):   #   is not automata
    if token == "if" or token == "else" or token == "for" or token == "while":
        return True
    else:
        return False


def identifier_recognizer(state, char):   #   is automata
    if state == 0:
        if char.isalpha():
            return accept_state
    elif state == accept_state:
        if char.isdigit() or char.isalpha or char == '_':
            return accept_state
    #   no match
    return fault_state


#   Application entry
def main():
    count = raw_input()
    sys.stdout.write("{0}\n".format(count))
    for i in range(0, int(count)):
        token = raw_input()
        tokenType = recognize(token)
        output(i + 1, tokenType)
    return 0


main()
