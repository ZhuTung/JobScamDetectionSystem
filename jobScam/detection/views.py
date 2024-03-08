from django.shortcuts import render
from .nlp import *
from .comm_pattern import *

# Create your views here.
def detection(request):

    result = 2
    
    if request.method == 'POST':
        title = request.POST['title']
        location = request.POST['location']
        com_profile = request.POST['com_profile']
        desc = format_textarea(request.POST['desc'])
        req = request.POST['req']
        benefits = request.POST['benefits']

        text = title + ' ' + location + ' ' + com_profile + ' ' + desc + ' ' + req + ' ' + benefits
        text = [process_text(text)]

        analysis_invoker = TextAnalysisInvoker()

        # User selects a command
        command = PredictCommand()

        analysis_invoker.set_command(command)
        analysis_invoker.execute_analysis(text)
        result = command.get_result()

        return render(request, "detection/detect.html", {"result":result})

    return render(request, "detection/detect.html")