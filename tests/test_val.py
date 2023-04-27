from utils.dicts import get_val
dic = {"vcs": "mercurial", 'lang': 'Python', 'school': 'Skypro'}
def test_get_val():
    assert test_get_val(dic, 'lang') == 'Python'
    assert test_get_val(dic, 'other') == 'default value'
    assert test_get_val(dic, 'other', 'Git') == 'Git'
