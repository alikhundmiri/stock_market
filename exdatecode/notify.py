import os

def notify(title, text, subtitle):
    if subtitle:
        os.system("""
        osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "Hero"'
        """.format(title, subtitle, text))
    else:
        os.system("""
        osascript -e 'display notification "{}" with title "{}" sound name "Hero"'
        """.format(title, text))

if __name__ == '__main__':
	notify("Testing", "Sending a random message", "Mic Testing, 1 2 3...")