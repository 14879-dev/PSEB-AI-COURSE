
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 11-11-2026

# ==========================================
# PART 11: TYPE HINTS AND DATACLASSES
# ==========================================

from dataclasses import dataclass, field, asdict
import json


# ==========================================
# WARM-UP: TYPE HINTS
# ==========================================

print("\n========== WARM-UP: TYPE HINTS ==========")


# Function to calculate area of a circle
def area_of_circle(r: float) -> float:
    return 3.14159 * r * r


# Function to check whether a number is even
def is_even(n: int) -> bool:
    return n % 2 == 0


# Function to greet in English or Urdu
def greet(name: str, lang: str = "en") -> str:
    if lang == "ur":
        return f"Salaam {name}!"
    return f"Hello {name}!"


# Function to calculate average marks
def average(marks: list[int]) -> float:
    return sum(marks) / len(marks)


# Function to calculate grade
def grade(marks: list[int]) -> str:
    avg = average(marks)

    if avg < 0 or avg > 100:
        return "Invalid Marks"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 33:
        return "D"
    else:
        return "Fail"


# Function to generate student report
def report(name: str, marks: list[int]) -> str:
    avg = average(marks)
    student_grade = grade(marks)

    return f"{name} | Average: {avg:.2f} | Grade: {student_grade}"


print("Area:", area_of_circle(5))
print("Even:", is_even(10))
print("Greeting:", greet("Mudassir"))
print("Greeting Urdu:", greet("Ali", "ur"))
print("Average:", average([80, 75, 90]))
print("Grade:", grade([80, 75, 90]))
print("Report:", report("Ahmed", [90, 85, 95]))


# ==========================================
# BUILD: PRODUCT DATACLASS
# ==========================================

print("\n========== BUILD: PRODUCT DATACLASS ==========")


@dataclass
class Product:
    name: str
    price: float
    stock: int
    tags: list[str] = field(default_factory=list)

    # Validate product data after object creation
    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("Price cannot be negative")

        if self.stock < 0:
            raise ValueError("Stock cannot be negative")


# Create 5 products
products: list[Product] = [
    Product("Laptop", 150000, 5, ["Electronics", "Computer"]),
    Product("Mouse", 1500, 0, ["Electronics", "Accessory"]),
    Product("Keyboard", 3000, 8, ["Electronics"]),
    Product("Monitor", 35000, 0, ["Electronics", "Display"]),
    Product("Headphones", 5000, 3, ["Audio", "Accessory"])
]


# Display all products
print("\nAll Products:")

for product in products:
    print(product)


# Display products that are out of stock
print("\nOut of Stock Products:")

for product in products:
    if product.stock == 0:
        print(product.name)


# ==========================================
# CHALLENGE: SAVE AND LOAD PRODUCTS
# ==========================================

print("\n========== CHALLENGE: JSON SAVE AND LOAD ==========")


# Save products into JSON file using asdict()
product_data = [asdict(product) for product in products]

with open("products.json", "w") as file:
    json.dump(product_data, file, indent=4)

print("\nProducts saved to products.json")


# Load products from JSON file
with open("products.json", "r") as file:
    loaded_data = json.load(file)


# Convert dictionaries back into Product objects
loaded_products: list[Product] = [
    Product(**data) for data in loaded_data
]

print("\nLoaded Products:")

for product in loaded_products:
    print(product)


# ==========================================
# SORT PRODUCTS BY PRICE
# ==========================================

print("\n========== PRODUCTS SORTED BY PRICE ==========")


# Add order=True to the dataclass for automatic ordering.
# Sorting by price is done explicitly using the price key.
sorted_products = sorted(loaded_products, key=lambda product: product.price)

for product in sorted_products:
    print(f"{product.name} - Rs. {product.price}")


print("\n========== PROGRAM FINISHED ==========")
