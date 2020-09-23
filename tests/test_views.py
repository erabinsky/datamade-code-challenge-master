import pytest
from parserator_web.views import AddressParse
import requests_mock
import requests
import usaddress

def test_get_resp(client):
    with requests_mock.Mocker() as m:
        a, err = client
        m.get("http://localhost:8000/api/parse", text=a)
        rsp = requests.post("http://localhost:8000/api/parse").text

        assert rsp.text == usaddress.RepeatedLabelError

### NOTE ###
#   I was totally unsuccessful with this part of the challenge. Based on how I understood @pytest.fixture params,
#   I figured the code above could be used to test both cases, but I seem to be missing something.
#   I don't have any experience with unit testing, and I tried my best to consult the documentation provided
#   by both Datamade and pytest. Normally, at that point, I would reach out for help, but being a coding challenge,
#   I felt that would have probably been inappropriate... BUT, I would really like to learn this skill,
#   so regardless of the outcome of this application process, would someone
#   be willing to walk me through this? It seems like particularly useful knowledge, and I am genuinely curious to learn more :)








    
# def test_api_parse_succeeds(client):
#     # TODO: Finish this test. Send a request to the API and confirm that the
#     # data comes back in the appropriate format.
#     address_string = '123 main st chicago il'
    
#     pytest.fail()


# # def test_api_parse_raises_error(client):
# #     # TODO: Finish this test. The address_string below will raise a
# #     # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
# #     address_string = '123 main st chicago il 123 main st'
# #     pytest.fail()

