# pip install requests 
# pip install bs4
# pip install django

import requests
from django.http import JsonResponse
from bs4 import BeautifulSoup

def extract_list_data(url, div_class):
    listOfStories = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            div = soup.find('div', class_=div_class)
            if div:
                # Extracting all <ul> from the div
                # by sonam.rani.min20@itbhu.ac.in
                list_items = div.find_all(['ul'])
                if list_items:
                    for list_item in list_items:
                        # Extract all <li> from the <ul>
                        items = list_item.find_all('li')
                        # print(items)
                        for item in items:
                            # link = item.select("a")[0]
                            a_tag = item.find('a')

                            # # Extract the value of the 'href' attribute
                            href_value = a_tag['href']
                            link = str(url+href_value)
                            # print(link)
                            # heading = str(item.a.text)
                            heading = str(item.find("h3").text)
                            # print(heading)
                            # listOfStories.append({link,heading})
                            listOfStories.append({'title':heading,'link':link})

                else:
                    print("No list found inside the div.")
            else:
                print("Div with class '{}' not found.".format(div_class))
        else:
            print("Failed to fetch the data from webpage. Status code:", response.status_code)
        return listOfStories
    except Exception as error:
        print("Something went wrong:", error)



def get_time_stories(request):
    try:
        # Example usage
        url = "https://time.com"  # Replace this with the URL you want to scrape
        div_class = "partial latest-stories"
        res = extract_list_data(url,div_class)
        for i in res:
            print(i)
        latest_stories = res
        return JsonResponse(latest_stories, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)})



