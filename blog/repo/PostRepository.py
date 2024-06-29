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
            objResult: QuerySet[Posts] = Posts.objects.filter(is_active=True).values('id','post_title','post_content','created_at','updated_at','author','featured_image');
            all_posts = [
                {
                    'id' : f"{item['id']}",
                    'post_title' : f"{item['post_title']}",
                    'post_content' : f"{item['post_content']}",
                    'created_at' : f"{item['created_at']}",
                    'updated_at' : f"{item['updated_at']}",
                    'author' : f"{item['author']}",
                    'featured_image' : f"{item['featured_image']}",
                }
                for item in objResult
            ]
        except Exception as e:
            logger.log(f"Error in PostRepository.get_all: {str(e)}");
            all_posts = None;
        return all_posts;