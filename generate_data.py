from faker import Faker
import pandas as pd
fake = Faker()
import random
customer=[]
for i in range(100):
    customer.append({
        'customer_id': i+1,
        'name': fake.name(),
        'city': fake.city(),
        'join_date': fake.date_between(start_date='-3y', end_date='today'),
        'phone' : '01' + ''.join(str(random.randint(0,9)) for _ in range(9))
    })
customer_df=pd.DataFrame(customer)
print(customer_df.head())
customer_df.to_csv('customer_data.csv', index=False)
print("Customer data generated and saved to customer_data.csv")
branches = ["Cairo", "Giza", "Alexandria", "Mansoura", "Tanta"]
roles = [
    "Manager",
    "Cashier",
    "Sales",
    "Supervisor",
    "Accountant"
]
Employee=[]
for i in range(100):
    Employee.append({
        'employee_id': i+1,
        'name': fake.name(),
        'branch':random.choice(branches),
        'role': random.choice(roles),
    })
employee_df=pd.DataFrame(Employee)
print(employee_df.head())
employee_df.to_csv('employee_data.csv', index=False,encoding="utf-8-sig")
print("Employee data generated and saved to employee_data.csv")
products = []

products_by_category = {
    "Laptop": [
        "Dell Inspiron",
        "HP Pavilion",
        "Lenovo ThinkPad",
        "MacBook Air",
        "Asus VivoBook",
        "Acer Aspire",
        "MSI Modern",
        "Huawei MateBook"
    ],

    "Mobile": [
        "iPhone 15",
        "Samsung Galaxy S24",
        "Xiaomi Redmi Note 13",
        "Oppo Reno 12",
        "Realme 12",
        "Google Pixel 9",
        "Huawei Nova 13",
        "Honor X9"
    ],

    "Tablet": [
        "iPad Air",
        "Samsung Galaxy Tab S9",
        "Lenovo Tab P12",
        "Huawei MatePad",
        "Xiaomi Pad 6",
        "Amazon Fire HD"
    ],

    "Accessories": [
        "Wireless Mouse",
        "Mechanical Keyboard",
        "USB-C Charger",
        "Laptop Bag",
        "Bluetooth Speaker",
        "Power Bank",
        "USB Flash Drive",
        "Webcam",
        "Gaming Headset",
        "Wireless Earbuds"
    ],

    "Monitor": [
        "Dell 24 Monitor",
        "Samsung Odyssey",
        "LG UltraWide",
        "HP M24",
        "AOC Gaming Monitor",
        "ASUS ProArt",
        "BenQ GW2480"
    ]
}

colors = [
    "Black",
    "White",
    "Silver",
    "Blue",
    "Gray",
    "Gold"
]

for i in range(100):

    category = random.choice(list(products_by_category.keys()))

    cost = round(random.uniform(100, 3000), 2)
    sell = round(cost * random.uniform(1.1, 1.5), 2)

    products.append({
    "product_id": i + 1,
    "name": random.choice(products_by_category[category]),
    "category": category,
    "cost_price": cost,
    "sell_price": sell,
    "stock_qty": random.randint(0, 300),
    "brand_id": random.randint(1, 20),
    "supplier_id": random.randint(1, 50),
    "warranty_months": random.choice([6, 12, 24, 36]),
    "weight": round(random.uniform(0.2, 8), 2),
    "color": random.choice(colors),
    "launch_date": fake.date_between(
        start_date="-5y",
        end_date="today"
    )
})

products_df = pd.DataFrame(products)

print(products_df.head())

products_df.to_csv(
    "products_data.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Products data generated successfully.")
orders = []

payment_methods = ['cash','card','wallet']

delivery_statuses = [
    "Delivered",
    "Pending",
    "Shipped",
    "Cancelled"
]

for i in range(5000):

    order_date = fake.date_between(
        start_date='-2y',
        end_date='today'
    )

    status = random.choice(delivery_statuses)

    orders.append({
        'order_id': i + 1,
        'customer_id': random.randint(1, 100),
        'employee_id': random.randint(1, 100),
        'payment_method': random.choice(payment_methods),
        'total_amount': round(random.uniform(100, 100000), 2),
        'order_date': order_date,
        'promotion_id': random.choice(list(range(1,31)))
        ,

        'delivery_status': status,

        'shipping_cost': round(
            random.uniform(20,300),
            2
        ),

        'delivery_date': fake.date_between(
            start_date=order_date,
            end_date='today'
        )
    })


df_orders = pd.DataFrame(orders)

print(df_orders.head())

df_orders.to_csv(
    'orders_data.csv',
    index=False,
    encoding='utf-8-sig'
)

print("Orders data generated successfully")
order_items=[]
for i in range(1500):
    order_items.append({
        'order_item_id': i+1,
        'order_id': random.randint(1, 500),
        'product_id': random.randint(1, 100),
        'quantity': random.randint(1, 10),
        'unit_price': round(random.uniform(50, 5000), 2)

    }

    )
order_items_df=pd.DataFrame(order_items)
print(order_items_df.head())
order_items_df.to_csv('order_items_data.csv', index=False)
print("Order items data generated and saved to order_items_data.csv")
brands = [
    "Apple",
    "Samsung",
    "Dell",
    "HP",
    "Lenovo",
    "Asus",
    "Acer",
    "Huawei",
    "Xiaomi",
    "Oppo",
    "Realme",
    "Google",
    "Honor",
    "MSI",
    "LG",
    "AOC",
    "BenQ",
    "Amazon",
    "Microsoft",
    "Razer"
]

brand_data = []

countries = [
    "USA",
    "South Korea",
    "China",
    "Japan",
    "Germany"
]

for i, brand in enumerate(brands):
    brand_data.append({
        "brand_id": i+1,
        "brand_name": brand,
        "country": random.choice(countries),
        "founded_year": random.randint(1970, 2015),
        "website": f"www.{brand.lower()}.com",
        "support_email": f"support@{brand.lower()}.com",
        "phone": "01" + ''.join(str(random.randint(0,9)) for _ in range(9)),
        "status": "Active"
    })

brand_df = pd.DataFrame(brand_data)

brand_df.to_csv(
    "brand_data.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Brand data generated")
supplier_data=[]

for i in range(50):
    supplier_data.append({
        "supplier_id": i+1,
        "supplier_name": fake.company(),
        "contact_person": fake.name(),
        "phone": "01" + ''.join(str(random.randint(0,9)) for _ in range(9)),
        "email": fake.email(),
        "city": fake.city(),
        "country": fake.country(),
        "address": fake.address().replace("\n"," "),
        "rating": round(random.uniform(3,5),2),
        "contract_start": fake.date_between(start_date="-5y"),
        "status": "Active"
    })


supplier_df=pd.DataFrame(supplier_data)

supplier_df.to_csv(
    "supplier_data.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Supplier data generated")
promotion_data = []

types = [
    "Discount",
    "Seasonal",
    "Clearance",
    "Special Offer"
]
promotion_names = [
    "Summer Sale",
    "Black Friday",
    "Flash Sale",
    "New Year Offer",
    "Ramadan Offer",
    "Buy 1 Get 1",
    "Weekend Deal",
    "Back to School",
    "Mega Discount",
    "Clearance Sale",
    "Holiday Special",
    "Student Offer",
    "Tech Week",
    "Cyber Monday",
    "Free Shipping",
    "Bundle Deal",
    "Loyalty Reward",
    "VIP Exclusive",
    "Limited Time Offer",
    "Member Discount",
    "Winter Sale",
    "Spring Festival",
    "Anniversary Sale",
    "Early Bird Offer",
    "Hot Deals",
    "Super Saver",
    "Family Pack",
    "Midnight Sale",
    "Special Weekend",
    "End of Season Sale"
]

for i in range(30):
    promotion_data.append({
        "promotion_id": i + 1,
        "promotion_name":random.choice(promotion_names),
        "promotion_type": random.choice(types),
        "discount_percent": random.randint(5, 50),
        "minimum_order": round(random.uniform(100, 5000), 2),
        "start_date": fake.date_between(start_date="-2y"),
        "end_date": fake.date_between(start_date="today"),
        "coupon_code": f"SALE{i+1}",
        "usage_limit": random.randint(50, 500),
        "status": "Active"
    })

promotion_df = pd.DataFrame(promotion_data)

promotion_df.to_csv(
    "promotion_data.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Promotion data generated")
returns = []

reasons = [
    "Damaged product",
    "Wrong item",
    "Customer changed mind",
    "Defective product"
]

statuses = [
    "Approved",
    "Pending",
    "Rejected"
]

for i in range(1000):
    returns.append({
    "return_id": i + 1,
    "order_items_id": random.randint(1, 1500),
    "order_id": random.randint(1, 500),
    "customer_id": random.randint(1, 100),
    "return_date": fake.date_between(start_date="-2y"),
    "return_reason": random.choice(reasons),
    "return_status": random.choice(statuses),
    "refund_amount": round(random.uniform(50, 5000), 2),
    "approved_by": fake.name(),
    "notes": fake.sentence()
})

returns_df = pd.DataFrame(returns)

returns_df.to_csv(
    "returns_data.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Returns data generated")


