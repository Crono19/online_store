from online_store.models import Category

def category_list(request):
    categories = Category.objects.all()
    return {'categories': categories}