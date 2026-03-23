from base_rule import Rule


class RevenueDeclineRule(Rule):
    def __init__(self):
        super().__init__(
            name="Revenue Decline",
            category="cashflow",
            severity=9,
            description="Revenue dropped significantly week-over-week"
        )

    def evaluate(self, data):
        if data["this_week_sales"] < data["last_week_sales"] * 0.9:
            change = (
                (data["this_week_sales"] - data["last_week_sales"])
                / data["last_week_sales"]
            ) * 100

            return self.build_flag({
                "percent_change": round(change, 2)
            })


class ExpenseSpikeRule(Rule):
    def __init__(self):
        super().__init__(
            name="Expense Spike",
            category="cashflow",
            severity=7,
            description="Expenses increased beyond normal levels"
        )

    def evaluate(self, data):
        if data["expenses"] > data["avg_expenses"] * 1.2:
            return self.build_flag({
                "expenses": data["expenses"],
                "avg": data["avg_expenses"]
            })


class SlowInventoryRule(Rule):
    def __init__(self):
        super().__init__(
            name="Slow Inventory",
            category="cashflow",
            severity=6,
            description="Inventory is not converting to cash fast enough"
        )

    def evaluate(self, data):
        if data["inventory_days"] > 45:
            return self.build_flag({
                "inventory_days": data["inventory_days"]
            })
