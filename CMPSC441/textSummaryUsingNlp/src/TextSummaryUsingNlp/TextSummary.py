from transformers import BartForConditionalGeneration, BartTokenizer


class TextSummary:
    def summarize_text_bart(self, text, model_name="facebook/bart-large-cnn"):
        model = BartForConditionalGeneration.from_pretrained(model_name)
        tokenizer = BartTokenizer.from_pretrained(model_name)
        inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs, max_length=150, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

