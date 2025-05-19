print("네이버 맛집")


# blog.py에서 함수 만들어서 모듈 포함시켜서 활용 
# 여기에서 메인 프로그램 작성
# 맛집 검색: 
# 맛집을 입력 하면 
# 결과가 나오는 프로그램 만들기  

# naver_blog_search.py
import urllib.request
import urllib.parse
import json

# 네이버 API 인증 정보
client_id = "WBfYyw5c3TVgmf7c833y"
client_secret = "cOOr830V1X"

def search_blog(query):
    encText = urllib.parse.quote(query)
    url = f"https://blog.naver.com/okok772/223372103761={encText}"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if rescode == 200:
            response_body = response.read()
            json_data = response_body.decode('utf-8')
            data = json.loads(json_data)

            extracted_list = []
            for item in data['items']:
                extracted_item = {
                    "title": item.get("title", ""),
                    "link": item.get("link", ""),
                    "description": item.get("description", ""),
                    "bloggername": item.get("bloggername", ""),
                    "postdate": item.get("postdate", "")
                }
                extracted_list.append(extracted_item)

            return extracted_list
        else:
            print("API 오류 코드:", rescode)
            return []

    except Exception as e:
        print("요청 중 오류 발생:", e)
        return []

# 메인 실행
if __name__ == "__main__":
    print("== 네이버 블로그 맛집 검색 ==")
    query = input("검색할 맛집 지역이나 키워드를 입력하세요: ")

    results = search_blog(query)

    if results:
        for idx, item in enumerate(results, 1):
            print(f"\n[{idx}] 제목: {item['title']}")
            print(f"     링크: {item['link']}")
            print(f"     블로거명: {item['bloggername']}")
            print(f"     작성일자: {item['postdate']}")
    else:
        print("검색 결과가 없습니다.")

        import urllib.request
import urllib.parse
import json

client_id = "WBfYyw5c3TVgmf7c833y"
client_secret = "cOOr830V1X"

def search_blog(query):
    encText = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/blog?query={encText}"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if rescode == 200:
            response_body = response.read().decode('utf-8')

            # 🟡 디버깅용 응답 출력
            print("\n[DEBUG] API 응답 내용:")
            print(response_body[:300])  # 앞부분만 출력

            try:
                data = json.loads(response_body)
            except json.JSONDecodeError as json_error:
                print("⚠️ JSON 파싱 오류:", json_error)
                return []

            extracted_list = []
            for item in data.get('items', []):
                extracted_item = {
                    "title": item.get("title", ""),
                    "link": item.get("link", ""),
                    "description": item.get("description", ""),
                    "bloggername": item.get("bloggername", ""),
                    "postdate": item.get("postdate", "")
                }
                extracted_list.append(extracted_item)

            return extracted_list
        else:
            print("API 오류 코드:", rescode)
            return []

    except Exception as e:
        print("요청 중 오류 발생:", e)
        return []


# main.py
import urllib.request
import urllib.parse
import json

# 네이버 API 인증 정보
client_id = "WBfYyw5c3TVgmf7c833y"
client_secret = "cOOr830V1X"

def search_blog(query):
    # 검색어 인코딩
    encText = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/blog?query={encText}"

    # 요청 설정
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    try:
        # 요청 보내기
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if rescode == 200:
            response_body = response.read().decode('utf-8')

            # JSON 파싱 시도
            try:
                data = json.loads(response_body)
            except json.JSONDecodeError:
                print("⚠️ 응답을 JSON으로 해석할 수 없습니다.")
                print("응답 내용:", response_body)
                return []

            # 결과 추출
            extracted_list = []
            for item in data.get('items', []):
                extracted_item = {
                    "title": item.get("title", "").replace("<b>", "").replace("</b>", ""),
                    "link": item.get("link", ""),
                    "description": item.get("description", ""),
                    "bloggername": item.get("bloggername", ""),
                    "postdate": item.get("postdate", "")
                }
                extracted_list.append(extracted_item)

            return extracted_list
        else:
            print("API 호출 실패 - 응답 코드:", rescode)
            return []

    except Exception as e:
        print("요청 중 오류 발생:", e)
        return []

# 메인 실행
if __name__ == "__main__":
    print("== 네이버 블로그 맛집 검색 ==")
    query = input("검색할 맛집 지역이나 키워드를 입력하세요: ")

    results = search_blog(query)

    if results:
        for idx, item in enumerate(results, 1):
            print(f"\n[{idx}] 제목: {item['title']}")
            print(f"     링크: {item['link']}")
            print(f"     블로거명: {item['bloggername']}")
            print(f"     작성일자: {item['postdate']}")
    else:
        print("검색 결과가 없습니다.")

