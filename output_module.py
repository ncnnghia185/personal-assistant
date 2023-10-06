import assistant_detail
from speech_module import speak
from database import speak_is_on


def output(o):
    if speak_is_on():
        speak(o)
    if o is not None:
        print(assistant_detail.name + " : " + str(o))
    else:
        print(assistant_detail.name + " : None")
    print()
