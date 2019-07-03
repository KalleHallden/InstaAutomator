import json
from post import Post
from datetime import datetime
from dateutil import parser

class PostList:
    def __init__(self, posts):
        self.posts = posts
    
    def serialize(self):
        return {
            'posts' : self.get_json_posts(),
        }
    def get_json_posts(self):
        post_lists = []
        for post in self.posts:
            post_lists.append(post.serialize())
        
        return post_lists

    def initialize_me(self):
        post_list = PostList([])
        with open('posts.json', 'r') as f:
            data = json.load(f)
            post_list = PostList(
                posts = self.get_posts_from_json(data),
            )
        return post_list
        
    def get_posts_from_json(self, data):
        return_list = []
        for post in data['posts']:
            return_list.append(
                Post(
                    description = post['description'],
                    image = post['image'],
                    post_date = parser.parse(post['post_date'])
                )
            )
        self.posts = return_list
        return return_list
