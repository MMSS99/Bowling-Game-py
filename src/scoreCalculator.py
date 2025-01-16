class ScoreCalculator():
    def __init__(self, annotation: str):
        self.annotation = annotation

    def calculateScore(self):
        return sum(self.__translateToInt())

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
    
    def __translateToInt(self):
        values = self.__framedValues()
        finalvalues = []
        for frame in values:
            frametotal = 0
            for roll in frame:
                if roll == 'X':
                    frametotal += 10
                elif roll == '-':
                    frame[frame.index(roll)] = 0
                    continue
                elif roll == '/':
                    frametotal += 10 - int(frame[frame.index('/')-1])
                else:
                    frametotal += int(roll)
            finalvalues.append(frametotal)
        
        print (finalvalues)
        return finalvalues





        
