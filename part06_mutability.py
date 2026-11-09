
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 06-11-2026

import copy

# ==========================================
# PART 6: REFERENCES & MUTABILITY
# ==========================================


# ==========================================
# WARM-UP: REFERENCES AND ALIASES
# ==========================================

print("\n========== WARM-UP ==========")

# Two variables referring to the same list
a = [10, 20, 30]

b = a

# Append an item using b
b.append(40)

print("After appending:")
print("a =", a)
print("b =", b)

# Create a separate copy
c = a.copy()

c.append(50)

print("\nAfter copying and appending:")
print("a =", a)
print("c =", c)

# Check identity and equality
print("\nIdentity and Equality:")

print("a is b:", a is b)
print("a == b:", a == b)

print("a is c:", a is c)
print("a == c:", a == c)


# ==========================================
# BUILD: MUTABLE DEFAULT ARGUMENT
# ==========================================

print("\n========== BUILD ==========")

# Incorrect function: mutable default argument
def add_item_bug(item, cart=[]):
    cart.append(item)
    return cart


print("Demonstrating the bug:")

print(add_item_bug("Apple"))
print(add_item_bug("Banana"))


# Correct function: using None
def add_item_fixed(item, cart=None):

    if cart is None:
        cart = []

    cart.append(item)

    return cart


print("\nAfter fixing the bug:")

print(add_item_fixed("Apple"))
print(add_item_fixed("Banana"))


# ==========================================
# CHALLENGE: SHALLOW AND DEEP COPY
# ==========================================

print("\n========== CHALLENGE ==========")

# Original nested dictionary
classes = {
    "Class A": ["Ali", "Ahmed"],
    "Class B": ["Sara", "Usman"]
}

print("Original Dictionary:")
print(classes)


# SHALLOW COPY
shallow_copy = copy.copy(classes)

# Modify the nested list
shallow_copy["Class A"].append("Ayesha")

print("\nAfter Shallow Copy Modification:")

print("Original:")
print(classes)

print("Shallow Copy:")
print(shallow_copy)


# DEEP COPY
deep_copy = copy.deepcopy(classes)

# Modify the nested list
deep_copy["Class B"].append("Mudassir")

print("\nAfter Deep Copy Modification:")

print("Original:")
print(classes)

print("Deep Copy:")
print(deep_copy)


print("\n========== PROGRAM FINISHED ==========")
