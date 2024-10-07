# app.py
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Обновленный список товаров
products = [
    {
        'id': 1,
        'name': 'AFE23',
        'description': 'Аэрогриль с сенсорным управлением',
        'image_filename': 'img.png',  # Имя файла изображения
        'kaspi_url': 'https://kaspi.kz/shop/p/tovar-1',
    },
    {
        'id': 2,
        'name': 'AFM23',
        'description': 'Аэрогриль с механическим управлением',
        'image_filename': 'img_1.png',
        'kaspi_url': 'https://kaspi.kz/shop/p/tovar-2',
    },
    # Добавьте больше товаров по необходимости
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((item for item in products if item['id'] == product_id), None)
    if product:
        return render_template('product.html', product=product)
    else:
        return "Товар не найден", 404

@app.route('/buy/<int:product_id>')
def buy_product(product_id):
    product = next((item for item in products if item['id'] == product_id), None)
    if product:
        return redirect(product['kaspi_url'])
    else:
        return "Товар не найден", 404

if __name__ == '__main__':
    app.run(debug=True)

