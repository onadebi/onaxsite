from datetime import datetime
from typing import Union

from blog.models.Posts import Posts;
from django.db.models import QuerySet;
from common.helpers.logger_service import LoggerService as Logger;


logger = Logger();

class PostRepository:
    def __init__(self):
        pass;
    
    def get_all(self):        
        """Returns list[ContactOptionsDao] of all active or None"""
        try:
            objResult: QuerySet[Posts] = Posts.objects.filter(is_active=True).values('id','post_title','post_content','created_at','updated_at','author','post_summary','slug','is_featured_post','post_image');
            all_posts = [
                {
                    'id' : int(item['id']),
                    'post_title' : str(item['post_title']),
                    'post_content' : str(item['post_content']),
                    'created_at' : datetime.strptime(str(item['created_at']), "%Y-%m-%d %H:%M:%S.%f%z"),
                    'updated_at' : datetime.strptime(str(item['updated_at']), "%Y-%m-%d %H:%M:%S.%f%z"),
                    'author' : str(item['author']),
                    # 'featured_image' : "700x350.png" if item['featured_image'] == "default_featured_image.jpg" else str(item['featured_image']),
                    'post_image' : "700x350.png" if item['post_image'] == "default_featured_image.jpg" else str(item['post_image']),
                    'post_summary' : str(item['post_summary']),
                    'slug' : str(item['slug']),
                    'is_featured_post' : bool(item['is_featured_post']),
                }
                for item in objResult
            ]
        except Exception as e:
            logger.log(f"Error in PostRepository.get_all: {str(e)}");
            all_posts = None;
        return all_posts;

    def get_featured_post(self) -> Union [Posts | None]:
        """Returns the featured post or None"""
        try:
            objResult: Posts = Posts.objects.filter(is_active=True, is_featured_post=True).values('id','post_title','post_content','created_at','updated_at','author','post_summary','slug','is_featured_post','post_image').last()
            featured_post = {
                    'id' : int(objResult['id']),
                    'post_title' : str(objResult['post_title']),
                    'post_content' : str(objResult['post_content']),
                    'created_at' : datetime.strptime(str(objResult['created_at']), "%Y-%m-%d %H:%M:%S.%f%z"),
                    'updated_at' : datetime.strptime(str(objResult['updated_at']), "%Y-%m-%d %H:%M:%S.%f%z"),
                    'author' : str(objResult['author']),
                    # 'featured_image' : "850x350.png" if objResult['featured_image'] == "default_featured_image.jpg" else str(objResult['featured_image']),
                     'post_image' : "700x350.png" if objResult['post_image'] == "default_featured_image.jpg" else str(objResult['post_image']),
                    'post_summary' : str(objResult['post_summary']),
                    'slug' : str(objResult['slug']),
                    'is_featured_post' : bool(objResult['is_featured_post']),
                }
        except Exception as e:
            logger.log(f"Error in PostRepository.get_featured_post: {str(e)}");
            featured_post = None;
        return featured_post;