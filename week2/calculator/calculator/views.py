from django.shortcuts import render


def main(request):
    return render(request, 'calculator/main.html')


def mycalculator(request):

    cal = request.GET['cal']

    return render(request, 'calculator/mycalculator.html', {'calcul': eval(cal)})
