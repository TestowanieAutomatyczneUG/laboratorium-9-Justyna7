from unittest import TestCase, main
from unittest.mock import *
from datetime import time


class Sound:
    def getTime(self):
        return None

    def playWavFile(self, file):
        return None


class Checker:
    def __init__(self):
        self.sound = Sound()
        self.played = False

    def remainder(self, filepath):
        if self.sound.getTime().hour >= 17:
            self.sound.playWavFile(filepath)
            self.wavWasPlayed()
        else:
            self.resetWav()

    def wavWasPlayed (self):
        self.played = True

    def resetWav(self):
        self.played = False


class test_Checker(TestCase):
    def setUp(self):
        # prepare mock path
        self.fpath = MagicMock()
        self.test_object = Checker()

    def test_17(self):
        # prepare mock time
        self.test_object.sound.getTime = Mock(name='getTime1')
        self.test_object.sound.getTime.return_value = time(17, 0, 0)

        # testing
        self.test_object.remainder(self.fpath.__fspath__)
        result = self.test_object.played
        self.assertEqual(True, result, 'return value from played incorrect')

    def test_23_59(self):
        # prepare mock time
        self.test_object.sound.getTime = Mock(name='getTime2')
        self.test_object.sound.getTime.return_value = time(23, 59, 59)

        # testing
        self.test_object.remainder(self.fpath.__fspath__)
        result = self.test_object.played
        self.assertEqual(True, result, 'return value from played incorrect')

    def test_00(self):
        # prepare mock time
        self.test_object.sound.getTime = Mock(name='getTime3')
        self.test_object.sound.getTime.return_value = time(0, 0, 0)

        # testing
        self.test_object.remainder(self.fpath.__fspath__)
        result = self.test_object.played
        self.assertEqual(False, result, 'return value from played incorrect')

    def test_16(self):
        # prepare mock time
        self.test_object.sound.getTime = Mock(name='getTime4')
        self.test_object.sound.getTime.return_value = time(16, 0, 0)

        # testing
        self.test_object.remainder(self.fpath.__fspath__)
        result = self.test_object.played
        self.assertEqual(False, result, 'return value from played incorrect')

    def test_minutes(self):
        # prepare mock time
        self.test_object.sound.getTime = Mock(name='getTime5')
        self.test_object.sound.getTime.return_value = time(0, 17, 0)

        # testing
        self.test_object.remainder(self.fpath.__fspath__)
        result = self.test_object.played
        self.assertEqual(False, result, 'return value from played incorrect')

    def test_seconds(self):
        # prepare mock time
        self.test_object.sound.getTime = Mock(name='getTime6')
        self.test_object.sound.getTime.return_value = time(0, 0, 17)

        # testing
        self.test_object.remainder(self.fpath.__fspath__)
        result = self.test_object.played
        self.assertEqual(False, result, 'return value from played incorrect')

    def tearDown(self):
        self.fpath = None
        self.test_object = None


if __name__ == '__main__':
    main()
