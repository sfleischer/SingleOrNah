# Gather relevant information from a given image.
# Adapted from Microsoft Azure Face API Quickstart Guide and Documentation.
# Written by Derek Leung for Princeton Hacks fa2017.

import http.client, urllib, base64, json, requests
#import requests

# Replace the subscription_key string value with your valid subscription key.
subscription_key = 'dfbf8eff05414406a5e0d33268caa0f9'

# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
uri_base = 'https://westcentralus.api.cognitive.microsoft.com'

# Request headers.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Obtain gender and age of person in given profile picture
# If multiple people in a given profile picutre, use most likely gender and average age
def gather_info_profile_pic (url):
    num_males = 0
    num_females = 0
    agg_age = 0
    count = 0

    # Establish required parameters
    params = {
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender',
    }

    body = {'url': url}
    try:
        # Execute the REST API call and get the response.
        response = requests.request('POST', uri_base + '/face/v1.0/detect', json=body, data=None, headers=headers, params=params)
        parsed = json.loads(response.text)

        '''
        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()

        # 'data' contains the JSON data and parsed is the JSON in dictionary form
        parsed = json.loads(data)
        '''
        count = len(parsed)
        print (parsed)

        # Iterate through all individual's face attributes to aggregate information.
        for x in range(count):
            agg_age += parsed[x]['faceAttributes']['age']
            if (parsed[x]['faceAttributes']['gender'] == 'male'):
                num_males += 1
            else:
                num_females += 1

        # Figure out if the target is male or female (ties to go females).
        ret_gender = 'female'
        if (num_males > num_females):
            ret_gender = 'male'

        # Figure out the average age of all individuals.
        ret_age = 0
        if (count != 0):
            ret_age = agg_age / count

        # Return (gender, age) for the target
        ans = [ret_gender, ret_age]
        return ans

        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

# Create json with the relevant data given a post image, poster's gender and age (we call this poster tgt).
def gather_info_post (url, tgt_gender, tgt_age):

    # Relevant data for evaluating score.
    num_same_gender = 0
    num_opp_gender = 0
    agg_happiness = 0
    agg_disgust = 0
    agg_smile = 0

    # Establish parameters
    params = {
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,emotion,smile',
    }

    body = {'url': url}
    try:
        # Execute the REST API call and get the response.
        response = requests.request('POST', uri_base + '/face/v1.0/detect', json=body, data=None, headers=headers, params=params)
        parsed = json.loads(response.text)

        '''
        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()

        # 'data' contains the JSON data and parsed is the JSON in dictionary form
        '''
        count = len(parsed)
        
        # Constant for relevant age range (don't want to include people that are too old/young)
        age_range = 10

        # Handle edge case where tgt_age is 0, increase the range to 100
        if (tgt_age == 0):
            age_range = 100

        # Iterate through all participants face attributes only counting those of opposite sex
        # and within +/- age_range with the target.
        for x in range(count):
            if parsed[x]['faceAttributes']['age'] > tgt_age - age_range and parsed[x]['faceAttributes']['age'] < tgt_age + age_range:
                if (parsed[x]['faceAttributes']['gender'] != tgt_gender):
                    num_opp_gender += 1
                else:
                    num_same_gender += 1
            agg_happiness += parsed[x]['faceAttributes']['emotion']['happiness']
            agg_happiness += parsed[x]['faceAttributes']['emotion']['disgust']
            agg_smile += parsed[x]['faceAttributes']['smile']

        # Return data for an insta post with num of opposing gender, aggregated happiness, aggregated
        # disgust, and aggregated smiles
        if (count != 0):
            avg_happiness = agg_happiness / count
            avg_disgust = agg_disgust / count
            avg_smile = agg_smile / count

        ans = [num_same_gender, num_opp_gender, avg_happiness, avg_disgust, avg_smile]
        return ans

        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

#gather_info_post('http://hinewyork.org/wp-content/uploads/2012/10/shutterstock_20253523.jpg', 'male', 10)
gather_info_post('http://www.webberenergygroup.com/wpnew/wp-content/uploads/green-1040x325.jpg', 'male', 32)
#('http://www.webberenergygroup.com/wpnew/wp-content/uploads/green-1040x325.jpg', 'female', 32.7)
#gather_info_profile_pic('http://www.stefantell.se/blog/wp-content/uploads/2013/12/lighting-groups-of-two-people-with-one-light.jpg')
