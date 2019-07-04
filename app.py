from instapy_cli import client
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from post import Post
from setup_ import POST_DAYS, POST_LIST, PASSWORD, USERNAME, POST_HOUR 
import os 
import json
from eventhandler import MyHandler
from datetime import datetime
import tkinter as tk
from alert_window import AlertWindow

path = '/Users/kalle/Documents/Projects/MyProjects/InstaAutomator/posts'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        try:
            POST_LIST.initialize_me()
        except Exception as e:
            print('no json')
        for post in POST_LIST.posts:
            todays_date = datetime.today()
            if post.description == "":
                root = tk.Tk()
                app = AlertWindow(root, post.image)
                root.mainloop()
                post.description = app.new_description
                with open('posts.json', 'w') as json_file:  
                        json.dump(POST_LIST.serialize(), json_file)
            if todays_date.day == post.post_date.day:
                if todays_date.hour == POST_HOUR:
                    # should post a photo
                    if not post.has_been_posted: 
                        with client(USERNAME, PASSWORD) as cli:
                            cli.upload("production_ready_posts/" + post.image, post.description)
                            post.has_been_posted = True
                    with open('posts.json', 'w') as json_file:  
                        json.dump(POST_LIST.serialize(), json_file)
                    
        time.sleep(60)
except KeyboardInterrupt:
    observer.stop()
observer.join()


# username = 'kallehallden'
# password = 'kallehalldenyes'
# image = 'posts/post1.png'
# text = 'Hello tester'


