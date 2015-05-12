import unittest

def runLengthEncoding(input):
    if not input or len(input) == 0:
        return ""
    prev = ""
    out = ""
    count = 0
    for alpha in input:
    	alpha = str(alpha)
    	if len(prev) == 0:
    		prev = alpha
    		count = 1
       	elif prev == alpha:
    		count += 1
    	elif prev != alpha:
    		out += prev
    		out += str(count)
    		prev = alpha
    		count = 1
    out += prev
    out += str(count)
    return out

class MyTest(unittest.TestCase):
	def test(self):
		self.assertEqual(runLengthEncoding(None), "")
		self.assertEqual(runLengthEncoding(""), "")
		self.assertEqual(runLengthEncoding("bwwwwaaadexxxxxx"), "b1w4a3d1e1x6")

if __name__ == "__main__":
	unittest.main()
