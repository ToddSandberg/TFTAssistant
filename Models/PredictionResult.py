class PredictionResult:
    def __init__(self, champion_name, probability, reason):
        self.champion_name = champion_name
        self.probability = probability
        self.reason = reason
