from chalice import Chalice
from chalicelib.apis.products import router

app = Chalice(app_name='chalice-sample')
app.register_blueprint(router)
