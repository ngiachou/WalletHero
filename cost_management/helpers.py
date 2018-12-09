import json
import datetime
import account as pb
import cost_types.base_type as pr
import transaction as tr


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


class PersonalBankEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, pb.PersonalBank):
            return {
                "balance": obj.balance,
                "history": [TransactionEncoder.default(self, t)
                            for t in obj.get_transaction_history()]
            }


if __name__ == "__main__":
    p = pr.Product("Beer", 2.5)

    json_string = json.dumps(p, cls=ProductEncoder, indent=2, sort_keys=True)

    print(json_string)

    p2 = pr.Product("Pizza", 9.0)
    t = tr.Transaction([p, p2], "friends", "in", datetime.date.today())

    json_string = json.dumps(t, cls=TransactionEncoder,
                             indent=2, sort_keys=True)

    print(json_string)

    personal_bank = pb.PersonalBank()
    personal_bank.add_transaction(t)

    json_string = json.dumps(personal_bank, cls=PersonalBankEncoder,
                             indent=2, sort_keys=True)
    print(json_string)
