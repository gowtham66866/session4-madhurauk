import pytest
import session4
import inspect
import re
from session4 import Qualean
import copy
import random
import os

CHECK_FOR_FUNCTIONS = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
]

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_and_when_q2_not_defined():
    q1=Qualean(0)
    q2=None
    assert q1.__and__(q2) == False, "__and__ function is not short circuiting"

def test_and_functionality():
    q1 = Qualean(random.choice([-1,0,1]))
    q2 = Qualean(random.choice([-1,0,1]))
    if q1.get_number()!=0 and q2.get_number()!=0:
        assert q1.__and__(q2)==True, "and True case is not working as expected"
    else:
        assert q1.__and__(q2)==False, "and False case is not working as expected"

def test_or_when_q2_not_defined():
    q1=Qualean(1)
    q2=None
    assert q1.__or__(q2) == True, "__or__ function is not short circuiting"

def test_or_functionality():
    q1 = Qualean(random.choice([-1,0,1]))
    q2 = Qualean(random.choice([-1,0,1]))
    if q1.get_number()!=0 or q2.get_number()!=0:
        assert q1.__or__(q2)==True, "or True case is not working as expected"
    else:
        assert q1.__or__(q2)==False, "or False case is not working as expected"

def test_repr():
    q = Qualean(0)
    assert 'object at' not in q.__repr__()

def test_str():
    q = Qualean(0)
    internal_value = q.get_number()
    assert q.__str__() == f'Qualean: internal number ={internal_value}', 'The print does not meet expectations'

def test_add_mul():
    q = Qualean(-1)
    total = q
    for x in range(99):
        total = q.__add__(total) 
    assert total==q.__mul__(100), "Pecision has been lost"

def test_ge():
    q1 = Qualean(random.choice([-1,0,1]))
    q2 = Qualean(random.choice([-1,0,1]))
    if q1.get_number()>= q2.get_number():
        # print(q1.get_number())
        # print(q2.get_number())
        # print(True)
        assert q1.__ge__(q2)==True, "__ge__ True case not working"
    else:
        # print(q1.get_number())
        # print(q2.get_number())
        # print(False)
        assert q1.__ge__(q2)==False, "__ge__ False case not working"

def test_all_functions_exist():
    code_lines = inspect.getsource(session4)
    for word in CHECK_FOR_FUNCTIONS:
        assert word in code_lines, 'Have you heard of Pinocchio?'

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in CHECK_FOR_FUNCTIONS:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"
