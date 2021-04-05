from retrieve_luis_intent import retrieve_luis_intent

if __name__ == "__main__":
    
    print("Here is the program to retrieve the intent of your utterance")

    appId = input("Give me (write) your appId : ")

    prediction_key = input("Give me (write) your prediction_key : ")

    prediction_endpoint = input("Give me (write) your prediction_endpoint : ")

    utterance = input("Give me (write) your utterance : ")

    retriever_of_intent = retrieve_luis_intent(appId,prediction_key,prediction_endpoint,utterance)

    intent = retriever_of_intent.()

    print(f'This is the retrieved intent : {intent}')

    print('A pizza_intent_response.json file has been generated !')
