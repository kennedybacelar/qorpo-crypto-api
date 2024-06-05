from flask import Blueprint, jsonify
from app.main.controller.price_controller import (
    get_price,
    get_price_history,
    delete_price_history,
)

price_bp = Blueprint("price", __name__)

@price_bp.route("/price/<currency>", methods=["GET"])
async def get_price_route(currency):
    price = await get_price(currency)
    return jsonify(price)

@price_bp.route("/price/history", methods=["GET"])
async def get_price_history_route():
    price_history = await get_price_history()
    return jsonify(price_history)

@price_bp.route("/price/history", methods=["DELETE"])
async def delete_price_history_route():
    result = await delete_price_history()
    return jsonify(result)