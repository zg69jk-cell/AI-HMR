from base_rule import Rule


class OwnerBottleneckRule(Rule):
    def __init__(self):
        super().__init__(
            name="Owner Bottleneck",
            category="operations",
            severity=8,
            description="Owner is involved in too many decisions"
        )

    def evaluate(self, data):
        if data["owner_approvals_pct"] > 60:
            return self.build_flag({
                "approval_pct": data["owner_approvals_pct"]
            })


class OwnerDependencySalesRule(Rule):
    def __init__(self):
        super().__init__(
            name="Owner Dependency Risk",
            category="operations",
            severity=8,
            description="Sales depend heavily on owner presence"
        )

    def evaluate(self, data):
        if "sales_with_owner" in data and "sales_without_owner" in data:
            if data["sales_without_owner"] < data["sales_with_owner"] * 0.8:
                return self.build_flag({
                    "with_owner": data["sales_with_owner"],
                    "without_owner": data["sales_without_owner"]
                })
