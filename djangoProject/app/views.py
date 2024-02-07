from django.shortcuts import render
from django.http import JsonResponse
from elasticsearch_dsl import *
from elasticsearch_dsl.query import *

connections.create_connection(hosts=['localhost'])

def search_query(search,query,columns):
    s=search.query(query)
    response=s.execute()

    for hit in response.hits:
        for col in columns:
            print(f'{col} : {hit.to_dict().get(col)}')



def law_query(request):
    if request.method == 'POST':
        law_number = request.POST.get('law_number', '')
        law_content = request.POST.get('law_content','')
        search = Search(index='law')
        if law_content:
            query= Match(content=law_content)
        else:
            query = Match(num=law_number)
        response = search.query(query).execute()
        results=response.hits
        print(results)
        return render(request, 'law_result.html',{'laws':results})
    return render(request, 'law_query.html')



