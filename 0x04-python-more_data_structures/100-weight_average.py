#!/usr/bin/python3

def weight_average(my_list=[]):
    """returns the weighted average of a list of tuples"""
    product_sum = 0
    weight_sum = 0
    product_list = list(map(lambda x: x[0] * x[1], my_list))
    weight_list = list(map(lambda x: x[1], my_list))
    for product in prod_list:
        product_sum += i
    for weight in weight_list:
        weight_sum += s
    average = product_sum / weight_sum
    return average
