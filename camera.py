class exposureCalc:
	def __init__(self, sunrise, sunset):
		self.sunrise=sunrise
		self.sunset=sunset
		self.span_midnight=self.sunset < self.sunrise
	def get_exposure(self, time):
                
		if not self.span_midnight and (time >=self.sunrise and time <=self.sunset):
			return 'auto'
		elif self.span_midnight and (time >= self.sunrise or time <= self.sunset):
			return 'auto'
		else:
			return 'night'
		
	#One hour either side of sunrise/set
	def take_shot(self, time):
		if not self.span_midnight and (time >=self.sunrise and time <=self.sunset):
			return True
		elif self.span_midnight and (time >= self.sunrise or time <= self.sunset):
			return True
		else:
			return False
