from api.v1.routes import app_routes
from api.v1.models.orders import Order

@app_routes.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """

    orders = Order.query.all()
    # print(orders)
    print("HOLA HP")
    return "ok2"