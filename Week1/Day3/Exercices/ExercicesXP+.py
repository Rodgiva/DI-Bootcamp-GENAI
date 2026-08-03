from pprint import pprint

# --- 🌟 Exercise 1 : Student Grade Summary ---
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}
student_averages = {}
student_letter_grades = {}
grade_sum = 0
grade_length = 0
class_avg = 0
for k,v in student_grades.items():
    avg_student = sum(v)/len(v)
    student_averages[k] = avg_student

    grade = ""
    if avg_student >= 90:
        grade = "A"
    elif 80 <= avg_student < 90:
        grade = "B"
    elif 70 <= avg_student < 80:
        grade = "C"
    elif 60 <= avg_student < 70:
        grade = "D"
    elif avg_student < 60: 
        grade = "F"
    student_letter_grades[k] = grade

    grade_sum += sum(v)
    grade_length += len(v)

    print(f"{k}\n Average Grades: {avg_student} -> {grade}")
print(student_averages)
print(student_letter_grades)
class_average = grade_sum/grade_length
print(class_average)

print("--------------------------")

# --- 🌟 Exercise 2 : Advanced Data Manipulation and Analysis ---
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

total_sales = {}
sales_by_customer = {}
for item in sales_data:
    if item["product"] in total_sales:
        total_sales[item["product"]] = total_sales[item["product"]] + (item["price"] * item["quantity"])
    else:
        total_sales[item["product"]] = item["price"] * item["quantity"]

    if item["customer_id"] in total_sales:
        sales_by_customer[item["customer_id"]] = total_sales[item["customer_id"]] + (item["price"] * item["quantity"])
    else:
        sales_by_customer[item["customer_id"]] = item["price"] * item["quantity"]

    item["total_price"] = item["price"] * item["quantity"]
print(total_sales)
print(sales_by_customer)
print(sales_data)

# high_value_list = [item for item in sales_data if (item["price"] * item["quantity"]) > 500]
high_value_list = [item for item in sales_data if item["total_price"] > 500]
high_value_list.sort(key=lambda item: item["total_price"])
print(high_value_list)

print(sales_by_customer)

# loyal_customers = [item for item in sales_data ]
loyalty_list = {}
for item in sales_data:
    if item["customer_id"] not in loyalty_list:
        loyalty_list[item["customer_id"]] = 1
    else:
        loyalty_list[item["customer_id"]] += 1

for item in sales_data:
    if item["customer_id"] <= 1:
        sales_data.pop(item["customer_id"])
print(loyalty_list)


print("--------------------------")
