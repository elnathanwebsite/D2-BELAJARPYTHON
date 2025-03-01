from flask import Flask, request, jsonify
from flask_cors import CORS  # Tambahkan ini agar frontend bisa mengakses backend

app = Flask(__name__)
CORS(app)  # Izinkan akses dari frontend

# Simpan data produk dalam list sebagai database sementara
products = []

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    if not all(key in data for key in ["name", "price", "description"]):
        return jsonify({"error": "Missing fields"}), 400

    products.append({
        "name": data["name"],
        "price": data["price"],
        "description": data["description"]
    })
    return jsonify({"message": "Product added successfully"}), 201

@app.route('/get_products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
