from flask import Flask, jsonify, request

from custom_exception.bad_customer_name import BadCustomerName
from custom_exception.id_not_found import IdNotFound
from dal_layer.customer_dao_imp import CustomerDAOImp
from entities.customer import Customer
from service_layer.customer_services import customer_service_imp
from service_layer.customer_services.customer_service_imp import CustomerServiceImp

app: Flask = Flask(__name__)
customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)


@app.route("/greeting", methods=["GET"])
def hello_world():
   return "Hello world!"


# @app.route("/customer", methods=["POST"])
#
# def api_create_customer():
#     try:
#         customer_data: dict = request.get_json()
#         customer = Customer(customer_data["customerId"], customer_data["firstName"], customer_data["lastName"])
#         result = customer_service.service_create_customer(customer)
#         result_dictionary = result.convert_to_dictionary()
#         result_json = jsonify(result_dictionary)
#         return result_json, 201
#     except BadCustomerName as e:
#         message = {
#             "message": str(e)
#         }
#         return jsonify(message), 400
#     except IdNotFound as e:
#         message = {
#             "message": str(e)
#         }
#         return jsonify(message), 400

# @app.route("/deletecustomer/<customerId>", methods=["POST"])
#
# def api_delete_customer(customerId: str):
#     try:
#         result = customer_service_imp.service_delete_customer_by_id(customerId)
#         result_dictionary = {
#             "Message": "Customer deleted sucessfully"
#         }
#     result_json = jsonify(result_dictionary)
#     return result_json, 200
#     except InvalidDataType as exception:
#         message = {
#             "message": str(exception)
#         }
#         return jsonify(message), 400
#     except IdNotFound as exception:
#         message = {
#             "message": str(exception)
#         }
#         return jsonify(message), 400
#


app.run()