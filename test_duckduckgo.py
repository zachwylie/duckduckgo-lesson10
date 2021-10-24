import pytest
from main import *


@pytest.mark.parametrize("expected", ["Washington", "Adams", "Jefferson", "Madison", "Monroe",
                                      "Jackson", "Buren", "Harrison", "Tyler", "Polk", "Taylor",
                                      "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson",
                                      "Grant", "Hayes", "Garfield", "Arthur", "Cleveland",
                                      "McKinley", "Roosevelt", "Taft", "Wilson",
                                      "Harding", "Coolidge", "Hoover", "Truman",
                                      "Eisenhower", "Kennedy", "Nixon", "Ford", "Carter",
                                      "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden"])
def test_ddg_search(expected):
    assert expected in ddg_search("presidents of the united states")
