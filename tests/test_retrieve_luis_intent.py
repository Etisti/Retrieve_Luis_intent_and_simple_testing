# Unit tests should be fast, isolated, and repeatable
# The response of the LUISE engine depends of a a specific context
# in the futur add a CI/CD workflows, batch testing 

class test_retrieve_luis_intent(object):

    '''
    tests :
     - mock the api call
     - topIntent
     - entities
     - scores exceeds a threshold defined

    optimise :
        - use for multiple tests @pytest.mark.parametrize()
        - use pytest-benchmark to test the speed 
        - NLU.DevOps is recommanded for testing
    '''

    def test_intent(self,mock_requests_get):
        '''
        test the top intent
        '''
        assert mock_requests_get.prediction.topIntent == 'ModifyOrder'

    def test_entities(self,mock_requests_get):
        '''
        test entites found
        '''
        assert mock_requests_get.entities.Order.Quantity == 'two'

    def test_scores(self,mock_requests_get):
        '''
        test if scores exceeds 0.75 threshold 
        '''
        assert mock_requests_get.intents.prediction.ModifyOrder.score > 0.75