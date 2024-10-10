from lib.diary_entry import *

def test_init():
    diaryentryfunction = DiaryEntry("Title","This is a String")
    result1 = diaryentryfunction.title
    result2 = diaryentryfunction.contents
    assert isinstance(result1,str) and isinstance(result2,str)
    

def test_count_words():
    diaryentryfunction = DiaryEntry("Title","This is a String")
    result1 = diaryentryfunction.count_words()
    assert result1 == 4

def test_reading_time():
    diaryentryfunction = DiaryEntry("Title", "This is not a String")
    result = diaryentryfunction.reading_time(5)
    assert result == 1

def test_reading_chunk():
    diaryentryfunction = DiaryEntry("Title", "This is not an integer but it is a string")
    result1 = diaryentryfunction.reading_chunk(5,1)
    assert result1 == "This is not an integer"
    result2 = diaryentryfunction.reading_chunk(5,1)
    assert result2 == "but it is a string"