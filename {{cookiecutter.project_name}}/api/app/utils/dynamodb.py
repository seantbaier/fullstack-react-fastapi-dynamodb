def format_items_response(response) -> dict:
    res = dict()
    if "Items" in response:
        res["data"] = response["Items"]

    if "Count" in response:
        res["count"] = response["Count"]

    return res


def format_item_response(response) -> dict:
    res = dict()
    if "Item" in response:
        res["data"] = response["Item"]

    return res
