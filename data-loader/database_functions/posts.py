import logging
from flask import Flask
from library import backend_util
logger = logging.getLogger(__name__)

app = Flask(__name__)
def add_posts(post_id, user_id, platform, timestamp, url):
    logger.info("Add post data")
    with backend_util.get_db_cursor() as cur:
        try:
            add_post = "INSERT INTO posts (post_id, user_id, platform, timestamp, url) values (%s,%s, %s, %s, %s) RETURNING post_id"
            cur.execute(add_post, (post_id, user_id, platform, timestamp, url))
            if cur.rowcount > 0:
                post_fetch_id = cur.fetchone()[0]
                result = {"post_id" : post_fetch_id}
                logger.info("Successfully created post row!")
            else:
                logger.error("There was a a problem in creating the post!")
            return result
        except Exception as ex:
            print("Error in adding data :", ex)

def get_all_posts():
    logger.info("Get all posts data")
    all_posts = []
    with backend_util.get_db_cursor() as cur:
        select_query = ("SELECT id, post_id, user_id, platform, timestamp, url from posts;")
        cur.execute(select_query)
        if cur.rowcount > 0:
            all_post_details = cur.fetchall()
            for post in all_post_details:
                post_json = {"id": post[0],
                             "post_id" : post[1],
                             "user_id" : post[2],
                             "platform" : post[3],
                             "timestamp" : post[4],
                             "url": post[5]
                             }
                all_posts.append(post_json)
                logger.info("Succesfully retrived all posts")
        else:
            logger.info("There is no posts to fetch!")
    return all_posts