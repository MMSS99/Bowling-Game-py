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
        #print (framedAnnotation)
        return framedAnnotation
    
    def __framedValues(self):
        framedValues = []

        frames = self.__frameAnnotation()
        for frameIndex in range(len(frames)-1):
            frameValue = []

            if '/' in frames[frameIndex]:
                frameValue = frames[frameIndex] + list(frames[frameIndex+1][0])
                framedValues.append(frameValue)
                frameValue = []
            elif 'X' in frames[frameIndex]:
                try:
                    frameValue = frames[frameIndex] + list(frames[frameIndex+1][0]) + list(frames[frameIndex+1][1])
                except IndexError:
                    frameValue = frames[frameIndex] + list(frames[frameIndex+1][0]) + list(frames[frameIndex+2][0])
                finally:
                    framedValues.append(frameValue)
                    frameValue = []
            else:
                framedValues.append(frames[frameIndex])
        
        framedValues.append(frames[-1])
        #print(framedValues)
        return framedValues



        
