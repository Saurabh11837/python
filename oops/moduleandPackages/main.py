
# =================================================================================
#                       Module and packages
# 
# What is Module in Python?
# --> Module is just a single file containting code and we can use this file code in other file.
# --> A single Python file (.py)
# --> Contains functions, variables, or classes
# --> Use to organize and reuse code
# --> Python comes with lots of ready-to-use modules like:
#   * math (for math operations)
#   * random (for generating random number)
#   * datetime (for date and time)

# A Package is a  folder that contains one or more modules (Python files). It may also contain sub-packages.
# And you just have to use from and import keywords to use the se things. You understood how these things work.
# There are third party packages as well like numpy. pandas., matplotib etc. and we hav to install all of these.

# =================================================================================
# ***************************************************************************************************************************

# __pycache__ folder kya hai?
# 1.Jab Python koi .py file (module/package) import karta hai, toh wo us code ko compile karke bytecode me convert karta hai.
# 2.Bytecode ek intermediate, machine-friendly format hota hai, jo Python interpreter ko fast execution me help karta hai.
# 3.Ye compiled files .pyc extension ke saath __pycache__ folder me store hoti hain.
# 4.Matlab, Python tumhare source code ka compiled version store kar raha hai.



# ***************************************************************************************************************************
# --------- Module imported  --------
# import math_utils

# print(math_utils.add(3,5))
# print(math_utils.subtract(10,8))


from my_package import hello,maths
print(maths.add(15,15))
print(maths.multiplication(15,15))























































