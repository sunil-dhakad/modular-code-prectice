

import pytest

class NOtInRange(Exception):
  def __init__(self,message="value not in range"):
    slef.message= message
    super.__init__(self.message)


def test_generic():
  a=5

  with pytest.raises(NOtInRange):
    if a not in Range(10,20):
      raise NOtInRange


def test_trial():

  a=3
  b=3
  assert True
