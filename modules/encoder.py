import json
import datetime
import pprint
import PersonalBank as pb
import Product as pr
import Transaction as tr


class ProductEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, pr.Product):
            return {
                "name": obj.name,
                "price": obj.price
            }
        return json.JSONEncoder.default(self, obj)


class TransactionEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, tr.Transaction):
            return {
                "product list": [ProductEncoder.default(self, p)
                                 for p in obj.product_list],
                "environment characteristic": obj.environment_characteristic,
                "place": obj.place,
                "date": str(obj.date)
            }
        return json.JSONEncoder.default(self, obj)


if __name__ == "__main__":
    p = pr.Product("Beer", 2.5)
    json_string = json.dumps(p, cls=ProductEncoder)

    pprint.pprint(json.loads(json_string))

    p2 = pr.Product("Pizza", 9.0)
    t = tr.Transaction([p, p2], "friends", "in", datetime.date.today())
    json_string = json.dumps(t, cls=TransactionEncoder)

    pprint.pprint(json.loads(json_string))
