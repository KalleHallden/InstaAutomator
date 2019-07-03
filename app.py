from instapy_cli import client
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from post import Post
from setup_ import POST_DAYS, POST_LIST, PASSWORD, USERNAME
import os 
from eventhandler import MyHandler

path = '/Users/kalle/Documents/Projects/MyProjects/InstaAutomator/posts'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

# username = 'kallehallden'
# password = 'kallehalldenyes'
# image = 'posts/post1.png'
# text = 'Hello tester'

# with client(USERNAME, PASSWORD) as cli:
#     cli.upload(image, text)

