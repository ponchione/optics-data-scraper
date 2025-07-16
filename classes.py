class Optic:
    def __init__(self, raw_desc, height, weight, manufacturer, name):
        self.raw_desc = raw_desc
        self.height = height
        self.weight = weight
        self.manufacturer = manufacturer
        self.name = name

class RedDotSight(Optic):
    def __init__(self, raw_desc, height, weight, manufacturer, name):
        super().__init__(raw_desc, height, weight, manufacturer, name)