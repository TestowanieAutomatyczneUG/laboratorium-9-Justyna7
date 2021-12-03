from unittest import TestCase, main
from unittest.mock import *


class Car:
    def needsFuel(self):
        return 0

    def getEngineTemperature(self):
        return 0

    def driveTo(self, destination):
        return 0


class CarImpl:
    def __init__(self):
        self.car = Car()

    def needsFuel(self):
        return self.car.needsFuel()

    def getEngineTemperature(self):
        return self.car.getEngineTemperature()

    def driveTo(self, destination):
        return self.car.driveTo(destination)


class test_Carimpl(TestCase):
    def test_needsFuel(self):
        # prepare mock
        test_object = CarImpl()
        test_object.needsFuel = Mock(name='needsFuel')
        test_object.needsFuel.return_value = False

        # testing
        result = test_object.needsFuel()
        self.assertEqual(False, result, 'return value from needsFuel incorrect')

    def test_getEngineTemperature(self):
        # prepare mock
        test_object = CarImpl()
        test_object.getEngineTemperature = Mock(name='getEngineTemperature ')
        test_object.getEngineTemperature.return_value = 80.69

        # testing
        result = test_object.getEngineTemperature(5)
        self.assertEqual(80.69, result, 'return value from getEngineTemperature incorrect')

    def test_driveTo(self):
        def side_effect(arg):
            return arg
        # prepare mock
        test_object = CarImpl()
        test_object.driveTo = Mock(name='driveTo')
        test_object.driveTo.side_effect = side_effect

        # testing
        result = test_object.driveTo("Nowa Huta")
        self.assertEqual("Nowa Huta", result, 'return value from driveTo incorrect')


if __name__ == '__main__':
    main()
