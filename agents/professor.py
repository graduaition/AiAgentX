from services.twitter_client import TwitterClient
from services.llm_client import LLMClient

class Professor:
    def __init__(self, name, twitter_client, llm_client):
        self.name = name
        self.twitter_client = twitter_client
        self.llm_client = llm_client
        self.last_tweet_id = None

    def pose_problem(self):
        """Posts a problem on X."""
        problem = self._generate_problem()
        self.last_tweet_id = self.twitter_client.post_tweet(f"Problème du jour : {problem}")
        return self.last_tweet_id

    def evaluate_responses(self):
        """Evaluates students answers."""
        evaluation = self._generate_evaluation()
        self.twitter_client.post_tweet(f"Evaluate answers : {evaluation}", in_reply_to_status_id=self.last_tweet_id)

    def _generate_problem(self):
        """Generates a problem thanks to Claude (private)"""
        ...
        return self.llm_client.generate_text(prompt)

    def _generate_evaluation(self):
        """Generates an evaluation of responses (private)."""
        ...
        return self.llm_client.generate_text(prompt)
