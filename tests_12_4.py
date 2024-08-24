import logging
import unittest
from Module12 import module12_2 as r

logging.basicConfig(
                    level=logging.INFO,
                    filename='runner_tests.log',
                    filemode='w',
                    encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s',
                   )


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = r.Runner(name="Usain", speed=-5)
            self.assertLessEqual(0, runner.speed)
            logging.info('"test_walk" выполнен успешно')
        except AssertionError as exc:
            logging.warning(f"Неверная скорость для Runner: {exc} ", exc_info=True)

    def test_run(self):
        try:
            runner = r.Runner(name=1, speed=10)
            self.assertIsInstance(runner.name, str)
            logging.info('"test_run" выполнен успешно')
        except AssertionError as exc:
            logging.warning(f"Неверный тип данных для объекта Runner: {exc}", exc_info=True)
            print("11111111111111111111111111111111111111111111111")

if __name__ == '__main__':
    unittest.main()









