from textUtilities import TextUtilities

tu = TextUtilities()

def test_word_count():
    assert tu.word_count("Hello Python") == 2

def test_unique_words():
    assert tu.unique_words("apple apple banana orange banana") == ["apple", "banana"]

def test_reverse_string():
    assert tu.reverse_string("abc") == "cba"

def test_empty_string():
    assert tu.word_count("") == 0
    assert tu.reverse_string("") == ""

def test_single_word():
    assert tu.word_count("Hello") == 1
    assert tu.reverse_string("Python") == "nohtyP"

def test_special_characters():
    assert tu.reverse_string("@#$") == "$#@"

def test_case_sensitive():
    assert tu.unique_words("Hello hello") == ["Hello", "hello"]

def test_case_insensitive():
    assert tu.unique_words("Hello hello", case_sensitive=False) == ["hello"]