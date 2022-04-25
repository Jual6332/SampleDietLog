class DayLog:
  def __init__(self):
    self.date = "";
    self.burned = 0;
    self.consumed = 0;
    self.net = 0;

  # The class' Getter Methods
  def get_date(self):
    return self.date;

  def get_calories_burned(self):
    return self.burned;

  def get_calories_consumed(self):
    return self.consumed;

  def get_calories_net(self):
    return self.net;

  # The class' Setter Methods
  def set_date(self,dat):
    self.date = dat;

  def set_calories_burned(self,cals):
    self.burned = cals;

  def set_calories_consumed(self,cals):
    self.consumed = cals;
  
  # Custom class Methods
  def calculate_net_calories(self):
    pass

  def add_exercise(self,exercise):
    self.burned += exercise

