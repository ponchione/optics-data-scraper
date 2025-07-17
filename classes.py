class Optic:
    def __init__(self, name: str, height: str, weight: str, raw_desc: str, optic_type: str):
        self.name = name
        self.height = height
        self.weight = weight
        self.raw_desc = raw_desc
        self.optic_type = optic_type

    def __repr__(self):
        return f"Optic(name='{self.name}', type='{self.optic_type}')"