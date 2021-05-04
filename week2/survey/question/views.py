from django.shortcuts import render
from survey.models import survey, answer


def home(request):
    survey = Survey.objects.filter(status="y").order_by('-survey_idx')[0]
    return render(request, 'question/home.html', {'survey': survey})


def save_survey(request):
    survey_idx = request.POST["survey_idx"]
    # answer 값 가져와서
    dto = Answer(survey_idx=int(
        request.POST["survey_idx"]), ans=request.POST["num"])
    dto.save()
    return render(request, "question/success.html")


def show_result(request, question_id):
    result = Answer.objects.filter(survey_idx=question_id)
    return render(request, "question/result.html", {'result': result})
