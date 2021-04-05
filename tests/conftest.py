# Fixtures are gathered here
from unittest.mock import Mock
from pytest_mock import MockFixture
import pytest

@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    """Fixture for mocking requests.get."""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
    "query":"I want two large pepperoni pizzas on thin crust please",
    "prediction":{
       "topIntent":"ModifyOrder",
       "intents":{
          "ModifyOrder":{
             "score":1.0
          },
          "None":{
             "score":8.55e-09
          },
          "Greetings":{
             "score":1.82222226e-09
          },
          "CancelOrder":{
             "score":1.47272727e-09
          },
          "Confirmation":{
             "score":9.8125e-10
          }
       },
       "entities":{
          "Order":[
             {
                "FullPizzaWithModifiers":[
                   {
                      "PizzaType":[
                         "pepperoni pizzas"
                      ],
                      "Size":[
                         [
                            "Large"
                         ]
                      ],
                      "Quantity":[
                         2
                      ],
                      "Crust":[
                         [
                            "Thin"
                         ]
                      ],
                      "$instance":{
                         "PizzaType":[
                            {
                               "type":"PizzaType",
                               "text":"pepperoni pizzas",
                               "startIndex":17,
                               "length":16,
                               "score":0.9978157,
                               "modelTypeId":1,
                               "modelType":"Entity Extractor",
                               "recognitionSources":[
                                  "model"
                               ]
                            }
                         ],
                         "Size":[
                            {
                               "type":"SizeList",
                               "text":"large",
                               "startIndex":11,
                               "length":5,
                               "score":0.9984481,
                               "modelTypeId":1,
                               "modelType":"Entity Extractor",
                               "recognitionSources":[
                                  "model"
                               ]
                            }
                         ],
                         "Quantity":[
                            {
                               "type":"builtin.number",
                               "text":"two",
                               "startIndex":7,
                               "length":3,
                               "score":0.999770939,
                               "modelTypeId":1,
                               "modelType":"Entity Extractor",
                               "recognitionSources":[
                                  "model"
                               ]
                            }
                         ],
                         "Crust":[
                            {
                               "type":"CrustList",
                               "text":"thin crust",
                               "startIndex":37,
                               "length":10,
                               "score":0.933985531,
                               "modelTypeId":1,
                               "modelType":"Entity Extractor",
                               "recognitionSources":[
                                  "model"
                               ]
                            }
                         ]
                      }
                   }
                ],
                "$instance":{
                   "FullPizzaWithModifiers":[
                      {
                         "type":"FullPizzaWithModifiers",
                         "text":"two large pepperoni pizzas on thin crust",
                         "startIndex":7,
                         "length":40,
                         "score":0.90681237,
                         "modelTypeId":1,
                         "modelType":"Entity Extractor",
                         "recognitionSources":[
                            "model"
                         ]
                      }
                   ]
                }
             }
          ],
          "ToppingList":[
             [
                "Pepperoni"
             ]
          ],
          "$instance":{
             "Order":[
                {
                   "type":"Order",
                   "text":"two large pepperoni pizzas on thin crust",
                   "startIndex":7,
                   "length":40,
                   "score":0.9047088,
                   "modelTypeId":1,
                   "modelType":"Entity Extractor",
                   "recognitionSources":[
                      "model"
                   ]
                }
             ],
             "ToppingList":[
                {
                   "type":"ToppingList",
                   "text":"pepperoni",
                   "startIndex":17,
                   "length":9,
                   "modelTypeId":5,
                   "modelType":"List Entity Extractor",
                   "recognitionSources":[
                      "model"
                   ]
                }
             ]
          }
       }
    }
 }
    return mock
