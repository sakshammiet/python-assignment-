"""
Milestone 2 - Process a Mixed E-Waste Collection
Assignment: COM-501
Model Institute of Engineering and Technology (Autonomous), Jammu
"""

def process_mixed_collection():
    print("=== Milestone 2: Mixed E-Waste Collection Processor ===")
    
    # a) Catalogue setup: Category -> (unit_weight_kg, rate_per_kg)
    catalogue = {
        "Smartphone": {"unit_weight": 0.18, "rate": 40.0},
        "Laptop":     {"unit_weight": 2.20, "rate": 55.0},
        "Charger":    {"unit_weight": 0.12, "rate": 20.0},
        "Keyboard":   {"unit_weight": 0.65, "rate": 15.0}
    }

    print("\nAvailable E-Waste Catalogue:")
    for item, details in catalogue.items():
        print(f" - {item}: {details['unit_weight']} kg/unit @ Rs. {details['rate']}/kg")
    print("Type 'DONE' at the category prompt to finish.\n")

    # c) Store valid selections in a suitable collection and maintain unique categories set
    valid_items = []
    unique_categories = set()

    # b) & d) Repeatedly accept input until DONE; reject unsupported or qty <= 0
    while True:
        category_input = input("Enter device category (or 'DONE'): ").strip()
        if category_input.upper() == "DONE":
            break

        # Standardize capitalization (e.g. smartphone -> Smartphone)
        matched_category = None
        for cat in catalogue:
            if cat.lower() == category_input.lower():
                matched_category = cat
                break

        if not matched_category:
            print(f"[REJECTED] Error: '{category_input}' is not an accepted category in the catalogue. Please try again.\n")
            continue

        qty_input = input(f"Enter quantity for {matched_category}: ").strip()
        try:
            quantity = int(qty_input)
            if quantity <= 0:
                print(f"[REJECTED] Error: Quantity must be a positive integer (> 0). Received: {quantity}. Please try again.\n")
                continue
        except ValueError:
            print(f"[REJECTED] Error: Invalid numeric input '{qty_input}' for quantity. Please try again.\n")
            continue

        # Valid selection
        valid_items.append({
            "category": matched_category,
            "quantity": quantity,
            "unit_weight": catalogue[matched_category]["unit_weight"],
            "rate": catalogue[matched_category]["rate"]
        })
        unique_categories.add(matched_category)
        print(f"[ACCEPTED] Added {quantity} x {matched_category}.\n")

    if not valid_items:
        print("No items recorded in this collection session.")
        return

    # e) Compute total weight and reward; apply 10% bonus if total weight >= 5 kg
    total_weight = sum(item["quantity"] * item["unit_weight"] for item in valid_items)
    base_reward = sum(item["quantity"] * item["unit_weight"] * item["rate"] for item in valid_items)

    bonus_applied = False
    bonus_amount = 0.0
    if total_weight >= 5.0:
        bonus_applied = True
        bonus_amount = base_reward * 0.10
    total_reward = base_reward + bonus_amount

    # Classify as SMALL (<3 kg), MEDIUM (3-8 kg), or LARGE (>8 kg)
    if total_weight < 3.0:
        classification = "SMALL (< 3 kg)"
    elif 3.0 <= total_weight <= 8.0:
        classification = "MEDIUM (3 - 8 kg)"
    else:
        classification = "LARGE (> 8 kg)"

    # Mixed-collection summary
    print("\n======================= MIXED COLLECTION SUMMARY =======================")
    print(f"{'Category':<15} | {'Quantity':<8} | {'Unit Wt (kg)':<14} | {'Total Wt (kg)':<14} | {'Subtotal (Rs)':<12}")
    print("-" * 72)
    for item in valid_items:
        sub_wt = item["quantity"] * item["unit_weight"]
        sub_rew = sub_wt * item["rate"]
        print(f"{item['category']:<15} | {item['quantity']:<8} | {item['unit_weight']:<14.2f} | {sub_wt:<14.3f} | Rs. {sub_rew:<9.2f}")
    
    print("-" * 72)
    print(f"Total Unique Categories Count : {len(unique_categories)} ({', '.join(sorted(unique_categories))})")
    print(f"Total Discarded Devices Count : {sum(item['quantity'] for item in valid_items)}")
    print(f"Cumulative Collection Weight  : {total_weight:.3f} kg")
    print(f"Collection Weight Class       : {classification}")
    print(f"Base Reward                   : Rs. {base_reward:.2f}")
    if bonus_applied:
        print(f"Volume Bonus (10% at >= 5 kg) : Rs. {bonus_amount:.2f}")
    else:
        print(f"Volume Bonus (10% at >= 5 kg) : Rs. 0.00 (Weight under 5 kg threshold)")
    print(f"Final Total Reward Payable    : Rs. {total_reward:.2f}")
    print("========================================================================")

if __name__ == "__main__":
    process_mixed_collection()

