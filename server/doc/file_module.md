## good module

- [file](###//file/{path})
- [edit](###/edit)
- [read](###/read)

### /file/{path}

method : get

headers

| 参数名 | 参数类型 | 是否必传 | 备注 |
| ------ | -------- | -------- | ---- |
| token  | str      | 是       | -    |

&emsp;

请求(request case)

```js
var request = require("request");
var options = {
  method: "GET",
  url: "http://localhost:10086/file/Users",
  headers: {},
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

响应(response case)

```json
{
  "code": 0,
  "list": [
    {
      "filename": "/Users/.localized",
      "is_can_read": true,
      "is_can_write": true,
      "is_dir": false
    },
    {
      "filename": "/Users/Shared",
      "is_can_read": true,
      "is_can_write": true,
      "is_dir": true
    },
    {
      "filename": "/Users/visitor",
      "is_can_read": true,
      "is_can_write": false,
      "is_dir": true
    }
  ]
}
```

### /file

method : get

&emsp;

headers

| 参数名 | 参数类型 | 是否必传 | 备注 |
| ------ | -------- | -------- | ---- |
| token  | str      | 是       | -    |

请求(request case)

```js
var request = require("request");
var options = {
  method: "GET",
  url: "http://localhost:10086/file",
  headers: {},
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

响应(response case)

```json
{
  "code": 0,
  "list": [
    {
      "filename": "/home",
      "is_can_read": true,
      "is_can_write": true,
      "is_dir": true
    }
  ]
}
```

### /edit

method : post

headers

| 参数名 | 参数类型 | 是否必传 | 备注 |
| ------ | -------- | -------- | ---- |
| token  | str      | 是       | -    |

param
|参数名|参数类型|是否必传|备注|
|-|-|-|-|
|path|str|是|文件绝对路径|
|text|str|是||

&emsp;

请求(request case)

```js
var data = new FormData();
data.append("text", "is_root111");

var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === 4) {
    console.log(this.responseText);
  }
});

xhr.open("POST", "http://localhost/edit?path={path}");
xhr.setRequestHeader("token", "1234");

xhr.send(data);
```

响应(response case)

```json
{
  "code": 0
}
```

### /read

method : post

headers

| 参数名 | 参数类型 | 是否必传 | 备注 |
| ------ | -------- | -------- | ---- |
| token  | str      | 是       | -    |

param
|参数名|参数类型|是否必传|备注|
|-|-|-|-|
|path|str|是|文件绝对路径|

&emsp;

请求(request case)

```js
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === 4) {
    console.log(this.responseText);
  }
});

xhr.open("POST", "http://localhost/read?path={path}");
xhr.setRequestHeader("token", "");

xhr.send();
```

响应(response case)

```json
{
  "code": 0,
  "text": "hello 123"
}
```
