from ..models import Comment

def fetch_comments_count(posts):
  comments_dict={}
  if posts:
    for post in posts:
      comments_count=len(Comment.query.filter_by(post=post).all())
      comments_dict[post.id]=comments_count

    return comments_dict

  else:
     return None