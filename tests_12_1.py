import runner_for_12_1
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        unit_1 = runner_for_12_1.Runner("Truant")
        for _ in range(10):
            unit_1.walk()
        self.assertEqual(unit_1.distance, 50)

    def test_run(self):
        unit_2 = runner_for_12_1.Runner("Jogger")
        for _ in range(10):
            unit_2.run()
        self.assertEqual(unit_2.distance, 100)

    def test_challenge(self):
        unit_3 = runner_for_12_1.Runner("Walker")
        unit_4 = runner_for_12_1.Runner("Runaway")
        for _ in range(10):
            unit_3.walk()
            unit_4.run()
        self.assertNotEqual(unit_3.distance, unit_4.distance)


if __name__ == "__main__":
    unittest.main
