import add_path
import pytest
import mit_ocw_exercises.lec6_recursion_dictionaries as lec6

def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) ==3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
    assert lec6.fib(7) == 21
    assert lec6.fib(8) == 34
    assert lec6.fib(9) == 55
    assert lec6.fib(10) == 89
    assert lec6.fib(11) == 144
    assert lec6.fib(12) == 233
    assert lec6.fib(13) == 377
    assert lec6.fib(14) == 610
    assert lec6.fib(15) == 987
    assert lec6.fib(16) == 1597
    assert lec6.fib(17) == 2584
    assert lec6.fib(18) == 4181
    assert lec6.fib(19) == 6765




def test_is_palindrome():
    assert lec6.is_palindrome('eve') == True
    assert lec6.is_palindrome('Able was I saw Elba') == True
    assert lec6.is_palindrome('Is this a palindrome') == False
    assert lec6.is_palindrome("HeleH") == True
    assert lec6.is_palindrome("redmeat") == False