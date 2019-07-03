
from watchdog.events import FileSystemEventHandler

from post import Post
from setup_ import POST_DAYS, POST_LIST, PASSWORD, USERNAME, DATES_OF_POSTS, DAYS_MAP
import os 
import json
import datetime
from datetime import timedelta  

path = '/Users/kalle/Documents/Projects/MyProjects/InstaAutomator/posts'
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        try:
            POST_LIST.initialize_me()
        except Exception as e:
            print 'no json'
        folder_path = '/Users/kalle/Documents/Projects/MyProjects/InstaAutomator/production_ready_posts'
        i = 1
        list_of_file_names = []
        for filename in os.listdir(path): 
            new_name = "post_" + str(i) + ".jpg"
            exists = True
            while exists:
                file_exists = os.path.isfile(folder_path+'/' + new_name)
                if file_exists:
                    DATES_OF_POSTS[new_name] = POST_LIST.posts[i-1]
                    i += 1
                    new_name = "post_" + str(i) + ".jpg"
                else:
                    exists = False

            new_name = folder_path + "/" + new_name
            src = path + "/" + filename 
          
            # rename() function will 
            # rename all the files 
            os.rename(src, new_name) 
            i += 1
            post_description = raw_input("Enter post description : ") 
            date_of_post = self.get_next_available_date()
            new_post = Post(post_description, new_name, date_of_post)
            DATES_OF_POSTS['post_' + str(i - 1) + ".jpg"] = new_post
            POST_LIST.posts.append(new_post)
            self.save_post(new_post)

    def save_post(self, post):
        with open('posts.json', 'w') as json_file:  
            json.dump(POST_LIST.serialize(), json_file)

    
    def get_next_available_date(self):
        return_date = datetime.date.today()
        print return_date.weekday()
        try:
            post = DATES_OF_POSTS['post_' + str(len(POST_LIST.posts)) + ".jpg"]
            return_date = post.post_date + timedelta(days=1)
        except Exception as e:
            print "exception"
        exists = True
        while exists:
            if DAYS_MAP[return_date.weekday()] not in POST_DAYS:
                return_date = return_date + timedelta(days=1) 
            else:
                exists = False
        
        return return_date
        
