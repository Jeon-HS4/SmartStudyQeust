from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PageContentSerializer
import requests
from bs4 import BeautifulSoup
import logging
import openai

logger = logging.getLogger('test')


@api_view(['GET'])
def crawl_api(request):
    url = request.GET.get('url')

    if not url:
        return Response({'error': 'Please provide a valid URL parameter.'}, status=400)

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.get_text()

        serializer = PageContentSerializer(data={'url': url, 'content': content})
        serializer.is_valid()
                
        # return {'url': url, 'content': content}
        return Response(serializer.validated_data)


    except requests.exceptions.RequestException as e:
        logger.error(e)
        return Response({'error': 'Error occurred: ' + str(e)}, status=500)



def call_gpt_api(input_text, api_key):
    # GPT API 엔드포인트 URL
    openai.api_key = "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"
    api_url = "https://api.openai.com/v1/engines/davinci/completions"
    # api_keys = "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"

    # GPT API 요청 보내기
    messages = []
    input_message = "test message. repeat this message."
    messages.append({"role":"user", "content":input_message})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    chat = completion.choices[0].message.content
    # print(f'ChatGPT: {chat}')
    return completion

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"GPT API 요청 실패: {response.status_code} - {response.text}")



@api_view(['GET'])  # POST 요청으로 변경
def gpt_api(request):
    logger.error('api 호출 성공')
    try:
        #data = crawl_api(request)  # crawl_api를 호출하여 데이터를 받아옴
        # GPT 모델에 데이터를 전달하고 결과를 얻는 작업
        input_text = "아래 내용은 테스트로 입력된 내용이다. <성공했습니다> 라는 답변을 출력해줘."
        # input_text += data['content']  # 크롤링한 데이터를 GPT 모델의 입력으로 사용
        api_key = "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"  # 본인의 GPT API 키로 대체

        gpt_response = call_gpt_api(input_text, api_key)
        logger.error(gpt_response)

        # GPT 모델의 응답을 반환
        return Response({'gpt_response': gpt_response})

    except Exception as e:
            return Response({'error': 'Error occurred: ' + str(e)}, status=500)


# @api_view(['GET'])
# def crawl_api(request):
#     url = request.GET.get('url')

#     if not url:
#         return Response({'error': 'Please provide a valid URL parameter.'}, status=400)

#     try:
#         response = requests.get(url)
#         response.raise_for_status()

#         soup = BeautifulSoup(response.content, 'html.parser')
#         content = soup.get_text()

#         serializer = PageContentSerializer(data={'url': url, 'content': content})
#         serializer.is_valid()
                
#         return Response(serializer.validated_data)

#     except requests.exceptions.RequestException as e:
#         logger.error(e)
#         return Response({'error': 'Error occurred: ' + str(e)}, status=500)