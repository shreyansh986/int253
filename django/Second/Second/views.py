from django.http import HttpResponse


def home(request):
    return HttpResponse("<h2>Hello</h2>")


def user1(request):
    name = request.GET.get("name", "User")
    return HttpResponse(f"Hello, {name}")


def user2(request, id):
    return HttpResponse(f"Hello, {id}")


def list1(request):
    my_list = ["Raman", "Aman", "Shreyansh", "Neetu"]
    return HttpResponse(str(my_list))


def set1(request):
    my_set = {"Raman", "Aman", "Shreyansh", "Neetu"}
    return HttpResponse(str(my_set))


def dict1(request):
    my_dict = {
        "Raman": 21,
        "Aman": 22,
        "Shreyansh": 23,
        "Neetu": 24,
    }
    return HttpResponse(str(my_dict))


def tuple1(request):
    my_tuple = ("Raman", "Aman", "Shreyansh", "neetu")
    return HttpResponse(str(my_tuple))
