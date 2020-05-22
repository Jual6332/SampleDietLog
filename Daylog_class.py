class DayLog:
  def __init__(self,dat,burn,consum):
    self.date = dat;
    self.burned = burn;
    self.consumed = consum;
    self.net = burn-consum;

  def get_calories_burned(self):
    return self.burned;

  def get_calories_consumed(self):
    return self.consumed;

  def get_calories_net(self):
    return self.net;

  def get_date(self):
    return self.date;

  def set_calories_burned(self,cals):
    self.burned = cals;

  def set_calories_consumed(self,cals):
    self.consumed = cals;

  def set_date(self,dat):
    self.date = dat;