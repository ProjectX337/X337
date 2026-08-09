def as_dict(self):
    return {
        "layout": self.layout,
        "theme": self.theme,
        "navigation": self.navigation,
        "metadata": self.metadata,

        "page_models": [
            p.as_dict()
            if hasattr(p, "as_dict")
            else {
                field: getattr(p, field)
                for field in p.__dataclass_fields__
            }
            for p in self.page_models
        ],

        "component_models": [
            c.as_dict()
            if hasattr(c, "as_dict")
            else {
                field: getattr(c, field)
                for field in c.__dataclass_fields__
            }
            for c in self.component_models
        ],

        "design_system": (
            self.design_system.as_dict()
            if hasattr(self.design_system, "as_dict")
            else {
                field: getattr(self.design_system, field)
                for field in self.design_system.__dataclass_fields__
            }
        ),
    }
