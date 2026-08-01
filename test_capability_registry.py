from core.capabilities.capability_registry import CapabilityRegistry

registry = CapabilityRegistry()

print("Capability Names:")
print(registry.names())

print()

print("Keyword Lookup:")
print(registry.find_by_keyword("login"))

print()

print("JWT Lookup:")
print(registry.find_by_keyword("jwt"))

print()

print("Keyword Index:")
print(registry.keyword_index())
