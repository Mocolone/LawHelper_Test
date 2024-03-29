import json

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
        fact_content = request.POST.get('fact_content','')
        search = Search(index='law')
        query = Match(num=law_number)
        if law_content:
            search = Search(index='law')
            query= Match(content=law_content)
        if law_number:
            search = Search(index='law')
            query = Match(num=law_number)
        if fact_content:
            search = Search(index='fact')
            query=Match(fact=fact_content)
        response = search.query(query).execute()
        results=response.hits
        print(results)
        return render(request, 'law_result.html',{'results':results})
    return render(request, 'law_query.html')

def getLawByNum(request):
    if request.method=="POST":
        request_data = json.loads(request.body)
        lawNum = request_data.get("lawNum")
        search = Search(index='law')
        lawList=[]
        if lawNum:
            for i in range(int(lawNum), int(lawNum) + 10):
                query = Match(num=i)
                response = search.query(query).execute()
                results = response.hits
                print(results)
                tmp={'num':results[0].num,'content':results[0].content}
                lawList.append(tmp)
            response = JsonResponse({'law':json.dumps(lawList)})
            response['Access-Control-Allow-Origin'] = '*'
            return response
        else:
            response = JsonResponse({'error':'错误'})
            response['Access-Control-Allow-Origin'] = '*'
            return response

def getLawByContent(request):
    if request.method=="POST":
        request_data = json.loads(request.body)
        lawContent = request_data.get("lawContent")
        search = Search(index='law')
        lawList=[]
        if lawContent:
            query = Match(content=lawContent)
            response = search.query(query).execute()
            results = response.hits
            if results:
                for result in results:
                    tmp = {'num': result.num, 'content': result.content}
                    lawList.append(tmp)
                response = JsonResponse({'law': json.dumps(lawList)})
                response['Access-Control-Allow-Origin'] = '*'
                return response
            else:
                response = JsonResponse({'error': "未找到相关法条"})
                response['Access-Control-Allow-Origin'] = '*'
                return response
        else:
            response = JsonResponse({'error':'错误'})
            response['Access-Control-Allow-Origin'] = '*'
            return response



