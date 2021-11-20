from bs4 import BeautifulSoup

with open('example.html','r')as html_file:
		content = html_file.read()

		soup = BeautifulSoup(content, 'lxml')
		#print(soup)

		course_cards = soup.find_all('div', class_='card') #let's find all html div with class card.
		#print(course_cards)
		for course in course_cards:
			course_name = course.h5.text
			course_price = course.a.text.split()[-1]
			print(course_name)
			print(course_price)

			print(f'{course_name} costs {course_price}')
