from bs4 import BeautifulSoup #if you don't have then do pip install beautifulsoup4
import requests #requests library requests information from a specific website; if you don't have then do pip install requests
import time
#The following allows you to create and edit an excel spreadsheet through python
#import openpyxl

#excel = openpyxl.Workbook()
#sheet = excel.active
#sheet.title = 'Top Rated Movies'
#sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDB Rating])
#for each iteration of a for loop, append a list of same length with the attributes in this order to the sheet, then when you're done adding execute the following command:
#excel.save('IMDB Movie Ratings'.xlsx)

#Asks the user to input some skill that they are not familiar with
print("Put some skill that you are not familiar with")
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    #soup = BeautifulSoup(html_text.content) would work if we didn't put the .text at the end on the previous line
    #soup.prettify gives everything with indenting
    soup = BeautifulSoup(html_text, 'lxml')

    #soup.find(["h1", "h2"]) finds the first occurrence of either an h1 or h2 tag; if we changed find to find_all then it would find all instances of h1 and h2 tags
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    #can filter for elements with a specific ID like so:
    #paragraph = soup.find_all("p", attrs  = {"id": "paragraph-id"})
    #if ID isn't a valid ID, then nothing is stored in variable

    #can find an element with a specific text using soup.find_all("p", string = "[whatever specific text you're looking for]")
    #can also find string with some phrase/part of string using regex library (import re) and then do soup.find_all("p", string = re.compile("(S|s)ome")) if you want to find all strings with the word "Some" in it with different capitalizations

    #can select elements using .select method (like the find_all method) but with the exception of just adding additional tags on to search for nested tags
    #for example: soup.select("div p") finds all p tags within div tags
    #to find all tags that occur after a specific tag: soup.select("h2 ~ p") to find all p tags that occur after h2 tags
    #to find tags with specific IDs: soup.select("p#paragraph-id b") gives all bold elemends nested inside a p tag with ID paragraph-id
    #can also find tags that are a direct descendant of a specific tag (i.e. not a grandchild, great grandchild, etc.): soup.select("body > p") -- can use a for loop to iterate through these elements to further sort
    
    #enumerate function allows us to iterate over the jobs list indices and the contents
    #index is the actual index/counter while the job is the actual job beautifulsoup object
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            #get the actual link that's within an a tag
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                #each .txt file should be 0.txt, 1.txt,...
                #f variable after "as" allows you to write to the given file
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info:  {more_info}")
                
                print(f"File saved: {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        #allows program to wait some time before continuing (600 seconds = 10 min)
        time_wait = 10
        print(f'Waiting {time_wait} minutes ...')
        time.sleep(time_wait * 60)