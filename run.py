from cellularAutomata3State import *

test_get_lookup_table0()
test_get_lookup_table3()

ca = cellularAutomata3State(leng=100, rulenum=110)
ca.plot_spacetime_field(time=100)
