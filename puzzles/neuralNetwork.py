###Neural Network
class Neuron:
    def  __init__(self, inp, thresh):
        self.inp = inp
        if(inp):
            self.thresh = thresh
        else:
            self.thresh = False
        self.hold = 0

    def setHold(self, hold):
        self.hold = hold

class Connection:
    def __init__(self, weight, start, end):
        self.weight = weight
        self.start = start
        self.end = end


class Network:
    def __init__(self, neuronList, connectList):
        self.neuronList = neuronList
        self.connectList = connectList
        self.inpList = self.start()

    def start(self):
        for i in self.connectList:
            startFound = False
            endFound = False
            for j in self.neuronList:
                if(j is i.start):
                    startFound = True
                if(j is i.end):
                    if(j.inp):
                        raise ValueError("A Input  neuron is an end connection. ")
                    endFound = True
            if(not(startFound) or not(endFound)):
                raise ValueError("A Connection doesn't have one of the neurons. ")

        final = []

        for i in self.neuronList:
            ###Add all the input neurons to a list
            if(i is b):
                print("YES")
            if(i.inp):
                final.append(i)
            
        for i in final:
            self.neuronList.remove(i)
        
        return final

    def go(self, inpDict):
        ###Make sure all the  inputs are given
        if(len(args) != len(self.inpList)):
            raise ValueError("Not enough arguments! ")
        ###Make sure all the input Neurons are real neurons
        for i in inpDict:
            if(not(i in self.inpList)):
                raise ValueError("A key is not in the input list!")

        ###Assign  each of them their starting value
        
        


