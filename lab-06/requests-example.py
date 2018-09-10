import requests


def count_yelp(text):
    words =text.split()
    yelp_count=words.count('Yelp')
    return yelp_count

def replace_yelp(text):
    return text.replace ('Yelp','google')
    

if __name__ == "__main__":

    r = requests.get('http://wwww.yelp.com')
    if r.status_code == 200:
        #print count_yelp(r.text)
        print replace_yelp(r.text)




# Assignmenttext

# Load the yelp page and replace all occurance of yelp to google
# Load the file from http://censusdata.ire.org/36/all_050_in_36.P2.csv and find
# the max P002001

