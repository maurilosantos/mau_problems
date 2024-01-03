"""
Exerc 1 Lasagna Cooking Module

This module provides functions to calculate various aspects of lasagna cooking.
It includes functions for determining the remaining baking time, preparation time,
and the total elapsed time for cooking a delicious lasagna.
"""
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(expec):
    """Calculate the remaining baking time.

    :param expec: int - elapsed baking time.
    :return: int - remaining baking time.
    """
    rest = EXPECTED_BAKE_TIME - expec
    return rest

def preparation_time_in_minutes(layers):
    """Calculate the preparation time in minutes.

    :param layers: int - number of layers in the lasagna.
    :return: int - total preparation time in minutes.
    """
    time = layers * 2
    return time

def elapsed_time_in_minutes(layers, total):
    """Calculate the total cooking time in minutes.

    :param layers: int - number of layers in the lasagna.
    :param total: int - elapsed baking time.
    :return: int - total cooking time in minutes.
    """
    total_time = preparation_time_in_minutes(layers) + bake_time_remaining(EXPECTED_BAKE_TIME - total)
    return total_time