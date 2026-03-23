class Rule:
    def __init__(self, name, category, severity, description):
        self.name = name
        self.category = category
        self.severity = severity
        self.description = description

    def evaluate(self, data):
        """
        Override this in each rule.
        Must return:
        - None if no issue
        - dict if triggered
        """
        raise NotImplementedError

    def build_flag(self, extra=None):
        return {
            "name": self.name,
            "category": self.category,
            "severity": self.severity,
            "description": self.description,
            "details": extra or {}
        }
