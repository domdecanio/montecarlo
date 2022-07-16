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

### Using a "Die" object
Now that the "Die" object has been created, any of its methods can be used to interact with the object. See the "Api Description" section to see all of these methods.


Creating & Using "Game" objects
-------------------------------



Creating & Using "Analyzer" objects
-----------------------------------


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

```
Manifest
========
