import numpy as np
import pandas as pd



## Die Class ##



class Die():
    """
    A class used to represent a die whose faces are customizable, and can be rolled.
    
    Attributes
    ----------
    faces : list
        A list of the faces of the corresponding "Die" object
    weights : ndarray
        Array of weights, where the index of the "weights" array corresponds to the index of the 
        "faces" list.
    
    Methods
    ------
    __init__(n)
        Initializes the "Die" object using a list of faces "n".
    change_weights(face_value, new_weight)
        Alters the weight(s) of given face(s).
    roll(num_rolls=1)
        Rolls the "Die" object a given number of times (default once).
    show()
        Returns the private pd.Dataframe containing the faces and corresponding weights of the 
        "Die" object.
    """
    def __init__(self, n):
        """
        Purpose: This method initializes "Die" objects that can be rolled to generate a face of the die.

        Inupts: n - (list) This is a list composed of str or int values, which indicate the number of 
                           sides on the die.
        Output: ("Die" object) "Die" object which has len(n) number of sides
        """
        counter = 0
        for i in n:
            try:
                assert isinstance(i, str) == True or \
                    (isinstance(i, int) == True and isinstance(i, bool) != True)
                counter += 1
            except:
                self.init_error = "Error - Input for argument 'n' is not of type: str or int"
                print("Error - Input for argument 'n' is not of type: str or int")
        if counter == len(n):
            self.faces = n
            self.weights = np.ones_like(self.faces, dtype = np.float64)
            self.__private_df = pd.DataFrame({'face': self.faces, 'weights': self.weights})
    
    def change_weights(self, face_value, new_weight):
        """
        Purpose: This method allows the user to change the weights of the die after it has 
                 been initialized.
        
        Inputs: face_value - (str or int) The face of the die object to which you will assign a new weight.
                new_weight - (int) The new weight for this face.
        Output: (None) Weights are changed in the object's attribute.
        """
        if isinstance(face_value, list):
            for index, value in enumerate(face_value):
                if value in self.__private_df['face'].values:
                    if isinstance(new_weight[index], float) != True:
                        try:
                            new_weight[index] = float(new_weight[index])
                            self.__private_df.loc[self.__private_df['face'] == value, 'weights'] = new_weight[index]
                        except:
                            print('Error - The weight passed is invalid. It is not a float, and cannot be converted to be one.')
                    else:
                        self.__private_df.loc[self.__private_df['face'] == value, 'weights'] = new_weight[index]        
                else: 
                    print('Error - The face value passed is invalid. It is not a valid face on the die.')
        else:
            if face_value in self.__private_df['face'].values:
                if isinstance(new_weight, float) != True:
                    try:
                        new_weight = float(new_weight)
                        self.__private_df.loc[self.__private_df['face'] == face_value, 'weights'] = new_weight
                    except:
                        print('Error - The weight passed is invalid. It is not a float, and cannot be converted to be one.')
                else:
                    self.__private_df.loc[self.__private_df['face'] == face_value, 'weights'] = new_weight        
            else: 
                print('Error - The face value passed is invalid. It is not a valid face on the die.')
      
    def roll(self, num_rolls=1):
        """
        Purpose: This method allows the user to roll the die 1 or more times.
        
        Input: num_rolls - (int) Default value is 1. This argument indicates the number of times the die
                                 object will be rolled.
        Output: (list) Output is a list of values corresponding to the results of your rolls.
        """
        return (self.__private_df['face'].sample(n=num_rolls, replace=True, weights=self.__private_df['weights'])).tolist()
    
    def show(self):
        """
        Purpose: This method shows the user the df containing the faces and weights.
        
        Input: (None)
        Output: (pd.DataFrame) Output returns the dataframe containing the die's face values and weights.
        """
        return self.__private_df
    
    
    
## Game Class ##
    
    
    
class Game():
    """
    A class used to represent a game of rolling many dice. Note that all dice in a single game must have 
    the same values and number of faces. They are NOT required to have the same weights for their faces.
    
    Attributes
    ----------
    dice_faces : list
        A list of the faces of the "Die" objects therein
    dice : list
        Array of weights, where the index of the "weights" array corresponds to the index of the 
        "faces" list.
    
    Methods
    ------
    __init__(dice)
        Initializes a "Game" object using a list of "Dice" objects in the parameter "dice".
    play(num_rolls)
        Rolls the given list of dice objects a customizable number of time.
    show(df_format="wide")
        Shows the user the results of the most recently played game.
    """
    def __init__(self, dice):
        """
        Purpose: Initialize a "Game" object.
        
        Inupts: dice - (list) A list composed of "Die" objects, which indicate the number of dice 
                              to be rolled each time the game is played. 
                        NOTE: All "Die" objects included in this list must have the same value and
                              number of faces.
        Output: ("Game" object) "Game" object which is composed of len(dice) number of "Die" objects.
        """
        self.dice_faces = dice[0].faces
        self.dice = dice
        
    def play(self, num_rolls):
        """
        Purpose: Generate outcomes of a given quantity of rolls of the given dice objects.
        
        Input: num_rolls - (int) Indicates the number of times the dice will be rolled.
        Output: (None) Results are stored in a private pd.Dataframe that is an attribute of the 
                       "Game" object.
        """
        try:
            assert isinstance(num_rolls, int) == True
            self.num_rolls = num_rolls
            self.__private_play_result_df = pd.DataFrame([x.roll(num_rolls) for x in self.dice])
        except:
            print('Error - The argument entered for "num_rolls" must be an integer.')

    def show(self, df_format="wide"):
        """
        Purpose: Show the user the results of the most recently played game.
        
        Input: df_format - ("wide" or "narrow") Chooses the format in which the dataframe of results 
                                                will display.
        Output: (pd.DataFrame) The Dataframe object containing the results of the most recently played 
                               game.
        """
        if df_format == "wide":
            return self.__private_play_result_df.T
        elif df_format == "narrow":
            return self.__private_play_result_df.stack()
        else:
            print('Error - The argument entered for "df_format" is invalid')
    

    
## Analyzer Class ##



class Analyzer():
    """
    A class used to analyze a "Game" object. 
    
    Attributes
    ----------
    dice_faces : list
        List of the faces of the dice used in the "Game" object to be analyzed.
    game_df : pd.DataFrame
        Dataframe containing the results of the most recently played game of the "Game" object.
    
    Methods
    ------
    __init__(game_object)
        Initializes an "Analyzer" object using a "Game" object in the parameter "game_object".
    jackpot()
        Returns the number of rolls in which all dice faces were matching.
    combo()
        Count all unique combinations of die faces in the game, and sort them.
    face_count_per_row()
        Count occurances of each face value in each roll of the game.
    """
    def __init__(self, game_object):
        """
        Purpose: Initialize an "Analyzer" object, which allows the user to conduct analysis on a "Game"
        object after that object has been passed the .play() method at least once. The subject of 
        analysis is the "Game" object's most recent play when it was used to instatiate the "Analyzer"
        object.
        
        Input: game_object - ("Game" object) A "Game" object that has been created using a list containing 
                                             one or more "Die" object(s).
        Output: (None) Generates the attributes:  dice_faces
                                                  game_df
        """
        try:
            self.dice_faces = game_object.dice_faces
            self.game_df = game_object.show('wide')
        except AttributeError:
            self.init_error = 'Error - The argument entered for "game_object" must be of type "montecarlo.Game".'
            print('Error - The argument entered for "game_object" must be of type "montecarlo.Game".')
        
    def jackpot(self):
        """
        Purpose: Creates a dataframe indicating all rows where the values for each die were equivalent.
                 A roll (row) of the results dataframe where all the die faces are equivalent is a 
                 "jackpot". This dataframe contains the original index of the roll, as well as the 
                 values of each "Die" object.
        
        Input: (None)
        Output: (int) Number of jackpots in the "Game" object's results.
        """
        self.game_jkpt = self.game_df.loc[lambda x: self.game_df.nunique(axis=1) == 1]
        return len(self.game_jkpt)
        
    def combo(self):
        """
        Purpose: Count all unique combinations of roll results that appear in the "Game" object's results, 
                 sort them by frequency of appearance, and save this information to a dataframe.
        
        Input: (None)
        Output: (None) The results are saved to a pd.DataFrame as the class attribute "game_combo".
        """
        self.game_combo = self.game_df.apply(lambda x: pd.Series(sorted(x)), 1)\
                             .value_counts()\
                                .to_frame('n')

    def face_count_per_row(self):
        """
        Purpose: Count the occurances of each die face value within a game's roll.
        
        Input: (None)
        Output: (None) The results are saved in the pd.DataFrame class attribute "game_face_counts".
        """
        all_faces = list()
        for i in range(0,len(self.game_df)):
            events_lst = list()
            for j in self.dice_faces:
                intermediate_lst = list(self.game_df.iloc[i].apply(lambda x: x == j))
                num = sum(intermediate_lst)
                events_lst.append(num)
            all_faces.append(events_lst)
        self.game_face_counts = pd.DataFrame(all_faces, columns=self.dice_faces)