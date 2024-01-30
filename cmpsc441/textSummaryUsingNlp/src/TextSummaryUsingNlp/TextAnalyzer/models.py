from django.db import models

# constants
MAX_TWEET_LENGTH = 280

# Create your models here
class RawTextDataModel(models.Model):
    """Holds the raw text that the user would like to analyze"""
    raw_text = models.CharField(max_length = MAX_TWEET_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.raw_text[:50])

class EmotionalAnalysisModel(models.Model):
    """Holds Raw Text that this function was invoked with and emotional classification details"""
    raw_text = models.OneToOneField(RawTextDataModel, on_delete=models.CASCADE)
    emotion_category = models.CharField(max_length=50)
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.emotion_category)

class SentimentAnalysisModel(models.Model):
    """Holds Raw text that this function was invoked for and sentiment analysis data (score)"""
    raw_text = models.OneToOneField(RawTextDataModel, on_delete=models.CASCADE)
    sentiment_score = models.FloatField()
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sentiment_score)
