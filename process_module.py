from output_module import output
from input_module import take_input
from database import *
from time_module import get_time, get_date
from internet_connect import check_internet_connection, check_on_wikipedia
import assistant_detail
from open_web import open_facebook, open_google, close_browser
from displaybg import change_wallpaper
from new import get_new
def process(query):
    answer = get_answer_from_QandA(query)

    # Answer the time
    if answer == "get time details":
        return "It is " + get_time()

    # Answer the internet connection
    elif answer == "check internet connection":
        if check_internet_connection():
            return "Internet Access"
        else:
            return "No Internet Access"

    # Answer change name
    elif answer == "change your name":
        output("What do you want to call me")
        temp = take_input()
        if temp == assistant_detail.name:
            return "This is my current name!"
        else:
            update_name(temp)
            assistant_detail.name = temp
            return "Now you can call me " + temp

    # Answer the date
    elif answer == "tell the date":
        return "The date is " + get_date()

    # Answer speak
    elif answer == "speak":
        return turn_on_speech()
    elif answer == "no speak":
        return turn_off_speech()

    #Answer open web
    elif answer == "open facebook":
        open_facebook()
        return "Opening Facebook"
    elif answer == "open browser":
        open_google()
        return "Opening Browser"
    elif answer == "close browser":
        return "Closing browser"

    #Answer change wallpaper
    elif answer == "change wallpaper":
        return change_wallpaper()
    #Answer get news
    elif answer == "get news":
        get_new()
    # Add question and answer
    else:
        # Answer from Wikipedia
        output("Do you want this information in Wikipedia")
        ans = take_input()
        if "yes" in ans:
            answer = check_on_wikipedia(query)
            if answer != "":
                return answer
        output("I don't know this , can you tell me what is this?")
        ans = take_input()
        if "it means" in ans.lower():
            ans = ans.replace("it means", "")
            ans = ans.strip()
            value = get_answer_from_QandA(ans)
            if value == "":
                return "Sorry , i can't help you"
            else:
                insert_q_and_a(query, value)
                return "Thanks , i will remember it"
        return "No information found"
