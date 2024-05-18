configurationt through pytsst

1) fn name start w test eg. test_foo():
2) class name start with Test eg TestMyClass
3) test exceptions pytest.raises(ValueError,lambda:int("foo"))
   with pytest.raises(ValueError):
    int("foo")
well that is different....

https://blog.jetbrains.com/pycharm/2020/08/webinar-recording-simplify-your-tests-with-fixtures-with-oliver-bestwalter/

pytest --fixtures
pytest --fixtures-per-test
pytest --setup-plan
pytest --setup-only
pytest --setup-show

https://github.com/obestwalter/pytest-fixtures-introduction/tree/master/tests

pytest
1) pytest.fixtures annotation is a shortcut for DI. 
put the annotation on a function then pytest.fixtures will intantiate this for you
put the pytest.fixtures function name as an argument into fns which you want the code in pytest.fixtures to be executed
advantage: can put the pytest.fixture in cache. 

