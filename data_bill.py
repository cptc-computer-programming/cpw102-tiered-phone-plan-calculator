"""Extend your phone bill lab with premium membership and tiered pricing."""

base_tolerance = 10
def exceeds_data_limit(data_used):
    return data_used > base_tolerance


def get_overage_rate(data_used, has_premium):
    if data_used <= 10:
        return 0
    elif data_used <= 20:
        if has_premium:
            return 1
        else:
            return 2
    else:
        if has_premium:
            return 2
        else:
            return 3

def main():
    user_gb = float(input("Enter GB used: "))
    user_base_plan = float(input("Enter Base Plan cost: "))

    premium = input("Do you have premium? (yes/no): ").strip().lower()
    has_premium = premium == "yes"

    overage_gb = max(0, user_gb - base_tolerance)
    base = user_base_plan
    rate = get_overage_rate(user_gb, has_premium)
    overage_cost = overage_gb * rate
    total_bill = base + overage_cost

    
    if not exceeds_data_limit(user_gb):
        print("You are within your data limit.")
        print(f"GB over limit: {overage_gb}")
        print(f"Overage cost: ${overage_cost}")
        print(f"Total bill: ${total_bill}")

    elif overage_gb <= 5:
        print(f"You are {overage_gb} GB over your limit.")
        print("Moderate extra usage.")
        print(f"Overage rate: ${rate} per GB")
        print(f"Overage cost: ${overage_cost}")
        print(f"Total bill: ${total_bill}")

    else:
        print(f"You are {overage_gb} GB over your limit.")
        print("High extra usage.")
        print(f"Overage rate: ${rate} per GB")
        print(f"Overage cost: ${overage_cost}")
        print(f"Total bill: ${total_bill}")
    if not has_premium and exceeds_data_limit(user_gb):
        print("Recommendation: Consider upgrading to Premium to reduce overage charges.")


# Keep this guard: importing functions for tests must not prompt for input.
if __name__ == "__main__":
    main()
