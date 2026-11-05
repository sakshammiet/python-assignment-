"""
Milestone 5 - Store History and Handle Errors
Assignment: COM-501
Model Institute of Engineering and Technology (Autonomous), Jammu
"""

import os
from datetime import datetime

RECORDS_FILE = "recycling_records.txt"

CATALOGUE = {
    "Smartphone": {"unit_weight": 0.18, "rate": 40.0},
    "Laptop":     {"unit_weight": 2.20, "rate": 55.0},
    "Charger":    {"unit_weight": 0.12, "rate": 20.0},
    "Keyboard":   {"unit_weight": 0.65, "rate": 15.0}
}


def append_record(collection_id: str, participant: str, device_count: int, total_weight: float, reward: float):
    """Appends completed collection summary to recycling_records.txt using '|' as delimiter."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record_line = f"{collection_id}|{participant}|{device_count}|{total_weight:.3f}|{reward:.2f}|{timestamp}\n"
    with open(RECORDS_FILE, "a", encoding="utf-8") as f:
        f.write(record_line)
    print(f"[FILE I/O] Record saved to '{RECORDS_FILE}' successfully.")


def read_history(filename: str = RECORDS_FILE):
    """
    Reads and displays previously saved records from the file.
    Handles FileNotFoundError when the file is not found.
    """
    print(f"\n--- Reading History from '{filename}' ---")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("The records file is empty.")
                return

            print(f"{'Col ID':<10} | {'Participant':<16} | {'Devices':<8} | {'Weight (kg)':<12} | {'Reward (Rs)':<12} | {'Timestamp':<19}")
            print("-" * 88)
            for line in lines:
                parts = line.strip().split("|")
                if len(parts) >= 6:
                    cid, part, count, wt, rew, tstamp = parts[:6]
                    print(f"{cid:<10} | {part:<16} | {count:<8} | {wt:<12} | {rew:<12} | {tstamp:<19}")
    except FileNotFoundError:
        print(f"[CAUGHT FileNotFoundError] Warning: The file '{filename}' does not exist yet. Please record a collection first.")


def parse_and_add_item(category_input: str, quantity_input: str, items_list: list):
    """
    Validates and adds an item using separate except blocks for ValueError and KeyError.
    """
    try:
        # Category lookup in CATALOGUE (exact or capitalized lookup)
        # We explicitly trigger KeyError if unsupported
        matched_cat = None
        for cat in CATALOGUE:
            if cat.lower() == category_input.strip().lower():
                matched_cat = cat
                break
        
        if not matched_cat:
            raise KeyError(f"Unsupported device category: '{category_input}'")

        # Parse quantity, may raise ValueError
        qty = int(quantity_input.strip())
        if qty <= 0:
            raise ValueError(f"Quantity must be a positive integer (> 0). Got: {qty}")

        # Add valid item
        items_list.append({"category": matched_cat, "quantity": qty})
        print(f"[SUCCESS] Added: {qty} x {matched_cat}")

    except KeyError as ke:
        print(f"[CAUGHT KeyError] Invalid Category Error: {ke}")
    except ValueError as ve:
        print(f"[CAUGHT ValueError] Invalid Quantity Error: {ve}")


def run_debugging_demonstration():
    """
    Milestone 5 (e):
    Debug: quantity = input("Quantity: ") followed by total_weight = quantity * unit_weight.
    Explain the type problem, correct the conversion, and show the output.
    """
    print("\n" + "=" * 30 + " DEBUGGING DEMONSTRATION " + "=" * 30)
    print("Code Snippet under investigation:")
    print('  quantity = input("Quantity: ")')
    print('  total_weight = quantity * unit_weight')

    unit_weight = 0.18
    raw_qty_input = "5" # Simulating user entering 5

    print(f"\n1. Demonstrating the Type Problem:")
    quantity_str = raw_qty_input
    print(f"   input() returns value: '{quantity_str}' with type: {type(quantity_str)}")
    
    # In Python, str * float causes TypeError
    try:
        buggy_result = quantity_str * unit_weight
    except TypeError as te:
        print(f"   [BUG TRIGGERED] TypeError caught: {te}")
        print("   Explanation: In Python, string cannot be multiplied with a floating-point number (str * float).")
        print("   Furthermore, if multiplied by an integer (str * int), it causes string repetition ('5'*3 = '555') instead of arithmetic multiplication!")

    print("\n2. Corrected Conversion and Execution:")
    print("   Corrected Code:")
    print('     quantity = int(input("Quantity: "))')
    print('     total_weight = quantity * unit_weight')

    corrected_quantity = int(quantity_str)
    corrected_total_weight = corrected_quantity * unit_weight
    print(f"   Converted quantity: {corrected_quantity} (type: {type(corrected_quantity)})")
    print(f"   Calculated total_weight: {corrected_total_weight:.3f} kg (type: {type(corrected_total_weight)})")
    print("=" * 85)


def run_collection_workflow(collection_id: str, participant: str, raw_items_input: list):
    """Executes a full collection run with validation and persistence."""
    print(f"\nProcessing Collection {collection_id} for {participant}...")
    items = []
    for cat_in, qty_in in raw_items_input:
        parse_and_add_item(cat_in, qty_in, items)

    if not items:
        print("No valid items collected. Nothing to record.")
        return

    # Calculate weight and reward
    total_wt = sum(it["quantity"] * CATALOGUE[it["category"]]["unit_weight"] for it in items)
    base_reward = sum(it["quantity"] * CATALOGUE[it["category"]]["unit_weight"] * CATALOGUE[it["category"]]["rate"] for it in items)
    bonus = (base_reward * 0.10) if total_wt >= 5.0 else 0.0
    total_reward = base_reward + bonus
    total_devices = sum(it["quantity"] for it in items)

    append_record(collection_id, participant, total_devices, total_wt, total_reward)


def main():
    print("=== Milestone 5: File I/O, Exception Handling & Debugging ===")

    # 1. Test FileNotFoundError handling with a non-existent file
    print("\n>>> TEST 1: Handling FileNotFoundError <<<")
    read_history("non_existent_records_file.txt")

    # 2. Test Error Handling for ValueError and KeyError
    print("\n>>> TEST 2: Handling KeyError & ValueError <<<")
    test_error_inputs = [
        ("Tablet", "3"),          # Unsupported category -> KeyError
        ("Smartphone", "abc"),    # Non-numeric quantity -> ValueError
        ("Laptop", "-4"),         # Negative quantity -> ValueError
        ("SmartWatch", "2")       # Unsupported category -> KeyError
    ]
    temp_items = []
    for cat, qty in test_error_inputs:
        print(f"\nAttempting input: Category='{cat}', Qty='{qty}'")
        parse_and_add_item(cat, qty, temp_items)

    # 3. Test Normal Run & File Append
    print("\n>>> TEST 3: Normal Collection Run & Append to File <<<")
    normal_items = [
        ("Smartphone", "5"),  # 5 * 0.18 = 0.90 kg
        ("Laptop", "2"),      # 2 * 2.20 = 4.40 kg
        ("Keyboard", "1")     # 1 * 0.65 = 0.65 kg -> Total = 5.95 kg (bonus applied)
    ]
    run_collection_workflow("COL-201", "Rohan Gupta", normal_items)

    normal_items_2 = [
        ("Charger", "4"),     # 4 * 0.12 = 0.48 kg
        ("Smartphone", "2")   # 2 * 0.18 = 0.36 kg -> Total = 0.84 kg
    ]
    run_collection_workflow("COL-202", "Ananya Sharma", normal_items_2)

    # 4. Read and display history
    print("\n>>> TEST 4: Reading and Displaying Saved History File <<<")
    read_history(RECORDS_FILE)

    # 5. Debugging Note & Execution
    run_debugging_demonstration()


if __name__ == "__main__":
    main()

