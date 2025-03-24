# Brian Swanson & Nick Laustrup
# CS 340, Spring 2024
# Portfolio Project Flask Backend

# Citation for the following code:
# Date: 05/19/2024
# Copied from: CS 340 Flask Guide
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app


from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import datetime
from decimal import Decimal
import os

# Configuration

app = Flask(__name__)

mysql = MySQL(app)

# database connection info
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_swanbria"
app.config["MYSQL_PASSWORD"] = "IKWjiilHUyLz"
app.config["MYSQL_DB"] = "cs340_swanbria"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"


# db_connection = db.connect_to_database()

# Routes 

# redirect page to Customers
@app.route("/")
def home():
    # return redirect("/customers")
    return render_template('index.html')

@app.route('/customers', methods=["POST","GET"])
def customers():

    if request.method == "POST":
        # fire off if user presses the Add Person button
        if request.form.get("Add_Customer"):
            # grab user form inputs
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            email = request.form["email"]
            phone = request.form["phone"]
            address = request.form["address"]

            # address is null-able

            if address == "":
                # mySQL query to insert a new person into Customers with our form inputs
                query = "INSERT INTO Customers (firstName, lastName, email, phone) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, email, phone))
                mysql.connection.commit()
            
            # no null inputs

            else:
                query = "INSERT INTO Customers (firstName, lastName, email, phone, address) VALUES (%s, %s,%s,%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, email, phone, address))
                mysql.connection.commit()

            # redirect back to Customers page
            return redirect("/customers")

    if request.method == "GET":
        # mySQL query to grab all the people in Customers
        query = "SELECT Customers.customerID, firstName, lastName, email, phone, address FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

    return render_template("customers.html", data=data, header="Customers", id_type="customerID")

@app.route("/delete_customers/<int:customerID>")
def delete_customers(customerID):
    # mySQL query to delete the customer with our passed customerID
    query = "DELETE FROM Customers WHERE customerID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (customerID,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/customers")

@app.route("/edit_customers/<int:customerID>", methods=["POST", "GET"])
def edit_customers(customerID):
    if request.method == "GET":
        # mySQL query to grab the info of the customer with our passed customerID
        query = "SELECT * FROM Customers WHERE customerID = %s" % (customerID)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("edit_customers.html", data=data, header="Customers", id_type="customerID")
    
    if request.method == "POST":
        # fire off if user clicks the 'Edit Customer' button
        if request.form.get("Edit_Customer"):
            # grab user form inputs
            customerID = request.form["customerID"]
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            email = request.form["email"]
            phone = request.form["phone"]
            address = request.form["address"]

            # account for null address
            if (address == "" or address == "None"):
                # mySQL query to update the attributes of customer with our passed customerID value
                query = "UPDATE Customers SET Customers.firstName = %s, Customers.lastName = %s, Customers.email = %s, Customers.phone = %s, Customers.address = NULL WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, customerID))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "UPDATE Customers SET Customers.firstName = %s, Customers.lastName = %s, Customers.email = %s, Customers.phone = %s, Customers.address = %s WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, email, phone, address, customerID))
                mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/customers")

# Employees
@app.route('/employees', methods=["POST","GET"])
def employees():

    if request.method == "POST":
        # fire off if user presses the Add Person button
        if request.form.get("Add_Employee"):
            # grab user form inputs
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            email = request.form["email"]
            phone = request.form["phone"]
            wage = request.form["wage"]

            # wage is null-able

            if wage == "":
                # mySQL query to insert a new person into Employees with our form inputs
                query = "INSERT INTO Employees (firstName, lastName, email, phone) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, email, phone))
                mysql.connection.commit()
            
            # no null inputs

            else:
                query = "INSERT INTO Employees (firstName, lastName, email, phone, wage) VALUES (%s, %s,%s,%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, email, phone, wage))
                mysql.connection.commit()

            # redirect back to Employees page
            return redirect("/employees")

    if request.method == "GET":
        # mySQL query to grab all the people in Employees
        query = "SELECT Employees.employeeID, firstName, lastName, email, phone, wage FROM Employees"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

    return render_template("employees.html", data=data, header="Employees", id_type="employeeID")

@app.route("/delete_employees/<int:employeeID>")
def delete_employees(employeeID):
    # mySQL query to delete the employee with our passed employeeID
    query = "DELETE FROM Employees WHERE employeeID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (employeeID,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/employees")

@app.route("/edit_employees/<int:employeeID>", methods=["POST", "GET"])
def edit_employees(employeeID):
    if request.method == "GET":
        # mySQL query to grab the info of the employee with our passed employeeID
        query = "SELECT * FROM Employees WHERE employeeID = %s" % (employeeID)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("edit_employees.html", data=data, header="Employees")
    
    if request.method == "POST":
        # fire off if user clicks the 'Edit Employee' button
        if request.form.get("Edit_Employee"):
            # grab user form inputs
            employeeID = request.form["employeeID"]
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            email = request.form["email"]
            phone = request.form["phone"]
            wage = request.form["wage"]

            # account for null wage
            if (wage == "" or wage == "None"):
                # mySQL query to update the attributes of employee with our passed employeeID value
                query = "UPDATE Employees SET Employees.firstName = %s, Employees.lastName = %s, Employees.email = %s, Employees.phone = %s, Employees.wage = NULL WHERE Employees.employeeID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, employeeID))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "UPDATE Employees SET Employees.firstName = %s, Employees.lastName = %s, Employees.email = %s, Employees.phone = %s, Employees.wage = %s WHERE Employees.employeeID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, email, phone, wage, employeeID))
                mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/employees")
        
        
# Products
@app.route('/products', methods=["POST","GET"])
def products():

    if request.method == "POST":
        # fire off if user presses the Add Product button
        if request.form.get("Add_Product"):
            # grab user form inputs
            
            ####  PRODUCTS ####
            inStock = request.form["inStock"]
            price = request.form["price"]
            
            ####  PRODUCTDETAILS  ####
            type = request.form["type"]
            name = request.form["name"]
            
            ####  PRODUCTDETAILS  ####
            query = "INSERT INTO ProductDetails (name, type) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, type))
            mysql.connection.commit()
            
            ####  PRODUCTS ####
            query = "INSERT INTO Products (price, inStock, productDetailsID) VALUES (%s, %s, (SELECT productDetailsID FROM ProductDetails WHERE ProductDetails.name = %s LIMIT 1))"
            cur = mysql.connection.cursor()
            cur.execute(query, (price, inStock, name))
            mysql.connection.commit()
        

            # redirect back to Products page
            return redirect("/products")

    if request.method == "GET":
        # mySQL query to grab all the people in Products
        query = """
        SELECT productID, price, inStock, type, name, Products.productDetailsID 
        FROM Products 
        JOIN ProductDetails 
        ON Products.productDetailsID = ProductDetails.productDetailsID
        """
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

    return render_template("products.html", data=data, header="Products", id_type="productID")

@app.route("/delete_products/<int:productID>")
def delete_products(productID):
    # mySQL query to delete the product with our passed productID
    query = "DELETE FROM ProductDetails WHERE productDetailsID = (SELECT productDetailsID FROM Products WHERE productID = '%s')"
    query2 = "DELETE FROM Products WHERE productID = '%s';"

    cur = mysql.connection.cursor()
    cur.execute(query, (productID,))
    cur.execute(query2, (productID,))
    mysql.connection.commit()

    # redirect back to product page
    return redirect("/products")

@app.route("/edit_products/<int:productID>", methods=["POST", "GET"])
def edit_products(productID):
    if request.method == "GET":
        # mySQL query to grab the info of the product with our passed productID
        query = """
        SELECT productID, price, inStock, Products.productDetailsID, type, name FROM Products 
        JOIN ProductDetails 
        ON Products.productDetailsID = ProductDetails.productDetailsID 
        WHERE productID = %s
        """
        cur = mysql.connection.cursor()
        cur.execute(query, (productID,))
        data = cur.fetchall()

        return render_template("edit_products.html", data=data, header="Products", id_type="productID")
    
    if request.method == "POST":
        # fire off if user presses the Add Product button
        if request.form.get("Edit_Product"):
            # grab user form inputs
            
            ####  PRODUCTS ####
            inStock = request.form["inStock"]
            price = request.form["price"]
            
            ####  PRODUCTDETAILS  ####
            type = request.form["type"]
            name = request.form["name"]
            productDetailsID = request.form["productDetailsID"]

            ####  PRODUCTDETAILS  ####
            query = """
            UPDATE ProductDetails
            SET ProductDetails.name = %s, ProductDetails.type = %s 
            WHERE ProductDetails.productDetailsID = %s
            """
            cur = mysql.connection.cursor()
            cur.execute(query, (name, type, productDetailsID))
            mysql.connection.commit()
            
            ####  PRODUCTS ####
            query = """
            UPDATE Products 
            SET Products.price = %s, Products.inStock = %s
            WHERE Products.productID = %s
            """
            cur = mysql.connection.cursor()
            cur.execute(query, (price, inStock, productID))
            mysql.connection.commit()

            # redirect back to product page after we execute the update query
            return redirect("/products")



# Transactions
@app.route('/transactions', methods=["POST","GET"])
def transactions():

    if request.method == "POST":
        # fire off if user presses the Add Person button
        if request.form.get("Add_Transaction"):
            
            # grab user form inputs
            transactionDate = request.form["transactionDate"]
            transactionTime = request.form["transactionTime"]
            customerID = request.form["customer"]
            employeeID = request.form["employee"]
            product = request.form.getlist("product")
            
            # mySQL query to insert a new transaction into Transactions and Transactions_has_Product
            query1 = """INSERT INTO Transactions (customerID, employeeID, transactionDate, transactionTime)
                        VALUES (%s, %s, %s, %s)"""
            
            cur = mysql.connection.cursor()
            cur.execute(query1, (customerID, employeeID, transactionDate, transactionTime))
            
            # Get the last inserted transaction ID
            transactionID = cur.lastrowid
            
            query2 = """
            INSERT INTO Transactions_has_Products (transactionID, productID) 
            VALUES 
            """
            
            # transaction contains multiple products
            if len(product) > 1:
                product_query = []
                
                for productID in product:
                    product_query.append(f"({transactionID}, {productID})")
                 
                query2 += ', '.join(product_query)
        
            # new transaction contains one product
            else:
                productID = product[0]
                query2 += f"({transactionID}, {productID})"
                
            cur.execute(query2,)
                
            mysql.connection.commit()

            # redirect back to Transactions page
            return redirect("/transactions")

    if request.method == "GET":
        data = {}
        # mySQL query to grab all transactions
        query_trans = """
        SELECT Transactions.transactionID, 
            Transactions.customerID, 
            CONCAT(Customers.firstName, " ", Customers.lastName) AS Customer, 
            Transactions.employeeID, 
            CONCAT(Employees.firstName, " ", Employees.lastName) AS Employee, 
            Transactions.transactionDate,
            Transactions.transactionTime, 
            Products.productID, 
            price, 
            ProductDetails.productDetailsID, 
            type, 
            name 
        FROM Transactions
        INNER JOIN Transactions_has_Products
        ON Transactions.transactionID = Transactions_has_Products.transactionID
        INNER JOIN Products
        ON Transactions_has_Products.productID = Products.productID
        JOIN ProductDetails 
        ON Products.productDetailsID = ProductDetails.productDetailsID
        JOIN Customers
        ON Transactions.customerID = Customers.customerID
        JOIN Employees
        ON Transactions.employeeID = Employees.employeeID
        ;"""
        cur_trans = mysql.connection.cursor()
        cur_trans.execute(query_trans)
        data_trans = cur_trans.fetchall()
        
        # mySQL query to grab all customers for dynamic drop down
        query_cust = """
        SELECT customerID, firstName, lastName 
        FROM Customers
        ;"""
        cur_cust = mysql.connection.cursor()
        cur_cust.execute(query_cust)
        data_cust = cur_cust.fetchall()
        
        # mySQL query to grab all Employees for dynamic drop down
        query_emp = """
        SELECT employeeID, firstName, lastName 
        FROM Employees
        ;"""
        cur_emp = mysql.connection.cursor()
        cur_emp.execute(query_emp)
        data_emp = cur_emp.fetchall()
        
        # mySQL query to grab all Products for dynamic drop down
        query_prod = """
        SELECT * 
        FROM Products
        JOIN ProductDetails 
        ON Products.productDetailsID = ProductDetails.productDetailsID
        ;"""
        cur_prod = mysql.connection.cursor()
        cur_prod.execute(query_prod)
        data_prod = cur_prod.fetchall()

        
    
        data["transactions"] = data_trans
        data["customers"] = data_cust
        data["employees"] = data_emp
        data["products"] = data_prod       

    return render_template("transactions.html", data=data, header="Transactions", id_type="transactionID")

@app.route("/delete_transactions/<int:transactionID>")
def delete_transactions(transactionID):
    # mySQL query to delete the transaction with our passed transactionID
    query = "DELETE FROM Transactions_has_Products WHERE transactionID = '%s';"
    query2 = "DELETE FROM Transactions WHERE transactionID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (transactionID,))
    cur.execute(query2, (transactionID,))
    mysql.connection.commit()

    # redirect back to transactions page
    return redirect("/transactions")


# # Citation for the following code:
# Date: 06/09/2024
# Copied from: Stackoverflow: "How do I get time from a datetime.timedelta object?"
# Source URL: https://stackoverflow.com/questions/764184/how-do-i-get-time-from-a-datetime-timedelta-object
def convert_timedelta(data):
    for index in range(len(data)):
        value = data[index]["transactionTime"]
        data[index]["transactionTime"] = (datetime.datetime.min + value).time()
    return data
        
        

@app.route("/edit_transactions/<int:transactionID>", methods=["POST", "GET"])
def edit_transactions(transactionID):
    if request.method == "GET":
        # mySQL query to grab the info of the transactions with our passed transactionID
        query = """
        SELECT Transactions.transactionID, 
            Transactions.customerID, 
            CONCAT(Customers.firstName, ' ', Customers.lastName) AS Customer, 
            Transactions.employeeID, 
            CONCAT(Employees.firstName, ' ', Employees.lastName) AS Employee, 
            Transactions.transactionDate,
            Transactions.transactionTime, 
            Products.productID, 
            price, 
            ProductDetails.productDetailsID, 
            type, 
            name 
        FROM Transactions
        INNER JOIN Transactions_has_Products
        ON Transactions.transactionID = Transactions_has_Products.transactionID
        INNER JOIN Products
        ON Transactions_has_Products.productID = Products.productID
        JOIN ProductDetails 
        ON Products.productDetailsID = ProductDetails.productDetailsID
        JOIN Customers
        ON Transactions.customerID = Customers.customerID
        JOIN Employees
        ON Transactions.employeeID = Employees.employeeID
        WHERE Transactions.transactionID = '%s'
        ;"""
        cur = mysql.connection.cursor()
        cur.execute(query, (transactionID,))
        raw_data_trans = cur.fetchall()
        data_trans = convert_timedelta(raw_data_trans)

        # mySQL query to grab all customers for dynamic drop down
        query_cust = """
        SELECT customerID, firstName, lastName 
        FROM Customers
        ;"""
        cur_cust = mysql.connection.cursor()
        cur_cust.execute(query_cust)
        data_cust = cur_cust.fetchall()

        # mySQL query to grab all Employees for dynamic drop down
        query_emp = """
        SELECT employeeID, firstName, lastName 
        FROM Employees
        ;"""
        cur_emp = mysql.connection.cursor()
        cur_emp.execute(query_emp)
        data_emp = cur_emp.fetchall()

        # mySQL query to grab all Products for dynamic drop down
        query_prod = """
        SELECT * 
        FROM Products
        JOIN ProductDetails 
        ON Products.productDetailsID = ProductDetails.productDetailsID
        ;"""
        cur_prod = mysql.connection.cursor()
        cur_prod.execute(query_prod)
        data_prod = cur_prod.fetchall()

        data = {}
        data["transactions"] = data_trans
        data["customers"] = data_cust
        data["employees"] = data_emp
        data["products"] = data_prod

        return render_template("edit_transactions.html", data=data, header="Transactions", id_type="transactionID")
    
    if request.method == "POST":
        # fire off if user clicks the 'Edit Transaction' button
        if request.form.get("Edit_Transaction"):
        
            # grab user form inputs
            customerID = request.form["customer"]
            employeeID = request.form["employee"]
            transactionDate = request.form["transactionDate"]
            transactionTime = request.form["transactionTime"]

            # TRANSACTION QUERY
            query1 = """
            UPDATE Transactions 
            SET customerID = %s, employeeID = %s, transactionTime = %s, transactionDate = %s WHERE transactionID = %s """
            
            cur = mysql.connection.cursor()
            cur.execute(query1, (customerID, employeeID, transactionTime, transactionDate, transactionID))
            
            
            # TRANSACTION_HAS_PRODUCTS QUERY
            productList = request.form.getlist("product")

            
            # TODO MAKE THIS COMPATIBLE WITH MULTIPLE PRODUCT UPDATES
            update_all_query = "SELECT * FROM Transactions_has_Products WHERE transactionID = %s"
            cur = mysql.connection.cursor()
            # Execute the query with the parameters
            cur.execute(update_all_query, (transactionID,))
            sql_trans_prod = cur.fetchall()            
            
            
            data_trans_prod = list(sql_trans_prod)
            for productID in productList:
                # ({'transactions_has_productsID': 2, 'transactionID': 2, 'productID': 29},)
                if data_trans_prod:
                    current_thp = data_trans_prod.pop(0)
                else:
                    current_thp = None
                if current_thp: 
                    # update
                    # keep updating as long as returned list is equal
                    update_query = f'UPDATE Transactions_has_Products SET productID = {productID} WHERE transactionID = {current_thp["transactions_has_productsID"]}'
                    cur.execute(update_query,)
                else:
                    # INSERT
                    # no more products on database but more from the form
                    insert_thp = f"INSERT INTO Transactions_has_Products (transactionID, productID) VALUES ({transactionID}, {productID});"
                    cur.execute(insert_thp,)
            
            if len(data_trans_prod) > 0:
                for remaining in data_trans_prod:
                    delete_query = "DELETE FROM Transactions_has_Products WHERE transactions_has_productsID = '%s';"
                    cur.execute(delete_query, (remaining["transactions_has_productsID"],))
                    


            mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/transactions")
            # return(request.form)


# Citation for the following code:
# Date: 06/09/2024
# Copied From: Stackoverflow: "jinja2 print to console or logging"
# https://stackoverflow.com/questions/14783438/jinja2-print-to-console-or-logging
@app.context_processor
def utility_functions():
    def print_in_console(message):
        print(str(message))

    return dict(mdebug=print_in_console)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def cannot_complete(e):
    url = request.url.split('/')
    url_split = url[-2].split('_')
    who = url_split[1].capitalize()
    return render_template('cannot_complete.html', who=who, header=who)


# Listener

if __name__ == "__main__":
    app.run(port=51192)