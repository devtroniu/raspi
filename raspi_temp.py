class CPUTemp:
	def __init__(self, tempfilename = "/sys/class/thermal/thermal_zone0/temp"):
		self.tempfilename = tempfilename

	def __enter__(self):
		self.open()
		return self

	def open(self):
		self.tempfile = open(self.tempfilename, "r")
		
	def read(self):
		self.tempfile.seek(0)
		return self.tempfile.read().rstrip()
		
	def get_temp(self):
		return self.get_temp_in_c()
		
	def get_temp_in_c(self):
		tempraw = self.read()
		return float(tempraw[:-3] + "." + tempraw[-3:])
		
	def get_temp_in_f(self):
		return self.convert_c_to_f(self.get_temp_in_c())
		
	def convert_c_to_f(self, c):
		return c * 9.0 / 5.0 + 32.0
		
	def __exit__(self, type, value, traceback):
		self.close()
		
	def close(self):
		self.tempfile.close()
		
	
if __name__ == "__main__":
	with CPUTemp() as cpu_temp:
		print ("{} C".format(cpu_temp.get_temp()))
		print ("{} F".format(cpu_temp.get_temp_in_f()))