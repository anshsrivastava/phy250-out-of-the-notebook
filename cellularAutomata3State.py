import random
from matplotlib import pyplot as plt


class cellularAutomata3State:
    rule_number = 0
    initial_condition = []
    length = 100
    
    def __init__(self, leng, rulenum):
        '''
        Initializes the initial condition and rule number that will be used later to simulate cellular automata.
        
        Parameters
        ----------
        rule_num: int
            Integer value between 0 and 3^9. The value indicates the rule being followed for the cellular automata.
        leng: int
            Integer value greater than 0 which indicates the number of cells to simulate in the cellular automata. 
        '''
        # Setting the rule number
        self.rule_number = rulenum
        self.length = leng
        initial_conditions = []
        # Initializing the initial condition list
        for i in range(self.length):
            initial_conditions.append(random.randint(0,2))
        self.initial_condition = initial_conditions
        
        
    def get_lookup_table(self): # Gets the lookup table dictionary
        '''
        Generates a dictionary with rules to transform the system of cells based on the left and current elements in the list.
        
        Returns
        -------
        lookup_table: dictionary 
            Contains the neighbors and the new value of the above cell as a key-value pair
        '''
        neighborhoods = [(0,0), (0,1), (1,0), (2,1), (2,2), (0,2), (2,0), (1,2), (1,1)]
        lookup_table = {}
        rule = self.rule_number
        for i in range(9):
            key = neighborhoods[i]
            val = rule % 3
            rule = rule // 3
            lookup_table.update({key:val})
        return lookup_table

    def get_spacetime_field(self, time):
        '''
        Generates a list that contains the time evolution and state of the cellular automata at every stage.
        
        Parameters
        ----------
        time: int
            Integer value greater than 0 that indicates the time the cellular automata will be simulated for
        
        Returns
        -------
        spacetime_field: 2D list 
            Contains the time evolution for every integer time between 0 and our parameter time.
        '''
        lookup_table = self.get_lookup_table()
        spacetime_field = [self.initial_condition]
        current_configuration = self.initial_condition.copy()
        # apply the lookup table to evolve the CA for the given number of time steps
        for t in range(time):
            new_configuration = []
            for i in range(len(current_configuration)):
                neighborhood = (current_configuration[i], current_configuration[i-1])
                new_configuration.append(int(lookup_table[neighborhood]))
        
            current_configuration = new_configuration
            spacetime_field.append(new_configuration)
        
        return spacetime_field
    
    def plot_spacetime_field(self, time):
        '''
        Plots the evolution of the cellular automata from 0 to a specified time.
        
        Parameters
        ----------
        time: int
            Integer value greater than 0 that indicates the time the cellular automata will be simulated for.
        '''
        spacetime_field = self.get_spacetime_field(time)
        # plot the spacetime field diagram
        plt.figure(figsize=(12,12))
        plt.imshow(spacetime_field, cmap=plt.cm.Greys, interpolation='nearest')
        plt.show()
    
def test_get_lookup_table0():
    '''
    Test the lookup table of rules for rule 0
    '''
    tst = cellularAutomata3State(leng=100, rulenum=0)
    assert tst.get_lookup_table() == {(0, 0): 0, (0, 1): 0, (1, 0): 0, 
                                      (2, 1): 0, (2, 2): 0, (0, 2): 0, (2, 0): 0, (1, 2): 0, (1, 1): 0}
    print("get_lookup_table() works for rule 0! ")
    
def test_get_lookup_table3():
    '''
    Test the lookup table of rules for rule 3
    '''
    tst = cellularAutomata3State(leng=100, rulenum=3)
    assert tst.get_lookup_table() == {(0, 0): 0, (0, 1): 1, (1, 0): 0, (2, 1): 0, 
                                      (2, 2): 0, (0, 2): 0, (2, 0): 0, (1, 2): 0, (1, 1): 0}
    print("get_lookup_table() works fo rule 3! ")
