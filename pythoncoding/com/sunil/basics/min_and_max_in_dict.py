class MinAndMaxInDict:
    def __init__(self):
        return


if __name__ == '__main__':
    veg_prices = {'tomato': 1.99, 'potato': 2.99, 'brinjal': 0.99, 'carrot': 5.99, 'mint': 1.49}
    min = 0.00
    max = 1000.00

    for key in veg_prices:
        if veg_prices[key] > min:
            max_price = veg_prices[key]
            min = max_price

        if veg_prices[key] < max:
            min_price = veg_prices[key]
            max = min_price

    print(f'Max prices is {max_price}')
    print(f'Min price is {min_price}')
