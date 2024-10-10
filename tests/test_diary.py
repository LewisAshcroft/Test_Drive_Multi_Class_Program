from lib.diary import *
from lib.diary_entry import *

#Diary tests

def test_init():
    diaryfunction = Diary()
    result = diaryfunction.entrylist
    assert isinstance(result,list)

def test_add():
    diaryfunction = Diary()
    entry = DiaryEntry("Title", "This is not an integer but it is a string")
    diaryfunction.add(entry)
    assert len(diaryfunction.entrylist) == 1
    assert diaryfunction.entrylist[0] == entry

def test_all():
    diaryfunction = Diary()
    diaryentry = DiaryEntry("Title","This is not an integer but it is a string")
    diaryfunction.add()
    result = diaryfunction.all()
    assert result == ["Title","This is not an integer but it is a string"]

def test_count_words():
    #Tests to ensure the correct value is calculated
    pass

def test_reading_time():
    #Tests if method returns correct value
    pass

def test_best_entry():
    #Tests if method returns correct value
    pass