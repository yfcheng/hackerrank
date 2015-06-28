import sys


class SimpleDatabase:
	def __init__(self):
		self.db = {}

	def processCommand(self, command):
		cmd = command.split(" ")
		cmdType = cmd[0]
		switch(cmdType):
			











if __name__ == "__main__":
    #db = Sider()
    line = sys.stdin.readline().strip()
    while line !=  "END":
        print line
        line = sys.stdin.readline().strip()
