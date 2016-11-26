from django.shortcuts import render


from .quik_sort import parallel_quik_sort


def index(request):
	return render(request,'index.html')

def sort_it(request):
	array = request.POST['array']
	array = [int(num) for num in array.split()]
	parallel_quik_sort(array)
	return render(request, 'sorted.html', {'array': array})