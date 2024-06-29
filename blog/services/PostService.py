from blog.repo.PostRepository import PostRepository
from common.helpers.logger_service import LoggerService as Logger;


logger = Logger();

class PostService:
    '''Service class for Posts operations'''
    def __init__(self):
        self.post_repository = PostRepository();

    def get_all(self):
        return self.post_repository.get_all()

    # def get_by_id(self, id):
    #     return self.post_repository.get_by_id(id)

    # def create(self, post):
    #     return self.post_repository.create(post)

    # def update(self, id, post):
    #     return self.post_repository.update(id, post)

    # def delete(self, id):
    #     return self.post_repository.delete(id)