import requests, json 

def emotion_detector(text_to_analyze):
    # Define a function that takes a string input (text_to_analyze)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create a dictionary with the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyze } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = input_json, headers=header)
	# If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion, key=emotion.get)
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    # If the response status code is 500, set to None
    elif response.status_code == 500:
        dominant_emotion = None
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
    # For any other unexpected status codes, set to None
    else:
        dominant_emotion = None
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        
	# Return the label and score in a dictionary
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': '<name of the dominant emotion>'
    }
