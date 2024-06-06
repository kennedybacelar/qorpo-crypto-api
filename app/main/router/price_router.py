from flask import Blueprint, current_app, jsonify, request

from app.main.controller.price_controller import delete_price_history, fetch_and_save_currency_price, get_price_history

price_bp = Blueprint("price", __name__)


@price_bp.route("/price/<currency>", methods=["GET"])
async def get_price_route(currency):
    saved_currency_bid_price = await fetch_and_save_currency_price(currency, current_app.db_session)
    return jsonify(saved_currency_bid_price)


@price_bp.route("/price/history", methods=["GET"])
async def get_price_history_route():
    page = request.args.get("page", 1, type=int)
    price_history = await get_price_history(current_app.db_session, page)
    return jsonify(price_history)


@price_bp.route("/price/history", methods=["DELETE"])
async def delete_price_history_route():
    return await delete_price_history(current_app.db_session)
