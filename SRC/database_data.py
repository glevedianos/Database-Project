from database_class import DataModel

db = DataModel("final.db")

# Companies
db.create_company(100000000, "Tutoring Center", "Bright Learning")
db.create_company(100000001, "Plumbing Services", "AquaTech Services")
db.create_company(100000002, "Department Store", "MetroMart")
db.create_company(100000003, "Tutoring Center", "SmartPath Academy")
db.create_company(100000004, "Law Firm", "Global Legal Advisors")
db.create_company(100000005, "Grill House", "Street Bites")
db.create_company(100000006, "Coffee Shop", "Daily Roast")

# Employees
db.create_employee(
    2000000000, "John", "Smith", "Mathematician",
    1415550123, "john.smith@example.com", "London", 1000
)

db.create_employee(
    2000000001, "Anna", "Brown", "Mathematician",
    4477009001, "anna.brown@example.com", "London", 800
)

db.create_employee(
    2000000002, "Michael", "Johnson", "Lawyer",
    1212555234, "michael.johnson@example.com", "New York", 1000
)

db.create_employee(
    2000000003, "Emily", "Davis", "Doctor",
    3314222333, "emily.davis@example.com", "Paris", 1500
)

db.create_employee(
    2000000004, "Sophia", "Miller", "Waiter",
    4930123456, "sophia.miller@example.com", "Berlin", 700
)

db.create_employee(
    2000000005, "David", "Wilson", "Refrigeration Technician",
    3902123456, "david.wilson@example.com", "Milan", 800
)

db.create_employee(
    2000000006, "James", "Taylor", "Cashier",
    6129876543, "james.taylor@example.com", "Sydney", 600
)

db.create_employee(
    2000000007, "Laura", "Anderson", "Cashier",
    1416555987, "laura.anderson@example.com", "Toronto", 750
)

# Job Positions
db.create_position(100000000, "Mathematician", "London", 1300)
db.create_position(100000000, "Philologist", "London", 1300)
db.create_position(100000000, "Chemist", "London", 1300)

db.create_position(100000002, "Cashier", "New York", 800)
db.create_position(100000002, "Accountant", "New York", 1500)

db.create_position(100000003, "Mathematician", "Paris", 900)

db.create_position(100000005, "Cashier", "Milan", 700)
db.create_position(100000005, "Refrigeration Technician", "Milan", 800)

db.create_position(100000006, "Cashier", "Berlin", 900)
db.create_position(100000006, "Waiter", "Berlin", 900)

# Contracts
db.create_contract(100, "10-10-2010", "10-10-2020")
db.create_contract(101, "05-08-2000", "01-01-2001")
db.create_contract(102, "15-07-2011", "15-07-2015")
db.create_contract(103, "07-03-2020", "07-03-2021")
db.create_contract(104, "17-10-2018", "17-10-2028")
db.create_contract(105, "06-11-2015", "06-11-2017")

# Contract Signings
db.create_signing(100, 100000004, 2500)
db.create_signing(101, 100000002, 1000)
db.create_signing(102, 100000002, 1000)

# Contract Closings
db.create_closing(103, 2000000002, 1500)
db.create_closing(104, 2000000003, 1400)
db.create_closing(105, 2000000000, 1200)
