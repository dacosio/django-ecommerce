from store.models import Category

# the store.context_processors.categories is entered in template settings to make it visible project wide,
# instead of declaring it here on a specific template
def categories(request):
    return {
        'categories': Category.objects.all()
    }
