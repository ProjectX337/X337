from core.capabilities.capability_loader import CapabilityLoader

loader = CapabilityLoader()

for capability in loader.load():
    print(capability)
