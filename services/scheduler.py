import schedule
import time
from professor import Professor
from conservative_student import ConservativeStudent
from progressive_student import ProgressiveStudent
from neutral_student import NeutralStudent
from services.twitter_client import TwitterClient
from services.llm_client import LLMClient

def run_experiment():
    # Clients initialisation
    twitter_client = TwitterClient(
        api_key="API_KEY",
        api_secret_key="API_SECRET_KEY",
        access_token="ACCESS_TOKEN",
        access_token_secret="ACCESS_TOKEN_SECRET"
    )
    llm_claude = LLMClient("claude", "API_KEY_CLAUDE")
    llm_grok = LLMClient("grok", "API_KEY_GROK")
    llm_gemini = LLMClient("gemini", "API_KEY_GEMINI")
    llm_chatgpt = LLMClient("chatgpt", "API_KEY_CHATGPT")

    # Agents initialisation
    professor = Professor("Machi", twitter_client, llm_claude)
    conservative_student = ConservativeStudent("Neslear", twitter_client, llm_grok)
    progressive_student = ProgressiveStudent("Lessly", twitter_client, llm_gemini)
    neutral_student = NeutralStudent("Nend", twitter_client, llm_chatgpt)

    def process():
        # Machi posts a problem
        tweet_id = professor.pose_problem()

        # Students answer 10 minutes later
        time.sleep(600)  # 10 minutes
        conservative_student.respond_to_problem(tweet_id)
        progressive_student.respond_to_problem(tweet_id)
        neutral_student.respond_to_problem(tweet_id)

        # Machi evaluates answers 10 minutes later
        time.sleep(600)  # 10 minutes
        professor.evaluate_responses()

    process()  # First execution
    schedule.every().hour.do(process)  # Repetition every hour

    while True:
        schedule.run_pending()
        time.sleep(1)
