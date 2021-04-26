from django.shortcuts import render


# Create your views here.


def main(request):
    return render(request, "calculator/main.html", )

def calculator(request):
    formula = request.GET['formula']
    try:
        result = eval(formula)
    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        result = "유효한 계산을 입력하세요"
    return render(request, "calculator/calculator.html", {'result':result})
