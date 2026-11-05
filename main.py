"""
main.py - Driver program for Milestone 4
Assignment: COM-501
Model Institute of Engineering and Technology (Autonomous), Jammu
"""

import recycling_utils

def run_analytics_demo():
    print("=== Milestone 4: Modularized Recycling Analytics ===")

    # Standard Catalogue
    catalogue = {
        "Smartphone": {"unit_weight": 0.18, "rate": 40.0},
        "Laptop":     {"unit_weight": 2.20, "rate": 55.0},
        "Charger":    {"unit_weight": 0.12, "rate": 20.0},
        "Keyboard":   {"unit_weight": 0.65, "rate": 15.0}
    }

    # Sample mixed collection
    items = [
        {"category": "Smartphone", "quantity": 4},   # 4 * 0.18 = 0.72 kg
        {"category": "Laptop", "quantity": 2},       # 2 * 2.20 = 4.40 kg
        {"category": "Keyboard", "quantity": 3},     # 3 * 0.65 = 1.95 kg
        {"category": "Charger", "quantity": 5}       # 5 * 0.12 = 0.60 kg
    ]

    print("\n--- Input Mixed Items ---")
    for idx, item in enumerate(items, 1):
        print(f"{idx}. {item['category']} x {item['quantity']}")

    # c) Function as argument: generate_metric passing total_weight
    metric_wt = recycling_utils.generate_metric(items, catalogue, recycling_utils.total_weight)
    print(f"\n[Higher-Order Function] generate_metric(..., total_weight) -> {metric_wt:.3f} kg")

    # b) Default parameters demonstration
    default_reward = recycling_utils.reward(items, catalogue)
    print(f"[Default Parameters] reward(items, catalogue) [default 10% bonus at >= 5kg] -> Rs. {default_reward:.2f}")

    # Keyword parameters demonstration
    custom_reward = recycling_utils.reward(items, catalogue, bonus_rate=0.15, threshold_kg=6.0)
    print(f"[Keyword Parameters] reward(..., bonus_rate=0.15, threshold_kg=6.0) -> Rs. {custom_reward:.2f}")

    # d) bins_required using math.ceil()
    bins_standard = recycling_utils.bins_required(metric_wt, capacity_kg=5.0)
    print(f"[math.ceil()] bins_required({metric_wt:.3f} kg, capacity=5.0 kg) -> {bins_standard} bin(s)")

    bins_small = recycling_utils.bins_required(metric_wt, capacity_kg=2.5)
    print(f"[math.ceil()] bins_required({metric_wt:.3f} kg, capacity=2.5 kg) -> {bins_small} bin(s)")

    # Complete collection summary
    print("\n==================== ANALYTICS REPORT ====================")
    print(f"Total Discarded Devices : {sum(i['quantity'] for i in items)}")
    print(f"Aggregated Total Weight : {metric_wt:.3f} kg")
    print(f"Calculated Reward       : Rs. {default_reward:.2f}")
    print(f"Standard 5-kg Bins Req. : {bins_standard} bin(s)")
    print("==========================================================")

if __name__ == "__main__":
    run_analytics_demo()

