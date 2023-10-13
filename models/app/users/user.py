import sys
from pathlib import Path

base_dir = Path(__file__).parent.parent.parent
print(base_dir)
sys.path.append(str(base_dir))

from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from app import login_manager
from app.forms.register import RegistrationForm
from app.forms.login import LoginForm
from user_ import User
from cart import Cart
from cartItem import CartItem
from product import Product

user_bp = Blueprint('user', __name__,
                       template_folder='templates',
                       static_folder='static')

def get_user_carts(user_id):
    from __init__ import storage
    cart = storage.get_user_cart(user_id)
    storage.close()
    return cart
    
product_count = 0
@login_manager.user_loader
def load_user(id):
    from __init__ import storage
    #print(id)
    return storage.get('user', id=id)
    
@user_bp.route('/', strict_slashes=False)
def index():
    from engine.db_storage import DBStorage
    storage = DBStorage()
    products = storage.all('product', limit=8).values()
    categories = storage.all('category').values()
    brands = storage.all('brand').values()
    return render_template('index1.html', products=products, categories=categories, brands=brands)

@user_bp.route('/product/<string:id>', strict_slashes=False)
def products_details(id):
    from __init__ import storage
    products = storage.get('product', id=id)
    #print(products)
    return render_template('product_info.html', p=products)

@user_bp.route('/add_to_cart', methods=['POST'])
@login_required
def add_to_cart():
    from engine.db_storage import DBStorage
    storage = DBStorage()
    if current_user.is_authenticated:
        product_id = request.form['product_id']
        quantity = int(request.form['quantity'])
        print("product", product_id,  'quantity', quantity)

        user_id = current_user.id

        cart = storage.session.query(Cart).join(Cart.user).filter(User.id==user_id).first()
        storage.session.close()
        print('user id', user_id)
        print('cart', cart)

        # Do this if it's the first product added to a cart
        if cart is None:
            cart = Cart()
            cart.user_id = user_id
            cart.cart_id = cart.id  
            print('cart now: ', cart)
            product = storage.session.query(Product).get(product_id)
            cart_item = storage.session.query(CartItem).all()
            product.stock_quantity = quantity
            storage.session.add(product)
            storage.session.commit()
            storage.session.close()
            print('product:', product, 'cart_item: ', cart_item)

            if product:
                for c in cart_item:
                    if c.product_id == product_id and c.cart_id == cart.id:
                        response = {'exist': True, 'message': 'Items already exist!'}
                        return jsonify(response)
                    
                    
                cart_item = CartItem(product_id=product.id, cart_id=cart.id, quantity=quantity)
                cart_item.cart_item_id = cart_item.id
                print('cart_item', cart_item)
                cart.save()
                cart_item.save()
                response = {'success': True, 'message': 'successful'}
                return jsonify(response)

        # Do this if the user has a cart.  
        else:
            product = storage.session.query(Product).get(product_id)
            cart_item = storage.session.query(CartItem).all()
            product.stock_quantity = quantity
            storage.session.add(product)
            storage.session.commit()
            storage.session.close()
            print('product:', product, 'cart_item: ', cart_item)
            if product:
                for c in cart_item:
                    if c.product_id == product_id and c.cart_id == cart.id:
                        response = {'exist': True, 'message': 'Items already exist!'}
                        return jsonify(response)
                    
                cart_item = CartItem(product_id=product.id, cart_id=cart.id, quantity=quantity)
                cart_item.cart_item_id = cart_item.id
                print('cart_item', cart_item)
                cart.save()
                cart_item.save()
                response = {'success': True, 'message': 'successful'}
                return jsonify(response)       
 
# Categories route or process               
@user_bp.route('/categories/<string:id>', strict_slashes=False)
def categories(id):
    from __init__ import storage
    products = storage.get_category_product(id).values()
    category = storage.get('category', id=id)
    category_name = category.name
    #print('products: ', products, 'name: ', category_name)
    return render_template('shop_listing.html', products=products, name=category_name)

@user_bp.route('/brands/<string:id>', strict_slashes=False)
def brands(id):
    from __init__ import storage
    products = storage.get_brand_product(id).values()
    brand = storage.get('brand', id=id)
    brand_name = brand.name + ' PCs'
    print('products: ', products, 'brand_name: ', brand_name)
    return render_template('shop_listing.html', products=products, name=brand_name)

@user_bp.route('/contact', strict_slashes=False)
def contact_us():
    return render_template('contact.html')

# Update cart route or process
@user_bp.route('/update-cart-item', methods=['POST'])
@login_required
def update_cart_item():
    product_id = request.form.get('cart_item_id')
    new_quantity = request.form.get('new_quantity')

    print('product_id: ', product_id, 'new_quantity: ', new_quantity)

    # Update the cart item in your backend and return a response
    # You should implement the logic to update your models here

    response = {
        'message': 'Cart item updated successfully'
    }

    return jsonify(response)

# Delete cart route or process
@user_bp.route('/remove-cart-item', methods=['POST'])
@login_required
def remove_cart():
    from engine.db_storage import DBStorage
    storage = DBStorage()

    # Getting the product from an ajax request
    product_id = request.form.get('cart_item_id')

    print('product_id: ', product_id)
    # Update the cart item in your backend and return a response
    # You should implement the logic to update your models here
    user_id = current_user.id
    cart = storage.session.query(Cart).join(Cart.user).filter(User.id==user_id).first()

    cart_items = cart_item = storage.session.query(CartItem).all()         
    print('cart_items: ', cart_items)

    cart_item_id = ''

    for c in cart_items:
        if c.cart_id == cart.id and c.product_id == product_id:
            cart_item_id = c.id
            print(cart_item_id)
    cart_item = storage.session.query(CartItem).filter(CartItem.id == cart_item_id, CartItem.cart_id == cart.id).first()
    print('cart_item: ', cart_item)
    storage.session.delete(cart_item)
    storage.session.commit()
    storage.session.close()

    flash('Deleted successfully!')
    # Return a response message back to the ajax api 
    response = {'success': True, 'message': 'successful', 'redirect': url_for('user.cart')}

    return jsonify(response)

@user_bp.route('/cart', strict_slashes=False)
@login_required
def cart():
    from engine.db_storage import DBStorage
    storage = DBStorage()
    if not current_user.is_authenticated:
        # Capture the requested URL and save it in the session
        session['next_url'] = request.url
        flash('Please log in to access this page.')
        return redirect(url_for('user.login'))

    user_id = current_user.id
    cart = storage.session.query(Cart).join(Cart.user).filter(User.id==user_id).first()
    items = []
    storage.session.close()
    print('user id', user_id)
    print('cart', cart)

    cart_items = cart_item = storage.session.query(CartItem).all()         
    print('cart_items: ', cart_items)
    total_price = 0
    total_price_all = 0
    tax = 14
    discount = -12
    for c in cart_items:
        if c.cart_id == cart.id:
            cart_item = storage.session.query(CartItem).filter(CartItem.id == c.id, CartItem.cart_id == cart.id).first()
            product = storage.session.query(Product).join(Product.cart_items).filter(CartItem.id == cart_item.id).first()
            total_price += product.price
            items.append(product)

    total_price_all = total_price + 14 - 12
    print('items', total_price)
    product_count = len(items)
    return render_template('shopping_cart.html', products=items, total_price=total_price, discount=discount, tax=tax, total_price_all=total_price_all, count=product_count)

@user_bp.route("/register", methods=["GET", "POST"], strict_slashes=False)
def register():
    if current_user.is_authenticated:
        redirect(url_for("user.index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.name.data, email=form.email.data)
        user.set_password(password=form.password.data)
        user.save()
        flash(f"Welcome {form.name.data},Thank You for registering", "success")
        return redirect(url_for("user.login"))
    return render_template("register.html", form=form, title="Register")

@user_bp.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    from __init__ import storage
    if current_user.is_authenticated:
        return redirect(url_for('user.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = storage.get('user', email=form.email.data)
        print('user: ', user)
        if user is not None and user.check_password(form.password.data) == False: 
            flash('Invalid username or password')
            return redirect(url_for('user.login'))
        elif user and user.check_password(form.password.data): 
            login_user(user, remember=form.remember_me.data)
            next_page = session['next_url']  # Get the saved URL from the session
            return redirect(url_for('user.index') or next_page)  # Redirect to the saved URL or home page
        else:
            flash('Invalid username or password')
            return redirect(url_for('user.login'))
    return render_template('login.html', title='Sign In', form=form)

@user_bp.route('/logout', strict_slashes=False)
def logout():
    logout_user()
    return redirect(url_for('user.login'))
