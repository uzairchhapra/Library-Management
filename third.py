from project2_gui import Ui_MainWindow
from mysql.connector import connect
from PyQt5.QtWidgets import QApplication, QMainWindow
import datetime
import smtplib


today = datetime.date.today()
smtpUser = 'pythonlibraryproject@gmail.com'
smtpPass = 'pythonproject1'

					
conn = connect(host = 'localhost', database = 'csv_db', user = 'root', password = '')
cursorb = conn.cursor()

mem = connect(host = 'localhost', database = 'members', user = 'root', password = '')
cursorm = mem.cursor()
flag=0

class Second(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.init_login_button()
		self.init_regi_page_button()
		self.init_regi_gender_combobox()

	def init_login_button(self):
		self.register_pushButton.clicked.connect(self.on_move_to_register)
		self.login_pushButton.clicked.connect(self.move_to_logged_in)


	def init_regi_page_button(self):
		self.pushbutton_regi_back.clicked.connect(self.on_move_to_login)
		self.submit_regi.clicked.connect(self.new_member_registeration)	
		self.pushButton.clicked.connect(self.move_to_logged_in)
	def init_regi_gender_combobox(self):
		self.gender_input_regi.addItems(['Male', 'Female', 'Others'])
	def on_move_to_register(self):
		self.box.setCurrentIndex(1)
	def on_move_to_login(self):
		self.box.setCurrentIndex(0)

	def book_search_name(self):
		global flag
		if flag==1:
			print('Entered funtion booksearchname')
			cursorb = conn.cursor()
			cursorm = mem.cursor()
			self.book_name = self.Book_name_search.text().lower()
			query = 'select * from table1 where original_title=%s'
			cursorb.execute(query, (self.book_name,))
			self.bookdb = cursorb.fetchone()
			self.Book_found_label.setText('Book Found')
			self.Issue_book_pushButton.setText('Issue')
			print('Printing bookdb of book_search_name=',self.bookdb,'Type=', type(self.bookdb))
			mem.commit()
			conn.commit()
			self.req = 1
			self.Issue_book_pushButton.clicked.connect(self.issue_new_book)
			flag=0
		else:
			pass

		#return 
	def issue_new_book(self):
		print('Entered function issue_new_book')
		cursorb = conn.cursor()
		cursorm = mem.cursor()
		print(self.books_taken)
		if self.books_taken < 4 :
			due_date = today + datetime.timedelta(days = 7)
			print('Printing bookdb of issue new book:',self.bookdb)
			author = self.bookdb[1]
			author = author.split(',')[0]
			print('Author=',author)
			message = ''
			#query = 'UPDATE membership SET %s=%s where membershipno=%s'
			print('Books Taken=',self.books_taken)
			print('Book1=',self.book_1,'Type=', type(self.book_1))
			print('Book2',self.book_2,'Type=', type(self.book_2))
			print('Book3',self.book_3,'Type=', type(self.book_3))
			self.req = 1
			if self.book_1 == '0':
				self.book_1 = self.book_name
				print('updating books taken from condition book1==0 is--=',self.books_taken)
				self.books_taken += 1
				query1 = 'UPDATE membership SET book1=%s WHERE membershipno=%s'
				query2 = 'UPDATE membership SET bookstaken=%s WHERE membershipno=%s'
				query3 = 'UPDATE membership SET book1_date=%s WHERE membershipno=%s'
				cursorm.execute(query1, (self.book_name, self.membershipno))
				cursorm.execute(query2, (self.books_taken, self.membershipno))
				cursorm.execute(query3, (due_date, self.membershipno))
				self.req = 0
				print('req', self.req)
				print('Book Issued Name:',self.book_name)
				print('Membership No:',self.membershipno)
				print('Books Taken=',self.books_taken)
				print('Due Date:',str(due_date.strftime('%d/%m/%Y')))
				message = 'Book-1 is issued: '
				pass
			elif self.book_1 !='0' and self.book_2 == '0':
				print('bookstaken : ' , self.books_taken)
				self.books_taken += 1
				self.book_2 = self.book_name
				query1 = 'UPDATE membership SET book2=%s WHERE membershipno=%s'
				query2 = 'UPDATE membership SET bookstaken=%s WHERE membershipno=%s'
				query3 = 'UPDATE membership SET book2_date=%s WHERE membershipno=%s'
				cursorm.execute(query1, (self.book_name, self.membershipno))
				cursorm.execute(query2, (self.books_taken, self.membershipno))
				cursorm.execute(query3, (due_date, self.membershipno))
				print('Book Issued Name:',self.book_name)
				print('Membership No:',self.membershipno)
				print('Books Taken=',self.books_taken)
				print('Due Date:',str(due_date.strftime('%d/%m/%Y')))
				self.req = 0
				print('req', self.req)
				'''
				cursorm.execute(query, ('book2', self.book_name, self.membershipno))
				cursorm.execute(query, ('bookstaken', self.books_taken, self.membershipno))
				cursorm.execute(query, ('book2_date', due_date, self.membershipno))
				'''
				message = 'Book-2 is issued: '
				pass
			elif self.book_1!='0' and self.book_2!='0' and self.book_3 == '0':
				self.books_taken += 1
				print('bookstaken : ' , self.books_taken)
				self.book_3 = self.book_name
				query1 = 'UPDATE membership SET book3=%s WHERE membershipno=%s'
				query2 = 'UPDATE membership SET bookstaken=%s WHERE membershipno=%s'
				query3 = 'UPDATE membership SET book3_date=%s WHERE membershipno=%s'
				cursorm.execute(query1, (self.book_name, self.membershipno))
				cursorm.execute(query2, (self.books_taken, self.membershipno))
				cursorm.execute(query3, (due_date, self.membershipno))
				print('Book Issued Name:',self.book_name)
				print('Membership No:',self.membershipno)
				print('Books Taken=',self.books_taken)
				print('Due Date:',str(due_date.strftime('%d/%m/%Y')))
				self.req = 0
				print('req', self.req)
				'''
				cursorm.execute(query, ('book3', self.book_name, self.membershipno))
				cursorm.execute(query, ('bookstaken', self.books_taken, self.member
				shipno))
				cursorm.execute(query, ('book3_date', due_date, self.membershipno))
				'''
				message = 'Book-3 is issued: '
				pass
			else:
				print('bookstaken : ' , self.books_taken)
				print('max limit is 3 books')
				self.Registration_sucessfull.setText('max limit is 3 books')
				self.box.setCurrentIndex(3)
				self.back_pushButton.clicked.connect(self.move_to_logged_in)
				return
			query4 = 'UPDATE membership SET booksread=%s WHERE membershipno=%s'
			self.booksread += 1
			cursorm.execute(query4, (self.booksread, self.membershipno))
			original_release = self.bookdb[2]
			title = self.bookdb[4]
			lang = self.bookdb[5]
			rating = self.bookdb[6]
			message += '\nOriginal Title:' + self.book_name + '\nTitle: ' + title + '\nAuthor: ' + author + '\nOriginal release: ' + str(original_release) + '\nLanguage: ' + lang + '\nRatings: ' + str(rating) + '\nDate of issue: ' + str(today.strftime('%d/%m/%Y')) + "\nDue day to return the book: " + str(due_date.strftime('%d/%m/%Y')) + ".\nIf the book is not returned on time then a fine of 10 per day would be charged to the Member."
			self.Registration_sucessfull.setText(message)
			self.box.setCurrentIndex(3)
			self.back_pushButton.clicked.connect(self.move_to_logged_in)
			toAdd = self.email
			fromAdd = smtpUser
			subject = 'New Book issued'
			header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: '+ subject
			body = message
			print(body)
			s = smtplib.SMTP('smtp.gmail.com',587)
			s.starttls()
			s.login(smtpUser,smtpPass)
			s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
			s.quit()
			print(message)
			mem.commit()
			conn.commit()
			#return
				
				
		else :
			print('Entered the last else of issue_new_book\nMax limit is 3 books')
			self.Registration_sucessfull.setText('Max limit is 3 books')
			self.box.setCurrentIndex(3)
			self.back_pushButton.clicked.connect(self.move_to_logged_in)

	def issue1(self):
		global flag
		if flag==1:
			print('Entered issue1')
			cursorm = mem.cursor()
			self.book_name = self.book1_diplay_browse.text().lower()
			query = 'select * from table1 where original_title=%s'
			cursorb.execute(query, (self.book_name,))
			self.bookdb = cursorb.fetchone()
			self.Book_found_label.setText('Book Found')
			self.Issue_book_pushButton.setText('Issue')
			print('Printing bookdb of issue1=',self.bookdb,'Type=', type(self.bookdb))
			mem.commit()
			conn.commit()
			self.req = 1
			self.issue_new_book()
			flag=0
		else:
			pass
	
	def issue2(self):
		global flag
		if flag==1:
			print('Entered issue2')
			cursorm = mem.cursor()
			self.book_name = self.book2_diplay_browse.text().lower()
			query = 'select * from table1 where original_title=%s'
			cursorb.execute(query, (self.book_name,))
			self.bookdb = cursorb.fetchone()
			self.Book_found_label.setText('Book Found')
			self.Issue_book_pushButton.setText('Issue')
			print('Printing bookdb of issue2=',self.bookdb,'Type=', type(self.bookdb))
			mem.commit()
			conn.commit()
			self.req = 1
			self.issue_new_book()
			flag=0
		else:
			pass

	def issue3(self):
		global flag
		if flag==1:
			print('Entered issue3')
			cursorm = mem.cursor()
			self.book_name = self.book3_diplay_browse.text().lower()
			query = 'select * from table1 where original_title=%s'
			cursorb.execute(query, (self.book_name,))
			self.bookdb = cursorb.fetchone()
			self.Book_found_label.setText('Book Found')
			self.Issue_book_pushButton.setText('Issue')
			print('Printing bookdb of issue3=',self.bookdb,'Type=', type(self.bookdb))
			mem.commit()
			conn.commit()
			self.req = 1
			self.issue_new_book()
			flag=0
		else:
			pass
	def issue4(self):
		global flag
		if flag==1:
			print('Entered issue4')
			cursorm = mem.cursor()
			self.book_name = self.book4_diplay_browse.text().lower()
			query = 'select * from table1 where original_title=%s'
			cursorb.execute(query, (self.book_name,))
			self.bookdb = cursorb.fetchone()
			self.Book_found_label.setText('Book Found')
			self.Issue_book_pushButton.setText('Issue')
			print('Printing bookdb of issue4=',self.bookdb,'Type=', type(self.bookdb))
			mem.commit()
			conn.commit()
			self.req = 1
			self.issue_new_book()
			flag=0
		else:
			pass
	def issue5(self):
		global flag
		if flag==1:
			print('Entered issue5')
			cursorm = mem.cursor()
			self.book_name = self.book5_diplay_browse.text().lower()
			query = 'select * from table1 where original_title=%s'
			cursorb.execute(query, (self.book_name,))
			self.bookdb = cursorb.fetchone()
			self.Book_found_label.setText('Book Found')
			self.Issue_book_pushButton.setText('Issue')
			print('Printing bookdb of issue5=',self.bookdb,'Type=', type(self.bookdb))
			mem.commit()
			conn.commit()
			self.req = 1
			self.issue_new_book()
			flag=0
		else:
			pass
	
	def  book_browse(self):
		cursorb = conn.cursor()
		name = "'" + self.search_book_input.text()
		query = query = "SELECT * FROM table1 WHERE original_title LIKE " + name + "%'"
		cursorb.execute(query)
		while True:
			global flag
			a = cursorb.fetchone()
			if a is None:
				break
			for i in range(4):
				if a is not None :
					self.book1_diplay_browse.setText(a[3])
					flag=1
					self.book1_issue_pushButton.clicked.connect(self.issue1)
				a = cursorb.fetchone()
				if a is not None :
					self.book2_diplay_browse.setText(a[3])
					flag=1
					self.book2_issue_pushButton.clicked.connect(self.issue2)
				a = cursorb.fetchone()
				if a is not None :
					self.book3_diplay_browse.setText(a[3])
					flag=1
					self.book3_issue_pushButton.clicked.connect(self.issue3)
				a = cursorb.fetchone()
				if a is not None :
					self.book4_diplay_browse.setText(a[3])
					flag=1
					self.book4_issue_pushButton.clicked.connect(self.issue4)
				a = cursorb.fetchone()
				if a is not None :
					self.book5_diplay_browse.setText(a[3])
					flag=1
					self.book5_issue_pushButton.clicked.connect(self.issue5)

	def on_move_browse(self):
		self.box.setCurrentIndex(2)
		self.browse_search_pushButton.clicked.connect(self.book_browse)	
	def move_to_logged_in(self):
		cursorb = conn.cursor()
		cursorm = mem.cursor()
		self.membershipno = int(self.membershipno_login.text())
		self.Book_found_label.setText('')
		self.Issue_book_pushButton.setText('')
		password = self.password_login.text()
		print(self.membershipno, type(self.membershipno))
		print(password, type(password))
		query = 'select * from membership where membershipno=%s'
		cursorm.execute(query, (self.membershipno,))
		a = cursorm.fetchone()
		mem.commit()
		conn.commit()

		print(a)
		global flag
		if password == a[2]:
			print('correct password')
			self.box.setCurrentIndex(4)
			flag=1
			self.Book_search_pushButton.clicked.connect(self.book_search_name)
			self.browse_pushbutton.clicked.connect(self.on_move_browse)
			self.books_taken = a[13]
			self.email = a[5]
			self.book_1 = a[7]
			self.book_1_due_date = a[8]
			self.book_2 = a[9]
			self.book_2_due_date = a[10]
			self.book_3 = a[11]
			self.book_3_due_date = a[12]
			self.booksread = a[15]
			print(self.book_1)
			print(self.book_2)
			print(self.book_3)
			print(self.books_taken)
			print(self.email)
			if self.books_taken > 0:
				self.Book1_label.setText(self.book_1)
				self.Book2_label.setText(self.book_2)
				self.Book3_label.setText(self.book_3)
				if self.book_1=='0':
					self.Book1_return_pushButton.setText('Add')
				else:
					self.Book1_return_pushButton.setText('Return')
					self.Book1_return_pushButton.clicked.connect(self.return_book1)
				if self.book_2=='0':
					self.Book2_return_pushButton.setText('Add')
				else :
					self.Book2_return_pushButton.setText('Return')
					self.Book2_return_pushButton.clicked.connect(self.return_book2)
				if self.book_3=='0':
					self.Book3_return_pushButton.setText('Add')
				else:
					self.Book3_return_pushButton.setText('Return')
					self.Book3_return_pushButton.clicked.connect(self.return_book3)
			else :
				self.Book1_label.setText('')
				self.Book2_label.setText('')
				self.Book3_label.setText('')
				self.Book1_return_pushButton.setText('Add')
				self.Book2_return_pushButton.setText('Add')
				self.Book3_return_pushButton.setText('Add')
				self.Book1_return_pushButton.clicked.connect(self.book_add)



		else:
			print('wrong password')
			self.Registration_sucessfull.setText('Wrong Password')
			self.box.setCurrentIndex(3)
			self.back_pushButton.clicked.connect(self.move_to_logged_in)



	def return_book1(self):
		print('Entered return_book1')
		if self.book_1=='0':
			pass
		else:
			cursorb = conn.cursor()
			cursorm = mem.cursor()
			print('Book1 from return_book1=',self.book_1)
			print('Memb no=',self.membershipno)
			print('Books taken=',self.books_taken)
			print('Book1 due date=',self.book_1_due_date)
			close_connection()
			cursorb = conn.cursor()
			query = "select * from table1 where original_title like "+"'"+self.book_1+"%'"
			cursorb.execute(query)
			self.bookdb = cursorb.fetchone()
			mem.commit()
			conn.commit()
			print('Printing bookdb of returnbook1:',self.bookdb)
			author = self.bookdb[1]
			author = author.split(',')[0]
			original_release = self.bookdb[2]
			title = self.bookdb[4]
			lang = self.bookdb[5]
			rating = self.bookdb[6]
			message = 'Book-1 Returned :\n' + '\nOriginal Title: ' + self.book_1 + '\nTitle: ' + title + '\nAuthor: ' + author + '\nOriginal release: ' + str(original_release) + '\nLanguage: ' + lang + '\nRatings: ' + str(rating) + '\nDate of issue: ' + str(today.strftime('%d/%m/%Y')) + '\nDue day to return the book: ' + str(self.book_1_due_date.strftime('%d/%m/%Y')) + '\nReturned Date: ' + str(today.strftime('%d/%m/%Y'))

			self.book_1 = '0'
			self.books_taken -= 1
			self.book_1_due_date = datetime.date(year = 1001, month = 1, day = 1)
			print('Book1 from return_book1=',self.book_1)
			print('Memb no=',self.membershipno)
			print('Books taken=',self.books_taken)
			print('Book1 due date=',self.book_1_due_date)
			query1 = 'UPDATE membership SET book1=%s WHERE membershipno=%s'
			query2 = 'UPDATE membership SET book1_date=%s WHERE membershipno=%s'
			query3 = 'UPDATE membership SET bookstaken=%s WHERE membershipno=%s'
			cursorm.execute(query1, (self.book_1, self.membershipno))
			cursorm.execute(query2, (self.book_1_due_date, self.membershipno))
			cursorm.execute(query3, (self.books_taken, self.membershipno))
			mem.commit()
			conn.commit()
			cursorb.close()
			cursorm.close()
			self.Registration_sucessfull.setText(message)
			self.box.setCurrentIndex(3)
			self.back_pushButton.clicked.connect(self.move_to_logged_in)
			toAdd = self.email
			fromAdd = smtpUser
			subject = 'Book-1 Returned'
			header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: '+ subject
			body = message
			s = smtplib.SMTP('smtp.gmail.com',587)
			s.starttls()
			s.login(smtpUser,smtpPass)
			s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
			s.quit()
			print(message)
	def return_book2(self):
		if self.book_2=='0':
			pass
		else:
			print('Entered return_book2')
			#cursorb = conn.cursor()
			#cursorm = mem.cursor()
			print('Book2 of return_book2=',self.book_2)
			print('Memb no=',self.membershipno)
			print('Books taken=',self.books_taken)
			print('Book2 duedate=',self.book_2_due_date)
			close_connection()
			cursorb = conn.cursor()
			query = "select * from table1 where original_title like "+"'"+self.book_2+"%'"
			cursorb.execute(query)
			self.bookdb = cursorb.fetchone()
			#mem.commit()
			#conn.commit()
			author = self.bookdb[1]
			author = author.split(',')[0]
			original_release = self.bookdb[2]
			title = self.bookdb[4]
			lang = self.bookdb[5]
			rating = self.bookdb[6]
			message = 'Book-2 Returned :\n' + '\nOriginal Title: ' + self.book_2 + '\nTitle: ' + title + '\nAuthor: ' + author + '\nOriginal release: ' + str(original_release) + '\nLanguage: ' + lang + '\nRatings: ' + str(rating) + '\nDate of issue: ' + str(today.strftime('%d/%m/%Y')) + '\nDue day to return the book: ' + str(self.book_2_due_date.strftime('%d/%m/%Y')) + '\nReturned Date: ' + str(today.strftime('%d/%m/%Y'))

			self.book_2 = '0'
			self.books_taken -= 1
			self.book_2_due_date = datetime.date(year = 1001, month = 1, day = 1)
			print('Book2 of return_book2=',self.book_2)
			print('Memb no=',self.membershipno)
			print('Books taken=',self.books_taken)
			print('Book2 due date=',self.book_2_due_date)
			close_connection()
			cursorm = mem.cursor()
			query1 = 'UPDATE membership SET book2=%s WHERE membershipno=%s'
			query2 = 'UPDATE membership SET book2_date=%s WHERE membershipno=%s'
			query3 = 'UPDATE membership SET bookstaken=%s WHERE membershipno=%s'
			cursorm.execute(query1, (self.book_2, self.membershipno))
			cursorm.execute(query2, (self.book_2_due_date, self.membershipno))
			cursorm.execute(query3, (self.books_taken, self.membershipno))
			self.Registration_sucessfull.setText(message)
			self.back_pushButton.clicked.connect(self.move_to_logged_in)
			self.box.setCurrentIndex(3)
			toAdd = self.email
			fromAdd = smtpUser
			subject = 'Book-2 Returned'
			header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: '+ subject
			body = message
			s = smtplib.SMTP('smtp.gmail.com',587)
			s.starttls()
			s.login(smtpUser,smtpPass)
			s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
			s.quit()
	def return_book3(self):
		print('Entered return_book3')
		if self.book_3=='0':
			pass
		else:
			#cursorb = conn.cursor()
			#cursorm = mem.cursor()
			print('Book3 of return_book3=',self.book_3)
			print('Memb no=',self.membershipno)
			print('Books taken=',self.books_taken)
			print('Book3 due date=',self.book_3_due_date)
			close_connection()
			cursorb = conn.cursor()
			query = "select * from table1 where original_title like "+"'"+self.book_3+"%'"
			cursorb.execute(query)
			self.bookdb = cursorb.fetchone()
			author = self.bookdb[1]
			author = author.split(',')[0]
			original_release = self.bookdb[2]
			title = self.bookdb[4]
			lang = self.bookdb[5]
			rating = self.bookdb[6]
			message = 'Book-1 Returned :\n' + '\nOriginal Title: ' + self.book_3 + '\nTitle: ' + title + '\nAuthor: ' + author + '\nOriginal release: ' + str(original_release) + '\nLanguage: ' + lang + '\nRatings: ' + str(rating) + '\nDate of issue: ' + str(today.strftime('%d/%m/%Y')) + '\nDue day to return the book: ' + str(self.book_3_due_date.strftime('%d/%m/%Y')) + '\nReturned Date: ' + str(today.strftime('%d/%m/%Y'))

			self.book_3 = '0'
			self.books_taken -= 1
			self.book_3_due_date = datetime.date(year = 1001, month = 1, day = 1)
			print('Book3 of return_book3=',self.book_3)
			print('Memb no=',self.membershipno)
			print('Books taken=',self.books_taken)
			print('Book3 due date=',self.book_3_due_date)
			query1 = 'UPDATE membership SET book3=%s WHERE membershipno=%s'
			query2 = 'UPDATE membership SET book3_date=%s WHERE membershipno=%s'
			query3 = 'UPDATE membership SET bookstaken=%s WHERE membershipno=%s'
			cursorm.execute(query1, (self.book_3, self.membershipno))
			cursorm.execute(query2, (self.book_3_due_date, self.membershipno))
			cursorm.execute(query3, (self.books_taken, self.membershipno))
			mem.commit()
			conn.commit()
			cursorb.close()
			cursorm.close()
			self.Registration_sucessfull.setText(message)
			self.box.setCurrentIndex(3)
			self.back_pushButton.clicked.connect(self.move_to_logged_in)
			toAdd = self.email
			fromAdd = smtpUser
			subject = 'Book-3 Returned'
			header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: '+ subject
			body = message
			s = smtplib.SMTP('smtp.gmail.com',587)
			s.starttls()
			s.login(smtpUser,smtpPass)
			s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
			s.quit()
	def book_add(self):
		pass
	def new_member_registeration(self):
		global mem
		global conn
		name = self.name_input_regi.text()
		dob = self.dob_input_regi.date().toPyDate()
		password = self.password_regi.text()
		gender = self.gender_input_regi.currentText()
		email = self.email_regi.text()
		phone = self.phone_regi.text()
		membership_validity = today + datetime.timedelta(days = 365)
		print(name, type(name))
		print(dob, type(dob))
		print(password, type(password))
		print(gender, type(gender))
		print(email, type(email))
		print(phone, type(phone))
		if gender == 'Male':
			gender = 'M'
		elif gender == 'Female':
			gender = 'F'
		else:
			gender = 'O'
		close_connection()
		cusorm=mem.cursor()
		query = 'insert into membership(name, password, birthday, gender, email, phoneno, membershipvalidity) values(%s, %s, %s, %s, %s, %s, %s)'
		cursorm.execute(query, (name, password, dob, gender, email, phone, membership_validity))
		mem.commit()
		conn.commit()
		query = 'select * from membership where name=%s'
		cursorm.execute(query, (name,))
		a = cursorm.fetchone()
		if a[4] == 'M':
			gender = 'Male'
		elif a[4] == 'F':
			gender = 'Female'
		else:
			gender = 'Others' 
		print('Membership No : ' + str(a[0]))
		print('Name : ' + a[1])
		print('Password : ' + a[2])
		print('DOB : ' + str(a[3]))
		print('Gender : ' + gender)
		print('Email Address : ' + a[5])
		print('Phone No. : ' + a[6])
		print('Books Taken : ' + str(a[7]))
		print('Membership Validity : ' + str(membership_validity.strftime('%d/%m/%Y')))
		toAdd = email
		fromAdd = smtpUser
		subject ='New Library Registration'
		header ='To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' +'Subject: '+subject
		body = 'Congratulations ' + name + ' on a new Membership at our Library\nYour Details are as follows:\n' + 'Membership No : ' + str(a[0]) + '\nName : ' + a[1] + '\nPassword : ' + a[2] + '\nDOB : ' + str(a[3]) + '\nGender : ' + gender + '\nEmail Address : ' + a[5] + '\nPhone No. : ' + a[6] + '\nBooks Taken : ' + str(a[7]) + '\nMembership Validity Upto : ' + str(membership_validity.strftime('%d/%m/%Y')) + '\nThank you for registering with us, we hope to provide you with all the help we can, contact the above email-address for any further assistance.'
		
		s = smtplib.SMTP('smtp.gmail.com',587)
		s.starttls()
		s.login(smtpUser,smtpPass)
		s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
		s.quit()
		self.Registration_sucessfull.setText('Sucessfully Registered\n' + 'Congratulations on a new Membership at our Library\nYour Details are as follows\n' + 'Membership No : ' + str(a[0]) + '\nName : ' + a[1] + '\nPassword : ' + a[2] + '\nDOB : ' + str(a[3]) + '\nGender : ' + gender + '\nEmail Address : ' + a[5] + '\nPhone No. : ' + a[6] + '\nBooks Taken : ' + str(a[7]) + '\nMembership Validity Upto : ' + str(membership_validity.strftime('%d/%m/%Y')))
		self.box.setCurrentIndex(3)
		self.back_pushButton.clicked.connect(self.on_move_to_login)
		#cursorm.close()
		#cursorb.close()


	def on_move_to_register(self):
		self.box.setCurrentIndex(1)
	def on_move_to_login(self):
		self.box.setCurrentIndex(0)



def get_details(name):
	'''
	query = 'select * from books1 where Name=%s'
	cursor.execute(query, (name,))
	b = cursor.fetchone()
	print(b)
	'''
	query = 'select * from table1 where title=%s'
	cursor.execute(query, (name,))
	b = cursor.fetchone()
	print(b)
def displayall():
	query = 'select * from table1'
	cursor.execute(query)
	#b = cursor.fetchone()
	for i in range(10):
		a = cursor.fetchone()
		print(a)
'''
while True:
	print('1. Search a book')
	print('2. Display books')

	n = int(input('Select from one option above : '))
	if n == 1:
		n = input('Enter the name of the book : ')
		get_details(n)
	elif n == 2 :
		displayall()
	else:
		exit()
'''
def close_connection():
	conn = connect(host = 'localhost', database = 'csv_db', user = 'root', password = '')
	mem = connect(host = 'localhost', database = 'members', user = 'root', password = '')
	mem.close()
	conn.close()
	conn = connect(host = 'localhost', database = 'csv_db', user = 'root', password = '')
	mem = connect(host = 'localhost', database = 'members', user = 'root', password = '')

	
if __name__ == '__main__':
	application = QApplication([])
	second = Second()
	second.show()
	application.exec_()