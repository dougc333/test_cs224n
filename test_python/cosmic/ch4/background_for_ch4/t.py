import pytest

@pytest.fixture
def foo():
  a=10
  print("I am foo")
  #there is no io? something odd
  #print("stderr:",os.stderr)
  return a

#well that sure is confusing
def test(foo):
  assert foo==10
  

#there has to be some logging feature in pytest
def test_log(foo):
  assert foo==foo


