class ScoreCalculator():
    def __init__(self, annotation: str):
        self.annotation = annotation

    def calculateScore(self):
        return sum(self.__translateToInt())

    def __frameAnnotation(self):
        MAXFRAMEINDEX = 9
        MAXFRAMELENGTH = 2

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

                if len(frameRolls) == MAXFRAMELENGTH:
                    framedAnnotation.append(frameRolls)
                    frameRolls = []

            else:
                frameRolls.append(roll)

        framedAnnotation.append(frameRolls)
        return framedAnnotation
    
    def __framedValues(self):
        MAXFRAMEINDEX = 9

        framedValues = []

        frames = self.__frameAnnotation()
        frameIndex = 0
        #for frameIndex in range(len(frames)-1):
        while frameIndex < MAXFRAMEINDEX:
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

            frameIndex += 1
        
        framedValues.append(frames[-1])
        return framedValues
    
    def __translateToInt(self):
        MAXROLLSCORE = 10
        MISS = 0

        values = self.__framedValues()

        finalvalues = []
        for frame in values:
            frametotal = 0
            for roll in frame:
                if roll == 'X':
                    frametotal += MAXROLLSCORE
                elif roll == '-':
                    frame[frame.index(roll)] = MISS
                elif roll == '/':
                    frametotal += MAXROLLSCORE - int(frame[frame.index('/')-1])
                else:
                    frametotal += int(roll)
            finalvalues.append(frametotal)
        
        return finalvalues





        
