Course_Project_TAP
==================

This contains the code for my course project for Thinking and Approach of Programming.

The course project aims to solve one fundamental problem in material science via computer programming, i.e., calculating the phase proportion in two-composites system.

There are two models in this program. The first is the Fe-C Diagram Calculator with the Phase Diagram of Fe-C system. With each point by mouse in the diagram, the calculator will automatically come out with the name of the two phases, the proportion of each phase. The second model is with a GUI of a calculator, where users are able to get the output of the proportion with the input of the proportion of each composites.

==================

Classes and methods:
To realize these functions, the program introduced two classes: CPCal and MainGUI.

CPCal: This class is the main calculating class of the program. There are two methods: run() and judge()

1. run()
returns the proportions of the two phases from the proportions of the given composites.

2. judge()
determines whether the point the user wishes to calculate falls in the two-phase area, i.e., the problem is solvable. returns the basic information of the two phases needed to be calculated.

MainGUI: come up with the Interfaces of the calculator using TKinter.

1. Interone()
This interface is for Fe-C Diagram Calculator.

2. Intertwo()
This interace is for customized calculator.

main.py: Main function for realize the calculator.
