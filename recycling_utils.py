"""
recycling_utils.py - Modularized Recycling Analytics Functions
Assignment: COM-501
Model Institute of Engineering and Technology (Autonomous), Jammu
"""

import math

def total_weight(items: list, catalogue: dict) -> float:
    """Calculates total weight of collected items in kilograms."""
    return sum(item["quantity"] * catalogue[item["category"]]["unit_weight"] for item in items)


def reward(items: list, catalogue: dict, bonus_rate: float = 0.10, threshold_kg: float = 5.0) -> float:
    """
    Computes total reward with default/keyword parameters for bonus rate and threshold weight.
    """
    base_reward = sum(
        item["quantity"] * catalogue[item["category"]]["unit_weight"] * catalogue[item["category"]]["rate"]
        for item in items
    )
    weight = total_weight(items, catalogue)
    bonus = (base_reward * bonus_rate) if weight >= threshold_kg else 0.0
    return base_reward + bonus


def bins_required(weight: float, capacity_kg: float = 5.0) -> int:
    """
    Estimates the number of recycling bins needed using math.ceil().
    """
    if weight <= 0:
        return 0
    return math.ceil(weight / capacity_kg)


def generate_metric(items: list, catalogue: dict, metric_function) -> float:
    """
    Higher-order function: accepts a function as an argument and executes it over items and catalogue.
    """
    return metric_function(items, catalogue)

