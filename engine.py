from cashflow_rules import (
    RevenueDeclineRule,
    ExpenseSpikeRule,
    SlowInventoryRule
)

from operations_rules import (
    OwnerBottleneckRule,
    OwnerDependencySalesRule
)

from incentive_rules import (
    LowIncentiveGapRule,
    UnrealisticTargetsRule
)


class RuleEngine:
    def __init__(self):
        self.rules = [
            # Cashflow
            RevenueDeclineRule(),
            ExpenseSpikeRule(),
            SlowInventoryRule(),

            # Operations
            OwnerBottleneckRule(),
            OwnerDependencySalesRule(),

            # Incentives
            LowIncentiveGapRule(),
            UnrealisticTargetsRule()
        ]

    def evaluate(self, data):
        results = []

        for rule in self.rules:
            try:
                result = rule.evaluate(data)
                if result:
                    results.append(result)
            except Exception as e:
                print(f"Error in rule {rule.name}: {e}")

        # Sort by severity
        results.sort(key=lambda x: x["severity"], reverse=True)

        return results
