"""
A very simple data class that is used to extract the information needed in the
calc_fib_indices.py script.
"""
from .utils import get_dict_val


class PostBase:
    """
    Base class for social media post.
    Classes for specific platforms can inherit it.
    It defines the common functions that the children classes should have.
    Should we want to update for V2, simply copy the Tweet_v1 class, create a
    Tweet_v2 class, and then update the functions.
    """

    def __init__(self, post_object):
        """
        This function initializes the instance by binding the post_object
        Parameters:
            - post_object (dict): the JSON object of the social media post
        """
        if post_object is None:
            raise ValueError("The post object cannot be None")
        self.post_object = post_object

    def is_valid(self):
        """
        Check if the data is valid
        """
        raise NotImplementedError

    def get_value(self, key_list: list = []):
        """
        This is the same as the midterm.get_dict_val() function
        Return `dictionary` value at the end of the key path provided
        in `key_list`.
        Indicate what value to return based on the key_list provided.
        For example, from left to right, each string in the key_list
        indicates another nested level further down in the dictionary.
        If no value is present, a `None` is returned.
        Parameters:
        ----------
        - dictionary (dict) : the dictionary object to traverse
        - key_list (list) : list of strings indicating what dict_obj
            item to retrieve
        Returns:
        ----------
        - key value (if present) or None (if not present)
        """
        return get_dict_val(self.post_object, key_list)

    def get_rt_count(self):
        """
        Return the retweet count from this status object
        """
        return NotImplementedError

    def get_post_ID(self):
        """
        Return the ID of the post as a string
        """
        raise NotImplementedError

    def get_link_to_post(self):
        """
        Return the link to the post so that one can click it and check
        the post in a web browser
        """
        raise NotImplementedError

    def get_retweeted_post_ID(self):
        """
        Return the post ID from the retweeted_status, if present.
        Otherwise, return None.
        """
        raise NotImplementedError

    def get_user_ID(self):
        """
        Return the ID of the user as a string
        """
        raise NotImplementedError

    def get_retweeted_user_ID(self):
        """
        Return the user ID from the retweeted_status, if present.
        Otherwise, return None.
        """
        raise NotImplementedError

    def get_user_sreenname(self):
        """
        Return the screen_name of the user (str)
        """
        return NotImplementedError

    def get_retweeted_user_sreenname(self):
        """
        Return the screen_name (str) of the user in the retweeted_status
        """
        return NotImplementedError

    def __repr__(self):
        """
        Define the representation of the object.
        """
        return f"<{self.__class__.__name__}() object>"


class Tweet_v1(PostBase):
    """
    Class to handle tweet object (V1 API)
    """

    def __init__(self, tweet_object):
        """
        This function initializes the instance by binding the tweet_object
        Parameters:
            - tweet_object (dict): the JSON object of a tweet
        """
        super().__init__(tweet_object)

        self.is_retweet = "retweeted_status" in self.post_object
        if self.is_retweet:
            self.retweet_object = Tweet_v1(self.post_object["retweeted_status"])

        self.is_quote = "quoted_status" in self.post_object
        if self.is_quote:
            self.quote_object = Tweet_v1(self.post_object["quoted_status"])

    def is_valid(self):
        """
        Check if the tweet object is valid.
        A valid tweet should at least have the following attributes:
            [id_str, user, text, created_at]
        """
        attributes_to_check = ["id_str", "user", "text", "created_at"]
        for attribute in attributes_to_check:
            if attribute not in self.post_object:
                return False
        return True

    def get_rt_count(self):
        """
        Return the retweet count from this status object
        """
        return self.get_value(["retweet_count"])

    def get_post_ID(self):
        """
        Return the ID of the tweet (str)
        This is different from the id of the retweeted tweet or
        quoted tweet
        """
        return self.get_value(["id_str"])

    def get_link_to_post(self):
        """
        Return the link to the tweet (str)
        so that one can click it and check the tweet in a web browser
        """
        return f"https://twitter.com/{self.get_user_sreenname()}/status/{self.get_post_ID()}"

    def get_retweeted_post_ID(self):
        """
        Return the post ID from the retweeted_status, if present.
        Otherwise, return None.
        """
        if self.is_retweet:
            return self.retweet_object.get_post_ID()
        return None

    def get_user_ID(self):
        """
        Return the ID of the base-level user (str)
        """
        return self.get_value(["user", "id_str"])

    def get_retweeted_user_ID(self):
        """
        Return the user ID from the retweeted_status, if present.
        Otherwise, return None.
        """
        if self.is_retweet:
            return self.retweet_object.get_user_ID()
        return None

    def get_user_sreenname(self):
        """
        Return the screen_name of the user (str)
        """
        return self.get_value(["user", "screen_name"])

    def get_retweeted_user_sreenname(self):
        """
        Return the screen_name (str) of the user in the retweeted_status
        """
        if self.is_retweet:
            return self.retweet_object.get_user_sreenname()
        return None

    def __repr__(self):
        """
        Define the representation of the object.
        """
        return "".join(
            [
                f"{self.__class__.__name__} object from @{self.get_user_sreenname()}\n",
                f"Link: {self.get_link_to_post()}",
            ]
        )
