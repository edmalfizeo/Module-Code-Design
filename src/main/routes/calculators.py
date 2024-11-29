from flask import Blueprint, request, jsonify
from src.calculators.calculator_1 import Calculator1

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    calculator = Calculator1()
    response = calculator.calculate(request)
    return jsonify({"success": True, "message": response}), 200
