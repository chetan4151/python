print("\n\n\t----------------->>>>>>>>>This program will Scrape info of hotels in delhi from OYO's website<<<<<<<<<<-----------------") 
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
import requests
import pandas
from bs4 import BeautifulSoup
url="https://www.oyorooms.com/hotels-in-delhi/?page="
maxpage = int(input("\n\nEnter number of pages you want to scrape: "))
data=[]
for page in range(1,maxpage+1):
    req=requests.get(url+str(page),headers=headers)
    parser=BeautifulSoup(req.content,'html.parser')
    all_hotels=parser.find_all('div',{'class':'hotelCardListing'})

    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict['Name']=hotel.find('h3',{'class':'listingHotelDescription__hotelName'}).text
        hotel_dict['Address']=hotel.find('span',{'itemprop':'streetAddress'}).text
        hotel_dict['Price']=hotel.find('span',{'class':'listingPrice__finalPrice'}).text
        amenities_elements=hotel.find('div',{'class':'amenityWrapper'})
        amenity_list=[]
        for amenity in amenities_elements.find_all('div',{'class':'amenityWrapper__amenity'}):
            amenity_list.append(amenity.find('span',{'class':'d-body-sm'}).text.strip())
        hotel_dict['Amenities']=', '.join(amenity_list[:-1])
        try:
            hotel_dict['Rating']=hotel.find('span',{'class':'hotelRating__ratingSummary'}).text
        except AttributeError:
            pass
        data.append(hotel_dict)
dataframe=pandas.DataFrame(data)
fname=input("Enter the filename with extension (.csv) where you want to save this info : ")
print("Creating csv file...")
dataframe.to_csv(fname)
print("File created successfully!!!")
