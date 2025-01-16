class ScoreCalculator():
    def __init__(self, annotation: str):
        self.annotation = annotation

    def calculateScore(self):
        pass

    def __frameAnnotation(self):
        MAXFRAMEINDEX = 9
        framedAnnotation = []

        frameRolls = []
        for roll in self.annotation:
            if len(framedAnnotation) < MAXFRAMEINDEX:    
                if roll != 'X':
                    frameRolls.append(roll)
                else:
                    frameRolls.append(roll)
                    framedAnnotation.append(frameRolls)
                    frameRolls = []

                if len(frameRolls) == 2:
                    framedAnnotation.append(frameRolls)
                    frameRolls = []

            else:
                frameRolls.append(roll)

        framedAnnotation.append(frameRolls)
        print (framedAnnotation)
        return framedAnnotation


        
