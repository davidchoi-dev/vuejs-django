# Vue-Django 연동 프로젝트 리뷰

ToDo 앱을 여러 방식으로 만들면서 django 폼, 템플릿의 한계점을 확인해보고  
vue.js 와의 연동을 통해서 효율적으로 개선함을 목표로 한다.

# only vue.js 

* 페이지 구성
    - 단일 페이지 : `todo/todo_vue_only.html` 
* 새로고침 시 데이터 초기화됨

# only django

* 페이지 구성
    - Todo 항목 생성 : TodoCV 의 `todo/todo_form.html`
    - Todo 항목 리스트 : TodoLV 의 `todo/todo_list.html`
    - Todo 항목 삭제 : TodoDelV 의 `todo/todo_confirm_delete.html`
* 데이터베이스 저장 및 불러오기 가능
* 페이지 구성이 복잡하며 페이지 이동이 계속 발생

# django mixin

* 페이지 구성
    - Todo 항목 생성 + 리스트 페이지 : TodoMOMCV 의 `todo/todo_form_list.html`
    - Todo 항목 삭제 : TodoDelV2 (DeleteView 의 get 을 재정의)
* 데이터베이스 저장 및 불러오기 가능
* 시작 페이지와 `success_url`이 같아서 이동이 없는 것 처럼 보이지만 실제로 리다이렉트와 함께  
  서버사이드 렌더링이 발생함

# django & vue.js

* 페이지 구성
    - 단일 페이지 : TodoTV 의 `todo/todo_index.html`
* `api` 앱에서 **JsonResponse**로 axios 요청을 처리
    - ApiTodoLV
    - ApiTodoDelV
    - ApiTodoCV
    - (위 클래스 모두 템플릿관련 처리가 필요없는 json 응답이기 때문에 Base기반뷰를 상속받음)
