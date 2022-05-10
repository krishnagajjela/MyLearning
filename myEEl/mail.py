import eel

eel.init('templates')

@eel.expose                         # Expose this function to Javascript
def button_handler_py(email, mpass):
    print("Javascript Email : {}".format(email))
    print("Javascript password {}".format(mpass))
    return "Py says thanks "

eel.start('home.html', size=(800, 800))    # Start
