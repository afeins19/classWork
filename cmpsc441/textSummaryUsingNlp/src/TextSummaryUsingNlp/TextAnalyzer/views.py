from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import TextInputForm
from Helper import Helper
import PyPDF2
analysis = Helper()


# Create your views here.
def index(request):
    return HttpResponse("Hello World!")


def home(request):
    if request.method =='POST':
        form = TextInputForm(request.POST, request.FILES)

        if form.is_valid():
            if 'text' in request.POST and request.POST['text']:
                raw_text = form.cleaned_data['text']
            else:
                upload_file = request.FILES.get('upload_file')
                if upload_file:
                    raw_text = extract_text_from_pdf(upload_file)

            # Perform text analysis using your Helper class
            summary = analysis.summarize_texts([raw_text])  # Pass a list containing the raw_text
            sentiment_result = analysis.find_sentiment([raw_text])
            emotion_result = analysis.get_emotions_detected([raw_text])  # Pass a list containing the raw_text

            analyzed_data = {
                'raw_text': raw_text,
                'summary': summary,
                'sentiment_result': sentiment_result,
                'emotion_result': emotion_result,
            }

            return render(request, 'TextAnalyzer/result.html', analyzed_data)

    else:
        initial_text_value = ("Enter text here or upload a pdf file. Must be 512 characters or less. "
                              "Delete this text before uploading a file.")  # Set your desired initial value
        form = TextInputForm(initial={'text': initial_text_value})

    return render(request, 'TextAnalyzer/home.html', {'form': form})


def about(request):
    return render(request, 'TextAnalyzer/about.html')


def extract_text_from_pdf(pdf_file):
    with pdf_file.open('rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        text = ''
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()

    if len(text) > 512:
        shortened_text = ""
        for num in range(512):
            shortened_text += text[num]
        return shortened_text

    return text
