class FirewallRule:
    def apply_rule(self):
        return "Applying generic rule."

class IPBlockRule(FirewallRule):
    def apply_rule(self):
        return "Block IP Address."

class PortBlockRule(FirewallRule):
    def apply_rule(self):
        return "Block port number."

#Polymorphism function
def firewall_action(rule):
    print(f"Firewall Action: {rule.apply_rule()}")
    
f = FirewallRule()
i = IPBlockRule()
p = PortBlockRule()

#polymorphism use
firewall_action(f)
firewall_action(i)
firewall_action(p)