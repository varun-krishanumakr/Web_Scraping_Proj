from bs4 import BeautifulSoup

#Statement that allows me to open a file and read the contents of that specific file
#home.html is the name of the file that we want to open, r denotes that we want python to read that file only
with open('home.html', 'r') as html_file:
    #reading html file content only
    content = html_file.read()
    #prints out exactly what is in home.html
    #print(content)

    #parameters are the content of the webpage that we want to scrape and the parser method passed as a string
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())

    #grabs the first instance of the specified tag in the HTML document
    #tags = soup.find('h5')
    #print(tags)

    #grabs all instances of h5 tags on the website and iterates through them to only display their text
    #courses_html_tags = soup.find_all('h5')
    #for course in courses_html_tags:
        #print(course.text)
    
    #get all of the div tags that have the class attribute set to "card" (use the underscore after since class is a built in keyword in python)
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        #print the h5 tags of all of the different course_card divs (printing just course prints everything in the div) 
        #print(course.h5)
        
        #get and store the text in each of the h5 headers (the name of the course) and the text in each button (which contains course price)
        #update: use the .split() method on the text of the button and access the last element to get the last word (course price)
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        #print(course_name)
        #print(course_price)
        print(f'{course_name} costs {course_price}')
