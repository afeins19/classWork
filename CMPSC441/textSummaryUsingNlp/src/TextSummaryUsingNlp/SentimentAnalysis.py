from transformers import pipeline


class SentimentAnalysis:
    def calc_sentiment(self, texts):
        sentiment_pipeline = pipeline("sentiment-analysis")
        total_score = 0
        total_labels = {'POSITIVE': 0, 'NEGATIVE': 0, 'NEUTRAL': 0}

        for text in texts:
            result = sentiment_pipeline(text)[0]
            sentiment_score = result['score']
            sentiment_label = result['label']

            total_score += sentiment_score
            total_labels[sentiment_label] += 1

        average_score = total_score / len(texts)

        if total_labels['POSITIVE'] > total_labels['NEGATIVE']:
            overall_sentiment = 'positive'
        elif total_labels['NEGATIVE'] > total_labels['POSITIVE']:
            overall_sentiment = 'negative'
        else:
            overall_sentiment = 'neutral'

        return (overall_sentiment, average_score)