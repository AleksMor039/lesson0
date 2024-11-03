import logging
import unittest
from runner_for_12_4 import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            unit = Runner('Name', -5)
            for i in range(10):
                unit.walk()
            self.assertEqual(unit.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except Exception as err:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            unit = Runner(15)
            if not isinstance(unit.name, str):
                raise TypeError
            for i in range(10):
                unit.run()
            self.assertEqual(unit.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_challenge(self):
        unit_1 = Runner('Name_1')
        unit_2 = Runner('Name_2')
        for i in range(10):
            unit_1.run()
            unit_2.walk()
        self.assertNotEqual(unit_1.distance, unit_2.distance)


if __name__ == "__main__":
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(level='INFO', filemode='w', filename='runner_tests.log', encoding='UTF-8', force=True,
                        format='%(asctime)s | %(levelname)s | %(message)s')

    unittest.main()
