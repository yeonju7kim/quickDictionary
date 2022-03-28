from excel import save_excel
from gui import ask_word, show_word, ok_no_msgbox

while(1):
    word, dictionary = ask_word()
    summary = show_word(word, dictionary)
    save_excel(word, summary)
    if ok_no_msgbox("will you continue?") == False:
        break