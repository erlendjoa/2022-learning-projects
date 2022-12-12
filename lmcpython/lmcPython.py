

class LittleManComputer():
    def __init__(self):
        self._ram = {}
        for i in range(100):
            self._ram[i] = 000
        
        self._accumulator = 0
        self._output = ""
        self._commandList = []


    def addInstructions(self):
        addCommand = input("Add LMC Code (space between each instruction): ")
        for command in addCommand.split(" "):
            self._commandList.append(int(command))
        self.assembleToRam()


    def assembleToRam(self):
        for xxx in self._commandList:
            for counter in self._ram:
                if self._ram[counter] == 000:
                    self._ram[counter] = xxx
                    break


    def runProgram(self):
        for counter in self._ram:
            if self._ram[counter] != 000:
                self.instructions(self._ram[counter])
            else:
                break
        print(self._output)
    

    def instructions(self, xxx):
        if xxx == 901:
            self._accumulator = int(input("INPUT: "))
        elif xxx == 902:
            self._output += f"\n{self._accumulator}"
        elif str(xxx)[0] == "1":
            self._accumulator += self._ram[xxx-100]
        elif str(xxx)[0] == "2":
            self._accumulator -= self._ram[xxx-200]
        elif str(xxx)[0] == "3":
            copyList = [self._accumulator]
            self._ram[xxx-300] = copyList.copy()[0]
        elif str(xxx)[0] == "5":
            self._accumulator = self._ram[xxx-500]



lmc = LittleManComputer()
lmc.addInstructions()
lmc.runProgram()
