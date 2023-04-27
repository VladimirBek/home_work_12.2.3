from utils.dicts import get_val
dic = {"vcs": "mercurial", 'lang': 'Python', 'school': 'Skypro'}
def test_get_val():
    assert get_val(dic, 'lang') == 'Python'
    assert get_val(dic, 'other') == 'default value'
    assert get_val(dic, 'other', 'Git') == 'Git'
