import unittest
import main
import randomgame

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')
    def test_do_stuff(self):
        '''HIIII'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'dfgdfg'
        result = main.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)
    
    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ""
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')
    
    def tearDown(self):
        print('cleaning up')

class TestGame(unittest.TestCase):
    def test_input(self):
        # please note in the video, I had the parameters flipped it should be the "guess" parameter 1st and "answer" parameter 2nd
        result = randomgame.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = randomgame.run_guess(0, 5)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = randomgame.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        with self.assertRaises(TypeError):
            randomgame.run_guess('11', 5)

if __name__ == '__main__':
    unittest.main()