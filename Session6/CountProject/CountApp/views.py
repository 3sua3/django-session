from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    blank_exp_total_len = len(text.replace(" ", ""))
    total_word = len(text.split())
    return render(request, 'result.html', {'total_len': total_len, 'text': text,'blank_exp_total_len': blank_exp_total_len, 'total_word': total_word})  