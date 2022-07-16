Metadata
========
Package Name: montecarlo  
Author: Dominick DeCanio

Synopsis
============
This section contains code demonstrating how each class in this package is used.

Installing montecarlo
---------------------
Steps required to successfully install the montecarlo package:

1. Clone the package github repository to your local machine.  
Link to the repository: https://github.com/domdecanio/montecarlo

2. Navigate to the package directory and run one of the following commands in your terminal:

```
pip install .

python setup.py install
python setup.py build
```
The terminal should display "install montecarlo successful" if the package was installed correctly.

Importing montecarlo
--------------------
There are two methods for successfully importing this package into your desired python workspace:
1. **import montecarlo**  
Within your python file, you must then specify the package name as a prefix for calling any of the classes within the montecarlo package.

   Example:  
   ```python
   import montecarlo
   
   x = montecarlo.Die()  
   x = montecarlo.Game()  
   x = montecarlo.Analyzer()
   ```

2. **from montecarlo import Die, Game, Analyzer**  
There are many variations on this menthod, such as "from x import * ", and they interact with the package in the same way. Using this method, you may call the classes within the montecarlo package directly.

   Example:  
   ```python
   from montecarlo import Die, Game, Analyzer
   
   x = Die()  
   x = Game()  
   x = Analyzer()
   ```

Creating & Using "Die" objects
------------------------------
### Create a "Die" object
To instatiate a "Die" object, you must pass a list of face values upon instantiation. This list may be composed of integers or strings, or a subset of both.

   Examples:
   ```python
   face_values1 = ['H', 'T']
   face_values2 = [1, 2, 3, 4, 5, 6]
   
   x1 = montecarlo.Die(face_values1)
   x2 = montecarlo.Die(face_values2)
   ```

**Note:** It is important to understand the connection between the "Die" object's attributes, and the Monte Carlo simulation it represents. Each "Die" object has both face values and weights.

   face value - The outcome displayed when the face is the outcome of a roll (weighted random selection)  
   weight     - The weight corresponding to a face value on the die
   
By default, instantiating a "Die" object creates a list of weights corresponding to the list of face values passed. All default face value weights are 1. Therefore, rolling a die whose weights have not been altered will result in a roll in which each face has an equal probability of being selected. 

### Use a "Die" object
Now that the "Die" object has been created, any of its methods can be used to interact with the object. See the "Api Description" section to see all of these methods.


Creating & Using "Game" objects
-------------------------------
### Create a "Game" object
To instatiate a "Game" object, you must pass a list of "Die" objects. This list of dice represent the dice to be rolled simultaneously during any "play" of the game.

**Note:** All "Die" objects within the list passed must have the same face values, though their face weights can differ.
### Use a "Game" object

Creating & Using "Analyzer" objects
-----------------------------------
### Create a "Analyzer" object
### Use a "Analyzer" object

Api Description
===============
This Section of the documentation describes all classes of the montecarlo package, along with all their methods and attributes. This is formatted as a heirarchy, using the doc strings included in the package.


"Die" Class
-----------
```python
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
```

### .__init__(n)
```python
   def __init__(self, n):
        """
        Purpose: This method initializes "Die" objects that can be rolled to generate a face of the die.

        Inupts: n - (list) This is a list composed of str or int values, which indicate the number of 
                           sides on the die.
        Output: ("Die" object) "Die" object which has len(n) number of sides
        """
```

### .change_weights(face_value, new_weight)
```python
   def change_weights(self, face_value, new_weight):
        """
        Purpose: This method allows the user to change the weights of the die after it has 
                 been initialized.
        
        Inputs: face_value - (str or int) The face of the die object to which you will assign a new weight.
                new_weight - (int) The new weight for this face.
        Output: (None) Weights are changed in the object's attribute.
        """
```

### .roll(num_rolls=1)
```python
   def roll(self, num_rolls=1):
        """
        Purpose: This method allows the user to roll the die 1 or more times.
        
        Input: num_rolls - (int) Default value is 1. This argument indicates the number of times the die
                                 object will be rolled.
        Output: (list) Output is a list of values corresponding to the results of your rolls.
        """
```

### .show()
```python
   def show(self):
        """
        Purpose: This method shows the user the df containing the faces and weights.
        
        Input: (None)
        Output: (pd.DataFrame) Output returns the dataframe containing the die's face values and weights.
        """
```


"Game" Class
-----------
```python
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
```

### .__init__()
```python
   def __init__(self, dice):
        """
        Purpose: Initialize a "Game" object.
        
        Inupts: dice - (list) A list composed of "Die" objects, which indicate the number of dice 
                              to be rolled each time the game is played. 
                        NOTE: All "Die" objects included in this list must have the same value and
                              number of faces.
        Output: ("Game" object) "Game" object which is composed of len(dice) number of "Die" objects.
        """
```

### .play(num_rolls)
```python
   def play(self, num_rolls):
        """
        Purpose: Generate outcomes of a given quantity of rolls of the given dice objects.
        
        Input: num_rolls - (int) Indicates the number of times the dice will be rolled.
        Output: (None) Results are stored in a private pd.Dataframe that is an attribute of the 
                       "Game" object.
        """
```

### .show(df_format="wide")
```python
   def show(self, df_format="wide"):
        """
        Purpose: Show the user the results of the most recently played game.
        
        Input: df_format - ("wide" or "narrow") Chooses the format in which the dataframe of results 
                                                will display.
        Output: (pd.DataFrame) The Dataframe object containing the results of the most recently played 
                               game.
        """
```


"Analyzer" Class
-----------
```python
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
```

### .__init__(game_object)
```python
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
```

### .jackpot()
```python
   def jackpot(self):
        """
        Purpose: Creates a dataframe indicating all rows where the values for each die were equivalent.
                 A roll (row) of the results dataframe where all the die faces are equivalent is a 
                 "jackpot". This dataframe contains the original index of the roll, as well as the 
                 values of each "Die" object.
        
        Input: (None)
        Output: (int) Number of jackpots in the "Game" object's results.
        """
```

### .combo()
```python
   def combo(self):
        """
        Purpose: Count all unique combinations of roll results that appear in the "Game" object's results, 
                 sort them by frequency of appearance, and save this information to a dataframe.
        
        Input: (None)
        Output: (None) The results are saved to a pd.DataFrame as the class attribute "game_combo".
        """
```

### .face_count_per_row()
```python
   def face_count_per_row(self):
        """
        Purpose: Count the occurances of each die face value within a game's roll.
        
        Input: (None)
        Output: (None) The results are saved in the pd.DataFrame class attribute "game_face_counts".
        """
```

Manifest
========
