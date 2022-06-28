# 2022년 6월 28일

### Today is …

<aside>
🍇 비 안 오면 나나 산책(+목욕)

밥 맛있는 거로 챙겨먹기

청소기 돌리고 빨래 개기

도서관 가서 책 대출

</aside>

- [ ] 헷갈리던 키워드 정리(Jinja)
- [ ] 웹종합개발 4주차(빠르게 큰 단계별로 정리하면서)
- [ ] 파이썬 강의록
- [ ] TIL 작성, git commit
- [ ] ~~자바스크립트 강의(~1-9 조건문)~~

---

# 항해 1주차 전까지 알아두어야 할 것들

항해 1주차 TIL을 구글링 해봤다. 찾아보니 사전강의의 연장선으로(그런 의미로 계속 반복학습을 하라는 것 같다.) flask, mongoDB, AWS를 이용해서 미니 프로젝트를 진행하는 거로 보였다.

<aside>
🍉 **1주차 키포인트**

- **Jinja2** (템플릿 엔진, 서버사이드 렌더링)
- **JWT** 인증 방식 로그인 구현
- API와 API 설계(어떤 메서드를 쓰고 싶은가?)
  - DB - API 연결
- 크롤링, DB업로드
- (와이어프레임)
</aside>

특히, 로그인은 내가 직접 다시 구현하는 게 목표! 그렇지만 명심할 것 어려우니까 어려운 거다.

푼 문제와 풀지 않은 문제

---

## 1. Jinja

- python flask 패키지에 내장된 템플릿 엔진
- 개발자가 **동적으로** 변하는 웹 페이지를 쉽게 구현할 수 있도록 도와줌
- **고정**적으로 **출력**되어야 할 **서식 html코드**가 존재하고, **동적**으로 변해야 할 자리는 **jinja2 문법으로 비워놓는다.**
- 이후 클라이언트가 웹 브라우저를 통해 엔드포인트에 접근하면, 비워둔 자리에 값을 설정하여 클라이언트에게 출력한다.
  - 고정값과 변하는 값을 쉽게 제어할 수 있다는 장점

### 1-1. 형태

```html
<!DOCTYPE HTML>
<html lang="en">
<head>
     <title>My Webpage</title>
</head>
<body>
     <ul id="navigation">
          **{% for item in navigation %}**
          <li><a href="**{{ item.href }}**">**{{ item['caption'] }}**</a></li>
          **{% endfor}**
     <ul>
     <h1>My Webpage</h1>
     **{{ a_variable }}**
</body>
</html>
```

---

jinja 템플릿 문법은 크게 두 가지로 나눌 수 있다. (구분자 : jinja 템플릿 문법임을 구분하는 용도)

- `{{ … }}`
  변수, 표현식의 결과를 출력하는 구분자(delimeter)
- `{% … %}`
  if문이나 for문 같은 제어문을 할당하는 구분자(delimeter)
- `{# ... #}`
  주석
- `{%- ... %}` `{%+ ... %}` `{% ... -%}`
  공백 제거 혹은 유지
- `{% raw %}` … `{% endraw %}`
  이스케이프

---

`item.href` 와 `item['href']` 는 기본적으로 같다.

만약 `item.href`로 접근하는 경우,

item 객체 내에서 href라는 속성이 있는지 먼저 확인한 후, 없을 경우 href라는 객체가 있는지 확인

반면에 `item['href']`로 접근하는 경우,

item 객체 내에서 href라는 객체가 있는지 먼저 확인한 후, 없을 경우에 href라는 객체가 있는지 확인

<aside>
🍞 즉,

`.(온점)`으로 접근하는 경우 : 속성 → 객체 확인

`''(따옴표)`로 접근하는 경우 : 객체 → 속성 확인

</aside>

### 1-2. 반복문

```html
{% **for** <개별요소> in <리스트> %} <실행코드> {% **endfor** %}
```

```html
<!-- 예시 -->
{% for item in navigation %}
<li><a href="{{ item.href }}">{{ item.caption}}</a></li>
{% endfor %}
```

Jinja2의 for ~ in 문의 사용법은 파이썬 문법과 동일하다고 여기면 된다. navigation이라는 리스트의 각 변수 혹은 객체를 item 변수에 담아 안쪽에서 해당 값을 이용하며 시작시에는 for, 종료시에는 endfor를 이용한다.

### 1-3. 제어문

```html
{% if <조건> %} <실행코드> {% elif <조건> %} <실행코드> {% else %} <실행코드> {%
endif %}
```

[참고 1](https://snacky.tistory.com/7?category=710115)  
[참고 2](https://velog.io/@sezeom/flask-jinja%EB%9E%80)
