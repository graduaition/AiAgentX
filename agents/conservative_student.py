from services.twitter_client import TwitterClient
from services.llm_client import LLMClient

class ConservativeStudent:
    def __init__(self, name, twitter_client, llm_client):
        self.name = name
        self.twitter_client = twitter_client
        self.llm_client = llm_client

    def respond_to_problem(self, tweet_id):
        response = self._generate_response()
        self.twitter_client.reply_to_tweet(tweet_id, response)

    def _generate_response(self):
        """Generates a conservative answer (private)."""
        ...
        return self.llm_client.generate_text(prompt)
