from utils.dicts import get_val
import pytest
@pytest.fixture
def dic_for_test_get_val():
    return {"vcs": "mercurial", 'lang': 'Python', 'school': 'Skypro'}

def test_get_val(dic_for_test_get_val):
    assert get_val(dic_for_test_get_val, 'lang') == 'Python'
    assert get_val(dic_for_test_get_val, 'other') == 'default value'
    assert get_val(dic_for_test_get_val, 'other', 'Git') == 'Git'
