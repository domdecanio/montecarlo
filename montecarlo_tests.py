import montecarlo
import unittest


class MontecarloTestSuite(unittest.TestCase):
    
    
    def test_01_Die_init(self):
        '''
        Purpose: Testing Die.__init__() to ensure all elements of input list are valid faces (str or int).
        '''
        die = montecarlo.Die([1, True, 3, 'a', 4.3, 6])
        
        # "output" and "expected" will be equivalent if the operation was completed successfully.
        output = die.init_error
        expected = "Error - Input for argument 'n' is not of type: str or int"
        # This message will be displayed if the operation was unsuccessful.
        message = 'Error - The face value passed was invalid, but an exception was not raised.' 
        self.assertEqual(output, expected, message)
    
    
    def test_02_Die_change_weights(self):
        '''
        Purpose: Testing if the face_value passed to the .change_weights() method is valid.
        '''
        die = montecarlo.Die([1, 2, 3, 4, 5, 6])
        output = die.change_weights('a', 5)
        expected = print('The face value passed is invalid - it is not a valid face on the die.')
        
        # testValue will be "True" if the operation was completed successfully.
        testValue = output == expected
        # This message will be displayed if the operation was unsuccessful.
        message = 'Error - The face value passed was invalid, but an exception was not raised.' 
        self.assertTrue(testValue, message)


    def test_03_Die_roll(self):
        '''
        Purpose: Testing that the length of the outputted list of rolls matches the desired number of rolls.
        '''
        die = montecarlo.Die([1, 2, 3, 4, 5, 6])
        output = len(die.roll(5))
        expected = 5
        
        # testValue will be "True" if the operation was completed successfully.
        testValue = output == expected
        # This message will be displayed if the operation was unsuccessful.
        message = 'Error - The die was not rolled the desired number of times.' 
        self.assertTrue(testValue, message)

        
    def test_04_Die_show(self):
        '''
        Purpose: Ensure the Die.show() method displays the entire faces/weights dataframe.
        '''
        inputs = [1, 2, 3, 4, 5, 6]
        die = montecarlo.Die(inputs)
        output = len(die.show())
        expected = len(inputs)
        
        # testValue will be "True" if the operation was completed successfully.
        testValue = output == expected
        # This message will be displayed if the operation was unsuccessful.
        message = 'Error - The number of faces and the number of rows in the faces/weights dataframe are not equal.' 
        self.assertTrue(testValue, message)
        
        
    def test_05_Game_init(self):
        '''
        Purpose: Ensure the Game.__init__() method correctly takes a list.
        '''
        inputs = [1, 2, 3, 4, 5, 6]
        die = montecarlo.Die(inputs)
        game = montecarlo.Game([die, die])
        output = isinstance(game.dice, list)
        expected = True
        
        # testValue will be "True" if the operation was completed successfully.
        testValue = output == expected
        # This message will be displayed if the operation was unsuccessful.
        message = 'Error - The input when initializing a new instance of "Game" was not a list.' 
        self.assertTrue(testValue, message)
        
    
    def test_06_Game_play(self):
        '''
        Purpose: Ensure the Game.play() method correctly requires the input to be type "int".
        '''
        inputs = [1, 2, 3, 4, 5, 6]
        die = montecarlo.Die(inputs)
        game = montecarlo.Game([die, die])
        
        # "output" and "expected" will be equivalent if the operation was completed successfully.
        output = game.play(25.3)
        expected = print('Error - The argument entered for "num_rolls" must be an integer.')
        # This message will be displayed if the operation was unsuccessful.
        message = 'Error - The game.play() method incorrectly accepts non-integers as inputs.' 
        self.assertEqual(output, expected, message)

        
    def test_07_Game_show(self):
        '''
        Purpose: Ensure the Game.show() method correctly handles improper inputs.
        '''
        inputs = [1, 2, 3, 4, 5, 6]
        die = montecarlo.Die(inputs)
        game = montecarlo.Game([die, die])
                
        # "output" and "expected" will be equivalent if the operation was completed successfully.
        output = game.show('blob')
        expected = print('Error - The argument entered for "df_format" is invalid')
        # This message will be displayed if the operation was unsuccessful.
        message = 'Error - The input when initializing a new instance of "Game" was not a list.' 
        self.assertEqual(output, expected, message)
    
    
    def test_08_Analyzer_init(self):
        '''
        Purpose: Ensure the Analyzer.__init__() method  correctly prohibits inputs other than "Game"
                 objects from the montecarlo package when instantiating a new "Analyzer" object.
        '''
        broken_analyzer = montecarlo.Analyzer('blob')
        
        # "output" and "expected" will be equivalent if the operation was completed successfully.
        output = broken_analyzer.init_error
        expected = 'Error - The argument entered for "game_object" must be of type "montecarlo.Game".'
        # This message will be displayed if the operation was unsuccessful.
        message = 'Error - The argument entered for "game_object" was not of type "montecarlo.Game".' 
        self.assertEqual(output, expected, message)
        
        
    def test_09_Analyzer_jackpot(self):
        '''
        Purpose: Ensure the Analyzer.jackpot() method does not incorrectly classify jackpots.
        '''
        inputs = [1, 2, 3, 4, 5, 6]
        die1 = montecarlo.Die(inputs)
        die2 = montecarlo.Die(inputs)
        die1.change_weights(1, 1000)
        die1.change_weights(6, .001)
        die2.change_weights(6, 1000)
        die2.change_weights(1, .001)
        game = montecarlo.Game([die1, die2])
        game.play(100)
        analyzer = montecarlo.Analyzer(game)
        
        # "output" and "expected" will be equivalent if the operation was completed successfully.
        output = analyzer.jackpot()
        expected = 0
        # This message will be displayed if the operation was unsuccessful.
        message = 'Error - The Analyzer.jackpot() incorrectly identifies jackpots.' 
        self.assertEqual(output, expected, message)
        
        
    def test_10_Analyzer_combo(self):
        '''
        Purpose: Ensure the Analyzer.combo() method correctly sorts the face combinations.
        '''
        inputs = [1, 2, 3, 4, 5, 6]
        die = montecarlo.Die(inputs)
        game = montecarlo.Game([die, die])
        game.play(25)
        analyzer = montecarlo.Analyzer(game)
        analyzer.combo()
        output1 = list(analyzer.game_combo['n'])[0]
        output2 = list(analyzer.game_combo['n'])[1]
        
        # Will be "True" if the operation was completed successfully.
        testValue = output1 >= output2
        # This message will be displayed if the operation was unsuccessful.
        message = 'Error - The Analyzer.combo() method incorrectly sorts the face combinations.' 
        self.assertTrue(testValue, message)
    

    def test_11_Analyzer_face(self):
        '''
        Purpose: Ensure the Analyzer.face_count_per_row() method includes a row for each die face.
        '''
        inputs = [1, 2, 3, 4, 5, 6]
        die = montecarlo.Die(inputs)
        game = montecarlo.Game([die, die])
        game.play(25)
        analyzer = montecarlo.Analyzer(game)
        analyzer.face_count_per_row()
                
        # "output" and "expected" will be equivalent if the operation was completed successfully.
        output = analyzer.game_face_counts.shape[1]
        expected = len(inputs)
        # This message will be displayed if the operation was unsuccessful.
        message = 'Error - The Analyzer.face_count_per_row() method does not include a row for each die face.' 
        self.assertEqual(output, expected, message)
        
        
if __name__ == '__main__':
    
    unittest.main(verbosity=2)