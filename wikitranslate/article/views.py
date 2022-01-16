from django.shortcuts import render, get_object_or_404
from .models import Project, Sentence
from wikipediaapi import Wikipedia
from nltk import tokenize
  

def index(request):
    project_list = Project.objects.all()
    wiki = Wikipedia('en')
    context = {
        'project_list': project_list,
    }
    if request.method == "POST":
        result = ''
        search_article = request.POST['article_name']
        try:
            result = wiki.page(search_article).summary[:]
        except:
            result = 'Wrong Input. Try Again.'
        if result:
            new_project = Project.objects.create(wiki_title = search_article, target_lang = request.POST['lang'])
            new_project.save()
            sentences = tokenize.sent_tokenize(result)
            for sentence in sentences:
                new_sen = Sentence.objects.create(project_id = new_project, original_sentence = sentence)
                new_sen.save()
        context = {
        'project_list': project_list,
        'result': result,
        }
        return render(request,"article/index.html",context)
    return render(request, 'article/index.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        sentences = []
        sentences = Sentence.objects.filter(project_id = project)
        for sentence in sentences:
            print(sentence.pk)
            sentence.translated_sentence = request.POST[str(sentence.pk)]
            # sentence.translated_sentence = 'hi'
            sentence.save()
    return render(request, 'article/detail.html', {'project': project})
