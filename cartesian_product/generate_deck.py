def generate_deck(properties):
    ret = []
    for property_, values in properties.items():
        to_add = []
        if len(ret) == 0:
            for value in values:
                card = {}
                card[property_] = value
                to_add.append(card)
        else:
            while len(ret) > 0:
                popped_card = ret.pop()
                for value in values:
                    card = popped_card.copy()
                    card[property_] = value
                    to_add.append(card)
        ret.extend(to_add)
    return ret
