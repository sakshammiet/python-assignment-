"""
Milestone 1 - Estimate One E-Waste Collection
Assignment: COM-501
Model Institute of Engineering and Technology (Autonomous), Jammu
"""

def estimate_single_collection():
    print("=== Milestone 1: E-Waste Collection Estimator ===")
    
    # a) Input participant, device category, quantity, unit weight, recovery %, reward rate
    # Allowing command-line prompt or fallback to test defaults if needed
    participant_raw = input("Enter participant name: ") or "Aarav"
    device_raw = input("Enter device category: ") or "Smartphone"
    qty_raw = input("Enter quantity: ") or "3"
    unit_wt_raw = input("Enter unit weight in kg: ") or "0.18"
    recovery_raw = input("Enter recovery percentage (%): ") or "80"
    rate_raw = input("Enter reward rate per recyclable kg (Rs): ") or "40"

    # b) Convert numeric inputs to suitable types; display types of quantity and unit weight
    quantity = int(qty_raw)
    unit_weight = float(unit_wt_raw)
    recovery_pct = float(recovery_raw)
    reward_rate = float(rate_raw)

    print("\n--- Data Type Verification ---")
    print(f"Variable 'quantity' value: {quantity}, Type: {type(quantity)}")
    print(f"Variable 'unit_weight' value: {unit_weight}, Type: {type(unit_weight)}")

    # c) Calculate total weight, recyclable weight, and estimated reward using arithmetic operators
    total_weight = quantity * unit_weight
    recyclable_weight = total_weight * (recovery_pct / 100.0)
    estimated_reward = recyclable_weight * reward_rate

    # d) Format participant/device names and create a 5-character collection code
    # Formatting: trimmed, title-cased names
    participant_clean = participant_raw.strip().title()
    device_clean = device_raw.strip().title()

    # 5-character collection code: First 3 letters of participant + First 2 letters of device (all uppercase)
    part_slice = participant_clean[:3].upper().ljust(3, 'X')
    dev_slice = device_clean[:2].upper().ljust(2, 'X')
    collection_code = part_slice + dev_slice

    # e) Display labelled output
    print("\n================== COLLECTION SUMMARY ==================")
    print(f"Collection Code        : {collection_code}")
    print(f"Participant Name       : {participant_clean}")
    print(f"Device Category        : {device_clean}")
    print(f"Quantity Discarded     : {quantity} unit(s)")
    print(f"Unit Weight            : {unit_weight:.2f} kg")
    print(f"Total Weight           : {total_weight:.3f} kg")
    print(f"Recovery Percentage    : {recovery_pct:.1f}%")
    print(f"Recyclable Weight      : {recyclable_weight:.3f} kg")
    print(f"Reward Rate            : Rs. {reward_rate:.2f}/kg")
    print(f"Estimated Reward       : Rs. {estimated_reward:.2f}")
    print("========================================================")

if __name__ == "__main__":
    estimate_single_collection()

