from api.v1.routes import app_routes
from api.v1.models.orders import Order
#import api.v1.db

@app_routes.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
   # orders = db.session.query(Order).all()
    #print(orders)
    return "ok2"