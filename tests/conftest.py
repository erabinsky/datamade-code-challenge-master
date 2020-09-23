# Define test fixtures here.
import pytest
import usaddress

cases = [
    ('123 main st chicago il', None),
    ('123 main st chicago il 123 main st', usaddress.RepeatedLabelError)
]

@pytest.fixture(params=cases)
def client(request):
    return request.param

### NOTE ### 
# See comments in test_views.py