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

jinja 템플릿 문법은 크게 두 가지로 나눌 수 있다. (구분자 : jinja 템플릿 문법임을 구분하는 용도)

- `{{ … }}`
  변수, 표현식의 결과를 출력하는 구분자(delimeter)
- `{% … %}`
  if문이나 for문 같은 제어문을 할당하는 구분자(delimeter)

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
