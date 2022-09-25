from datetime import datetime

def sample_responses(input_text):
    user_message=str(input_text).lower()

    if user_message in ("hello","hi","hola","hey","hii"):
        return "Hey! How is it going..??"

    if user_message in ("who are you","what are you","who","what","why"):
        return "I am IIITL's Bot"

    if user_message in ("time","time?"):
        now=datetime.now()
        date_time=now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    else:
        return "Bolna kya chahte ho bhayyy.."

