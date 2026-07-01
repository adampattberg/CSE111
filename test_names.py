from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("John", "John-Doe") == "John-Doe;John"
    assert make_full_name("Adam", "Pattberg") == "Pattberg;Adam"
    assert make_full_name("A", "Pg") == "Pg;A"
    assert make_full_name("", "") == ";"

def test_extract_family_name():
    assert extract_family_name("John-Doe; John") == "John-Doe"
    assert extract_family_name("Pattberg; Adam") == "Pattberg"
    assert extract_family_name("Pg; A") == "Pg"
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    assert extract_given_name("John-Doe; John") == " John"
    assert extract_given_name("Pattberg; Adam") == " Adam"
    assert extract_given_name("Pg; A") == " A"
    assert extract_given_name("; ") == " "

pytest.main(["-v", "--tb=line", "-rN", __file__])