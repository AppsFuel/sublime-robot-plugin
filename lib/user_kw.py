import unittest
import re


def user_kw(keywords, keyword_prefix, sublime_prefix):
    head = keyword_prefix.lower()
    head = head.lstrip()
    head = head if head.rstrip() else head.rstrip()
    prefix = sublime_prefix if head and head[-1] != ' ' else ''
    user_kw = []
    for kw in filter(lambda kw: kw.lower().startswith(head), keywords):
        tail = re.sub(head, '', kw.lower())
        value = prefix + tail if head and ' ' in tail and ' ' in head else kw
        user_kw.append((kw.title(), value.title()))
    return user_kw


class TestGetCompletionValue(unittest.TestCase):
    def setUp(self):
        self.keywords = [
            'Go', 'Go To', 'Go Tom', 'Go To Home', 'Go To Tom To', 'Go To Zoom Zoom', 'Home Go To'
        ]

    def test_(self):
        self.assertEquals(
            zip(self.keywords, self.keywords),
            user_kw(self.keywords, '', '')
        )

    def test_ssss(self):
        self.assertEquals(
            zip(self.keywords, self.keywords),
            user_kw(self.keywords, '    ', '')
        )

    def test_ssssG(self):
        self.assertEquals(
            zip(self.keywords[:-1], self.keywords[:-1]),
            user_kw(self.keywords, '    G', 'G')
        )

    def test_ssssg(self):
        self.assertEquals(
            zip(self.keywords[:-1], self.keywords[:-1]),
            user_kw(self.keywords, '    g', 'g')
        )

    def test_gos(self):
        self.assertEquals(
            [('Go To', 'Go To'), ('Go Tom', 'Go Tom'), ('Go To Home', 'To Home'), ('Go To Tom To', 'To Tom To'), ('Go To Zoom Zoom', 'To Zoom Zoom')],
            user_kw(self.keywords, 'go ', '')
        )

    def test_Gos(self):
        self.assertEquals(
            [('Go To', 'Go To'), ('Go Tom', 'Go Tom'), ('Go To Home', 'To Home'), ('Go To Tom To', 'To Tom To'), ('Go To Zoom Zoom', 'To Zoom Zoom')],
            user_kw(self.keywords, 'Go ', '')
        )

    def test_gosto(self):
        self.assertEquals(
            [('Go To', 'Go To'), ('Go Tom', 'Go Tom'), ('Go To Home', 'To Home'), ('Go To Tom To', 'To Tom To'), ('Go To Zoom Zoom', 'To Zoom Zoom')],
            user_kw(self.keywords, 'go to', 'to')
        )

    def test_gostos(self):
        self.assertEquals(
            [('Go To Home', 'Go To Home'), ('Go To Tom To', 'Tom To'), ('Go To Zoom Zoom', 'Zoom Zoom')],
            user_kw(self.keywords, 'go to ', '')
        )


if __name__ == '__main__':
    unittest.main()
