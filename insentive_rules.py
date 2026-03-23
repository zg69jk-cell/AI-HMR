from base_rule import Rule


class LowIncentiveGapRule(Rule):
    def __init__(self):
        super().__init__(
            name="Low Incentive Gap",
            category="incentives",
            severity=6,
            description="Top performers are not sufficiently rewarded"
        )

    def evaluate(self, data):
        gap = data["top_bonus"] - data["avg_bonus"]

        if gap < 10:
            return self.build_flag({
                "gap": gap
            })


class UnrealisticTargetsRule(Rule):
    def __init__(self):
        super().__init__(
            name="Unrealistic Targets",
            category="incentives",
            severity=7,
            description="Too few employees are hitting targets"
        )

    def evaluate(self, data):
        if "pct_hitting_target" in data:
            if data["pct_hitting_target"] < 30:
                return self.build_flag({
                    "pct_hitting": data["pct_hitting_target"]
                })
