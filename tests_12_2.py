import runner_for_12_2 as rt
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = {}

    def setUp(self):
        self.un1 = rt.Runner("Усейн", 10)
        self.un2 = rt.Runner("Андрей", 9)
        self.un3 = rt.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in all_results.items():
            print(value)

    def test_t_1(self):
        u_1_3 = rt.Tournament(90, self.un1, self.un3)
        results = u_1_3.start()
        zabeg = ""
        for key, value in results.items():
            zabeg += str(key) + ": " + str(value) + " "
        all_results["1"] = zabeg

        self.assertTrue(results[2] == "Ник", "В забеге 1 пришёл не последним")

    def test_t_2(self):
        u_2_3 = rt.Tournament(90, self.un2, self.un3)
        results = u_2_3.start()
        zabeg = ""
        for key, value in results.items():
            zabeg += str(key) + ": " + str(value) + " "
        all_results["2"] = zabeg
        self.assertTrue(results[2] == "Ник", "В забеге 2 пришёл не последним")

    def test_t_3(self):
        u_1_2_3 = rt.Tournament(90, self.un1, self.un2, self.un3)
        results = u_1_2_3.start()
        zabeg = ""
        for key, value in results.items():
            zabeg += str(key) + ": " + str(value) + " "
        all_results["3"] = zabeg
        self.assertTrue(results[3] == "Ник", "В забеге 3 пришёл не последним")


if __name__ == "__main__":
    unittest.main()
