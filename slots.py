from rasa_core.slots import Slot

class BudgetSlot(Slot):

    def feature_dimensionality(self):
        return 2;

    def as_feature(self):
        r = [0.0] * self.feature_dimensionality()
        if self.value:
            if self.value > 700:
                r[1] = 1.0
            if self.value >= 300:
                r[0] = 1.0
        return r
    