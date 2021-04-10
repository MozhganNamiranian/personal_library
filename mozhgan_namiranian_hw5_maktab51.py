
class Book():

    def __init__(self,title,author,publish_year,pages,language,price,allread_pages=0):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages= pages
        self.language = language
        self.price = price
        self.allread_pages = allread_pages
        """allread_pages is number of pages that reader has read until now and it's initial value zero.."""


    def read(self,read_pages):

        self.allread_pages+=read_pages
        if int(self.allread_pages)<int(self.pages):
            print (f' you have read {int(read_pages)} more pages from {self.title}.\
         There are {int(self.pages)-int(self.allread_pages)} pages left')
            progress = (int(self.allread_pages)/int(self.pages))*100
            print ('progress is:%' ,progress)

        elif self.allread_pages==self.pages:
            print ("Well done! You've finished the book")
        else:
            print ('you can not read more than book’s pages')
        return self.allread_pages

    def get_status(self):
        if self.allread_pages == 0:
            status = 'unread'
        elif 0 <int (self.allread_pages) <int(self.pages):
            status = 'reading'
        else:
            status = 'finished!'
        print (f'status is: {status}')

        return status
    def __str__(self):
        return f' title: {self.title},' \
               f' author: {self.author}, publish_year:{self.publish_year},' \
               f' pages:{self.pages}, language: {self.language},'  \
               f' price: {self.price}, read pages till now: {self.allread_pages}'


class Magazine(Book):
    def __init__(self,title,author,publish_year,pages,language,price,issue,allread_pages=0):
        super().__init__(title,author,publish_year,pages,language,price,allread_pages=0)
        self.issue = issue
    def __str__(self):
        st = super(Magazine,self).__str__()
        st += f ('issue: {self.issue}')
        return st

class Podcast_episode():
    def __init__(self,title,speaker,publish_year,time,language,price,all_listened=0):
        """similar to Book class, we set the initial value of all_listened to zero"""
        self.title=title
        self.speaker=speaker
        self.publish_year=publish_year
        self.time=time
        self.language=language
        self.price=price
        self.all_listened=all_listened

    def listen(self,listened):
        """similar to read method in Book class"""
        self.all_listened+=listened
        return self.all_listened
        if self.all_listened<self.time:
            print (f' you have listened {int(listened)} more minutees from {self.title}.\
         There are {int(self.time)-int(self.all_listened)} minutes left')
            progress = (int(self.all_listened)/int(self.time))*100
            print ('progress is:%' ,progress)

        elif self.all_listened==self.time:
            print ("Well done! You've finished the podcast episode")
        else:
            print ('you can not listen more than podcast time')
        return self.all_listened

    def podcast_get_status(self):
        if self.all_listened == 0:
            status = 'not listened'
        elif 0 <int (self.all_listened) <int(self.time):
            status = 'listening'
        else:
            status = 'finished!'
        print (f'status is: {status}')


class Audiobook(Book,Podcast_episode):
    def __init__(self,title,speaker,author,publish_year,pages,book_language,audio_language,time,price):
        Book.__init__(title,author,publish_year,pages,language,price)
        Podcast_episode.__init__(self,title,speaker,publish_year,time,language,price)
        self.audio_language=audio_language

    def audiobook_get_status(self):
        super(Audiobook, self).get_status()
        super(Audiobook, self).podcast_get_status()


    def __str__(self):
        st = super().__str__()
        st += f ('speaker: {self.speaker}, duration: {self.time}, language: {self.audio_language}')
        return st

def main():
      """we should define a shelf in the format of an empty list for each media type"""
      listofbooks = []
      listofmagazines = []
      listofpodcasts = []
      listofaudiobooks = []
      finish = str('')

      while finish != str ('Quit'):
        userinput = input ('please choose the number of your preferred media type: \n1.book 2.magazine 3.audiobook 4.podcast ')
        title = input(f'please enter title: ')
        publish_year = input('please enter publish_year: ')
        language = input('please enter language: ')
        price = input('please enter price: ')
        author = input('please enter author name: ')

        if userinput =='1' or userinput =='2' or userinput =='3' :
            pages = int (input('please enter number of pages: '))
            if userinput==2:
                issue = input('please enter issue: ')
                """we create an object or instance"""
                listofmagazines.append(Magazine(title,author, publish_year, pages,language, price, issue))

            elif userinput == 3:
                speaker = input(f'please enter speaker:')
                time = int(input(f'please enter duration:'))
                language= input(f'please enter audio language:')

                listofaudiobooks.append(AudioBook(title, speaker, authors, publish_year, pages, time, language, audio_language, price))
            else:
                listofbooks.append(Book(title,author,publish_year,pages,language,price))

        elif userinput == 4:
            speaker = input('please enter speaker :')
            time = input('please enter duration :')
            listofpodcasts.append(Podcast_episode(title, speaker, publish_year, time, language, price))
            finish = input('write "Quit" if you want to leave or press other keys to continue:')
        finish = input('write "Quit" if you want to leave or press other keys to continue:')
      libdict = {'book':  listofbooks, 'magazine': listofmagazines, 'podcast': listofpodcasts, 'audiobook': listofaudiobooks}
      shelf = listofbooks+listofmagazines+listofpodcasts+listofaudiobooks
      for i in shelf:
        print(i)
      #shelf.sort(key=lambda x: x.progress, reverse=True)

      return libdict


bookshelf=main()
book = Book('No Friend But the Mountains', 'Behrouz Boochani', '2018', '374', 'english', '10')
book.read(100)
book.get_status()

