def evaluate_business(data):
    flags = []

    # Revenue decline
    if data["this_week_sales"] < data["last_week_sales"] * 0.9:
        flags.append({
            "name": "Revenue Decline",
            "severity": 9
        })

    # Expense spike
    if data["expenses"] > data["avg_expenses"] * 1.2:
        flags.append({
            "name": "Expense Spike",
            "severity": 7
        })

    # Slow inventory
    if data["inventory_days"] > 45:
        flags.append({
            "name": "Slow Inventory",
            "severity": 6
        })

    # Owner bottleneck
    if data["owner_approvals_pct"] > 60:
        flags.append({
            "name": "Owner Bottleneck",
            "severity": 8
        })

    # Low incentive gap
    if (data["top_bonus"] - data["avg_bonus"]) < 10:
        flags.append({
            "name": "Low Incentive Gap",
            "severity": 6
        })

    return flags
