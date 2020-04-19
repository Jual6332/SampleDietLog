import matplotlib

class DayLog:
  def __init__(self,date,burn,consum):
    self.date = date;
    self.burned = burn;
    self.consumed = consum;
    pass
  def set_calories_burned(self,cals):
    self.burned = cals;


# Initialisation
april_2020 = []
may_2020 = []

# Define April Data
april19 = DayLog("4/19",170,960*2+90)

april_2020.append(april19)

# 

