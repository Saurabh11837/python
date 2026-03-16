# Multipla Inheritance Problem ,
# ---- This problem not solved in java, becaause in java occur the ambiguty problem.
# Diamond Problem in Python – Step by Step
# 1️⃣ Problem Setup

# Diamond Problem tab hota hai jab:

#       A
#      / \
#     B   C
#      \ /
#       D

# A = Grandparent class
# B and C = Parents (inherit from A)
# D = Child (inherits from B and C)
# Agar A me koi method hai, aur B & C me override hua, to D call kare to ambiguity hoti hai ki kaunsa method execute hoga?
# 2️⃣ Python Code Example
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()
# 3️⃣ Step 1 – Check Method Resolution Order (MRO)
# Python internally C3 Linearization ka use karta hai to calculate D ka MRO:

print(D.mro())

# Output:
# [D, B, C, A, object]

# Explanation:
# D → child class
# B → left parent first
# C → right parent next
# A → common grandparent

# object → Python base class

# ✅ C3 Linearization ensures:
# Child comes before parents
# Left-to-right parent order preserved
# No duplicate classes in search path

# 4️⃣ Step 2 – Method Lookup

obj.show() #call karte hain:

# Python check karta hai D → show() nahi mila
# Fir B → show() mila → execute B ka show()
# C aur A check nahi kiye jaate, kyunki method mil chuka

# Output:

# B

# 💡 No ambiguity! Python auto-resolved using MRO.



# --Full Explanation -----
"Python allows multiple inheritance and solves diamond problem automatically using MRO (C3 Linearization). The child class searches methods in a deterministic order: child → left parent → right parent → common ancestors. In contrast, Java prevents multiple inheritance of classes to avoid this problem."


