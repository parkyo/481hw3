# -*- coding: utf8 -*-
from __future__ import unicode_literals
import unittest
import re
import sys
import pycodestyle

import fuzzywuzzy 
# from fuzzywuzzy import process
# from fuzzywuzzy import utils
# from fuzzywuzzy.string_processing import StringProcessor

if sys.version_info[0] == 3:
    unicode = str

if sys.version_info[:2] == (2, 6):
    # Monkeypatch to make tests work on 2.6
    def assertLess(first, second, msg=None):
        assert first > second
    unittest.TestCase.assertLess = assertLess


class StringProcessingTest(unittest.TestCase):
    def test_replace_non_letters_non_numbers_with_whitespace(self):
        strings = ["new york mets - atlanta braves", "CÃ£es danados",
                   "New York //// Mets $$$", "Ã‡a va?"]
        for string in strings:
            proc_string = fuzzywuzzy.StringProcessor.replace_non_letters_non_numbers_with_whitespace(string)
            regex = re.compile(r"(?ui)[\W]")
            for expr in regex.finditer(proc_string):
                self.assertEqual(expr.group(), " ")



class est(unittest.TestCase):
    def setUp(self):
        self.s1 = "new york mets"
        self.s1a = "new york mets"
        self.s2 = "new YORK mets"
        self.s3 = "the wonderful new york mets"
        self.s4 = "new york mets vs atlanta braves"
        self.s5 = "atlanta braves vs new york mets"
        self.s6 = "new york mets - atlanta braves"
        self.mixed_strings = [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
            "C'est la vie",
            "Ã‡a va?",
            "CÃ£es danados",
            "\xacCamarÃµes assados",
            "a\xac\u1234\u20ac\U00008000",
            "\u00C1"
        ]

    def tearDown(self):
        pass

    def test_asciidammit(self):
        for s in self.mixed_strings:
            fuzzywuzzy.asciidammit(s)

    def test_fullProcess(self):
        for s in self.mixed_strings:
            fuzzywuzzy.full_process(s)


class RatioTest(unittest.TestCase):

    def setUp(self):
        self.s1 = "new york mets"
        self.s1a = "new york mets"
        self.s2 = "new YORK mets"
        self.s3 = "the wonderful new york mets"
        self.s4 = "new york mets vs atlanta braves"
        self.s5 = "atlanta braves vs new york mets"
        self.s6 = "new york mets - atlanta braves"
        self.s7 = 'new york city mets - atlanta braves'

        self.cirque_strings = [
            "cirque du soleil - zarkana - las vegas",
            "cirque du soleil ",
            "cirque du soleil las vegas",
            "zarkana las vegas",
            "las vegas cirque du soleil at the bellagio",
            "zarakana - cirque du soleil - bellagio"
        ]

        self.baseball_strings = [
            "new york mets vs chicago cubs",
            "chicago cubs vs chicago white sox",
            "philladelphia phillies vs atlanta braves",
            "braves vs mets",
        ]

    def tearDown(self):
        pass

    def testCaseInsensitive(self):
        self.assertNotEqual(fuzzywuzzy.ratio(self.s1, self.s2), 100)
        self.assertEqual(fuzzywuzzy.ratio(fuzzywuzzy.full_process(self.s1), fuzzywuzzy.full_process(self.s2)), 100)

    def testTokenSortRatio(self):
        self.assertEqual(fuzzywuzzy.token_sort_ratio(self.s1, self.s1a), 100)

    def testTokenSetRatio(self):
        self.assertEqual(fuzzywuzzy.token_set_ratio(self.s4, self.s5), 100)

    def testQuickRatioEqual(self):
        self.assertEqual(fuzzywuzzy.QRatio(self.s1, self.s1a), 100)

    def testQuickRatioNotEqual(self):
        self.assertNotEqual(fuzzywuzzy.QRatio(self.s1, self.s3), 100)

    def testWRatioCaseInsensitive(self):
        self.assertEqual(fuzzywuzzy.WRatio(self.s1, self.s2), 100)

    def testWRatioMisorderedMatch(self):
        # misordered full matches are scaled by .95
        self.assertEqual(fuzzywuzzy.WRatio(self.s4, self.s5), 95)

    def testQRatioUnicode(self):
        self.assertEqual(fuzzywuzzy.WRatio(unicode(self.s1), unicode(self.s1a)), 100)

    def testIssueSeven(self):
        s1 = "HSINCHUANG"
        s2 = "SINJHUAN"
        s3 = "LSINJHUANG DISTRIC"
        s4 = "SINJHUANG DISTRICT"

        self.assertTrue(fuzzywuzzy.partial_ratio(s1, s2) > 75)
        self.assertTrue(fuzzywuzzy.partial_ratio(s1, s3) > 75)
        self.assertTrue(fuzzywuzzy.partial_ratio(s1, s4) > 75)

    def testPartialRatioUnicodeString(self):
        s1 = "\u00C1"
        s2 = "ABCD"
        score = fuzzywuzzy.partial_ratio(s1, s2)
        self.assertEqual(0, score)

    def testQRatioUnicodeString(self):
        s1 = "\u00C1"
        s2 = "ABCD"
        score = fuzzywuzzy.QRatio(s1, s2)
        self.assertEqual(0, score)

        # Cyrillic.
        s1 = "\u043f\u0441\u0438\u0445\u043e\u043b\u043e\u0433"
        s2 = "\u043f\u0441\u0438\u0445\u043e\u0442\u0435\u0440\u0430\u043f\u0435\u0432\u0442"
        score = fuzzywuzzy.QRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)

        # Chinese.
        s1 = "\u6211\u4e86\u89e3\u6570\u5b66"
        s2 = "\u6211\u5b66\u6570\u5b66"
        score = fuzzywuzzy.QRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)

    def testQRatioForceAscii(self):
        s1 = "ABCD\u00C1"
        s2 = "ABCD"

        score = fuzzywuzzy.WRatio(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)

        score = fuzzywuzzy.WRatio(s1, s2, force_ascii=False)
        self.assertLess(score, 100)

    def testTokenSortForceAscii(self):
        s1 = "ABCD\u00C1 HELP\u00C1"
        s2 = "ABCD HELP"

        score = fuzzywuzzy._token_sort(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)

        score = fuzzywuzzy._token_sort(s1, s2, force_ascii=False)
        self.assertLess(score, 100)


class ValidatorTest(unittest.TestCase):
    def setUp(self):
        self.testFunc = lambda *args, **kwargs: (args, kwargs)

    def testCheckEmptyString(self):
        invalid_input = [
            ('', ''),
            ('Some', ''),
            ('', 'Some')
        ]
        decorated_func = fuzzywuzzy.check_empty_string(self.testFunc)
        for i in invalid_input:
            self.assertEqual(decorated_func(*i), 0)

        valid_input = ('Some', 'Some')
        actual = decorated_func(*valid_input)
        self.assertNotEqual(actual, 0)


class ProcessTest(unittest.TestCase):

    def setUp(self):
        self.s1 = "new york mets"
        self.s1a = "new york mets"
        self.s2 = "new YORK mets"
        self.s3 = "the wonderful new york mets"
        self.s4 = "new york mets vs atlanta braves"
        self.s5 = "atlanta braves vs new york mets"
        self.s6 = "new york mets - atlanta braves"

        self.cirque_strings = [
            "cirque du soleil - zarkana - las vegas",
            "cirque du soleil ",
            "cirque du soleil las vegas",
            "zarkana las vegas",
            "las vegas cirque du soleil at the bellagio",
            "zarakana - cirque du soleil - bellagio"
        ]

        self.baseball_strings = [
            "new york mets vs chicago cubs",
            "chicago cubs vs chicago white sox",
            "philladelphia phillies vs atlanta braves",
            "braves vs mets",
        ]

    def testGetBestChoice2(self):
        query = "philadelphia phillies at atlanta braves"
        best = fuzzywuzzy.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], self.baseball_strings[2])

    def testGetBestChoice4(self):
        query = "chicago cubs vs new york mets"
        best = fuzzywuzzy.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], self.baseball_strings[0])

    def testWithScorer(self):
        choices = [
            "new york mets vs chicago cubs",
            "chicago cubs at new york mets",
            "atlanta braves vs pittsbugh pirates",
            "new york yankees vs boston red sox"
        ]

        choices_dict = {
            1: "new york mets vs chicago cubs",
            2: "chicago cubs vs chicago white sox",
            3: "philladelphia phillies vs atlanta braves",
            4: "braves vs mets"
        }

        # in this hypothetical example we care about ordering, so we use quick ratio
        query = "new york mets at chicago cubs"
        scorer = fuzzywuzzy.QRatio

        # first, as an example, the normal way would select the "more
        # 'complete' match of choices[1]"

        best = fuzzywuzzy.extractOne(query, choices)
        self.assertEqual(best[0], choices[1])

        # now, use the custom scorer

        best = fuzzywuzzy.extractOne(query, choices, scorer=scorer)
        self.assertEqual(best[0], choices[0])

        best = fuzzywuzzy.extractOne(query, choices_dict)
        self.assertEqual(best[0], choices_dict[1])

    def testWithCutoff2(self):
        choices = [
            "new york mets vs chicago cubs",
            "chicago cubs at new york mets",
            "atlanta braves vs pittsbugh pirates",
            "new york yankees vs boston red sox"
        ]

        query = "new york mets vs chicago cubs"
        # Only find 100-score cases
        res = fuzzywuzzy.extractOne(query, choices, score_cutoff=100)
        self.assertTrue(res is not None)
        best_match, score = res
        self.assertTrue(best_match is choices[0])

    def testNullStrings(self):
        choices = [
            None,
            "new york mets vs chicago cubs",
            "new york yankees vs boston red sox",
            None,
            None
        ]

        query = "new york mets at chicago cubs"

        best = fuzzywuzzy.extractOne(query, choices)
        self.assertEqual(best[0], choices[1])

    def test_dict_like_extract(self):
        """We should be able to use a dict-like object for choices, not only a
        dict, and still get dict-like output.
        """
        try:
            from UserDict import UserDict
        except ImportError:
            from collections import UserDict
        choices = UserDict({'aa': 'bb', 'a1': None})
        search = 'aaa'
        result = fuzzywuzzy.extract(search, choices)
        self.assertTrue(len(result) > 0)
        for value, confidence, key in result:
            self.assertTrue(value in choices.values())

    def test_simplematch(self):
        basic_string = 'a, b'
        match_strings = ['a, b']

        result = fuzzywuzzy.extractOne(basic_string, match_strings, scorer=fuzzywuzzy.ratio)
        part_result = fuzzywuzzy.extractOne(basic_string, match_strings, scorer=fuzzywuzzy.partial_ratio)

        self.assertEqual(result, ('a, b', 100))
        self.assertEqual(part_result, ('a, b', 100))


class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self):
        pep8style = pycodestyle.StyleGuide(quiet=False)
        pep8style.options.ignore = pep8style.options.ignore + tuple(['E501'])
        pep8style.input_dir('fuzzywuzzy')
        result = pep8style.check_files()
        self.assertEqual(result.total_errors, 0, "PEP8 POLICE - WOOOOOWOOOOOOOOOO")

unittest.main()         # run all tests
