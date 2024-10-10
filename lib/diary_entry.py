class DiaryEntry:

    def __init__(self, title, contents): 
        self.title = title
        self.contents = contents
        self.chunk = 0

    def count_words(self):
        text = self.contents
        contents_list = str(text).split()
        return len(contents_list)

    def reading_time(self, wpm):
        number_of_words = self.count_words()
        reading_time = number_of_words / wpm
        return reading_time


    def reading_chunk(self, wpm, minutes):
        words_to_read = wpm * minutes
        contents = str(self.contents).split()
        result = ""
        for entry in contents[self.chunk:words_to_read + self.chunk]:
            result += f"{entry} "
        self.chunk += words_to_read
        return result.strip()
