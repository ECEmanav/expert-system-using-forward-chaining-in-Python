class Rule:
    def __init__(self, conditions, result):
        self.conditions = conditions
        self.result = result

    def evaluate(self, facts):
        if all(cond in facts for cond in self.conditions):
            facts[self.result] = True


def forward_chaining(rules, initial_facts):
    facts = initial_facts.copy()
    while True:
        rule_applied = False
        for rule in rules:
            if rule.result not in facts:
                rule.evaluate(facts)
                rule_applied = True

        if not rule_applied:
            break

    return facts


# Example Rules
rule1 = Rule(["Rainy", "Traffic"], "Late")
rule2 = Rule(["Sunny"], "OnTime")
rule3 = Rule(["Late"], "Unhappy")

# Initial Facts
initial_facts = {"Rainy": True, "Traffic": True}

# Applying Forward Chaining
result_facts = forward_chaining([rule1, rule2, rule3], initial_facts)

# Displaying Results
print("Final Facts:", result_facts)
