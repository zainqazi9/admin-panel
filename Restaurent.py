from flask import Flask , render_template

Web = Flask (__name__)

@Web.route("/login")
def login():
    return render_template("login.html")

@Web.route("/register")
def register():
    return render_template("register.html")

@Web.route("/forget")
def forget():
    return render_template("forgot-password.html")

@Web.route("/")
def index():
    return render_template("index.html")

@Web.route("/orders")
def orders():
    return render_template("Orders.html")

@Web.route("/new-order")
def order():
    return render_template("New-Order.html")

@Web.route("/products")
def products():
    return render_template("Products.html")

@Web.route("/add-products")
def product():
    return render_template("add-products.html")

@Web.route("/categories")
def categories():
    return render_template("Categories.html")

@Web.route("/add-categories")
def categorie():
    return render_template("add-categories.html")

@Web.route("/customers")
def customers():
    return render_template("Customers.html")

@Web.route("/add-customer")
def customer():
    return render_template("add-customers.html")

@Web.route("/staff")
def user():
    return render_template("staff.html")

@Web.route("/add-staff")
def adduser():
    return render_template("add-staff.html")

@Web.route("/stock-alerts")
def alerts():
    return render_template("Stock-Alerts.html")

@Web.route("/add-inventory")
def inventory():
    return render_template("add-inventory-item.html")

@Web.route("/modals")
def suppliers():
    return render_template("Suppliers.html")

@Web.route("/add-modals")
def supplier():
    return render_template("add-supplier.html")

@Web.route("/blank")
def reports():
    return render_template("Reports.html")

@Web.route("/profile")
def profile():
    return render_template("Profile.html")

@Web.route("/settings")
def setting():
    return render_template("setting.html")

Web.run(debug=True)