from flask import Blueprint, request, jsonify
from src.main.factories.calculator_1_factory import calculator_1_factory
from src.main.factories.calculator_2_factory import calculator_2_factory
from src.main.factories.calculator_3_factory import calculator_3_factory

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    calculator = calculator_1_factory()
    response = calculator.calculate(request)
    return jsonify({"success": True, "message": response}), 200

@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
    calculator = calculator_2_factory()
    response = calculator.calculate(request)
    return jsonify({"success": True, "message": response}), 200

@calc_route_bp.route("/calculator/3", methods=["POST"])
def calculator_3():
    calculator = calculator_3_factory()
    response = calculator.calculate(request)
    return jsonify({"success": True, "message": response}), 200
