### login

method : post

headers

| 参数名 | 参数类型 | 是否必传 | 备注 |
| ------ | -------- | -------- | ---- |
| token    | str     | 是       | -    |

param
|参数名|参数类型|是否必传|备注|
|-|-|-|-|
|username|str|是||
|password|str|是||

&emsp;

请求(request case)

```js
var data = new FormData();
data.append("username", "pi");
data.append("password", "raspberry");

var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === 4) {
    console.log(this.responseText);
  }
});

xhr.open("POST", "http://localhost/login");

xhr.send(data);
```

响应(response case)

```json
{
  "code": 0,
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InBpIiwiZXhwIjoxNjIzMTM4ODEzLjA4MTAxOTl9.7aSA-qQlklD66FocOMzeZaZZ6VcW6o9iQ8OzFAntCoo"
}
```
