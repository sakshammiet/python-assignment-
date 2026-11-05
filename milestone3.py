"""
Milestone 3 - Model the Collection Using OOP
Assignment: COM-501
Model Institute of Engineering and Technology (Autonomous), Jammu
"""

class EWasteCollection:
    # a) Class variable shared across all instances
    centre_name = "GreenEarth Central E-Waste Facility"

    # Pre-defined catalogue matching Milestone 2
    CATALOGUE = {
        "Smartphone": {"unit_weight": 0.18, "rate": 40.0},
        "Laptop":     {"unit_weight": 2.20, "rate": 55.0},
        "Charger":    {"unit_weight": 0.12, "rate": 20.0},
        "Keyboard":   {"unit_weight": 0.65, "rate": 15.0}
    }

    # b) Constructor
    def __init__(self, collection_id: str, participant_name: str, items=None):
        self.collection_id = collection_id
        self.participant_name = participant_name
        # items stored as a list of dicts: [{"category": ..., "quantity": ...}]
        self.items = []
        if items:
            for item in items:
                self.add_item(item["category"], item["quantity"])

    # b) Instance method to add an item
    def add_item(self, category: str, quantity: int):
        cat_key = category.strip().title()
        if cat_key not in self.CATALOGUE:
            print(f"[REJECTED] Unknown category: '{category}'")
            return False
        if quantity <= 0:
            print(f"[REJECTED] Quantity must be > 0. Received: {quantity}")
            return False

        self.items.append({
            "category": cat_key,
            "quantity": quantity,
            "unit_weight": self.CATALOGUE[cat_key]["unit_weight"],
            "rate": self.CATALOGUE[cat_key]["rate"]
        })
        return True

    # c) Calculate total weight
    def total_weight(self) -> float:
        return sum(item["quantity"] * item["unit_weight"] for item in self.items)

    # c) Calculate total reward with Milestone 2 bonus rules
    def total_reward(self) -> float:
        base_reward = sum(item["quantity"] * item["unit_weight"] * item["rate"] for item in self.items)
        weight = self.total_weight()
        bonus = base_reward * 0.10 if weight >= 5.0 else 0.0
        return base_reward + bonus

    # Classification helper
    def get_classification(self) -> str:
        w = self.total_weight()
        if w < 3.0:
            return "SMALL (< 3 kg)"
        elif 3.0 <= w <= 8.0:
            return "MEDIUM (3 - 8 kg)"
        else:
            return "LARGE (> 8 kg)"

    # c) Display formatted summary
    def display_summary(self):
        w = self.total_weight()
        r = self.total_reward()
        device_count = len(self)
        classification = self.get_classification()

        print(f"\n========================================================")
        print(f"Recycling Facility : {EWasteCollection.centre_name}")
        print(f"Collection ID      : {self.collection_id}")
        print(f"Participant        : {self.participant_name}")
        print(f"Total Device Count : {device_count} unit(s) [via len()]")
        print(f"Total Weight       : {w:.3f} kg ({classification})")
        print(f"Total Reward       : Rs. {r:.2f}")
        print(f"Items Breakdown:")
        for it in self.items:
            sub_wt = it["quantity"] * it["unit_weight"]
            sub_cost = sub_wt * it["rate"]
            print(f"  * {it['category']}: {it['quantity']} unit(s) | Weight: {sub_wt:.2f} kg | Value: Rs. {sub_cost:.2f}")
        print(f"========================================================")

    # d) Special dunder method so len(collection) returns total number of discarded devices
    def __len__(self) -> int:
        return sum(item["quantity"] for item in self.items)


def main():
    print("=== Milestone 3: Object-Oriented E-Waste Collection ===")
    
    # e) Create two distinct objects with different items
    col1 = EWasteCollection("COL-101", "Aarav Sharma")
    col1.add_item("Smartphone", 2)
    col1.add_item("Charger", 3)

    col2 = EWasteCollection("COL-102", "Priya Verma")
    col2.add_item("Laptop", 3)
    col2.add_item("Keyboard", 4)
    col2.add_item("Smartphone", 1)

    # Display each summary and verify len()
    print("\n--- Testing Instance 1 ---")
    col1.display_summary()
    print(f"Demonstrating len(col1) -> {len(col1)} total devices collected.")

    print("\n--- Testing Instance 2 ---")
    col2.display_summary()
    print(f"Demonstrating len(col2) -> {len(col2)} total devices collected.")

    print("\n--- 3-4 Line Explanation of OOP Modeling ---")
    explanation = (
        "1. Encapsulation: The EWasteCollection class bundles collection attributes (ID, participant, items) and operational methods (calculating weight, reward, formatting summaries) within a unified entity.\n"
        "2. Class vs. Instance State: The class variable `centre_name` maintains global facility context, while individual instance variables track unique collection batches.\n"
        "3. Pythonic Dunder Integration: Implementing `__len__()` delegates standard Python protocol to the class, allowing `len(collection)` to intuitively return aggregate device count.\n"
        "4. Modular Reusability: Methods like `add_item()` guard against invalid input and keep data validation cohesive and reusable across different collection scenarios."
    )
    print(explanation)

if __name__ == "__main__":
    main()

