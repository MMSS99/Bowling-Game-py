class ScoreCalculator():
    def __init__(self, annotation: str):
        self.bowlingcard= []

        currentthrow = 1
        while currentthrow <= len(annotation):
