from django.shortcuts import render


from .quik_sort import quik_sort as qqsort


def index(request):
	return render(request,'index.html')

def sort_it(request):
	array = request.POST['array']
	array = [int(num) for num in array.split()]
	qqsort(array)
	return render(request, 'sorted.html', {'array': array})