async function callApi() {
  const res = await fetch("http://www.nicovideo.jp/ranking/fav/hourly/all?rss=2.0");
  const users = await res.json();
  console.log(users);
};

callApi();

// XMLHttpRequest

// let request = new XMLHttpRequest();

// request.open('GET', 'https://jsonplaceholder.typicode.com/users/1', true);
// request.responseType = 'json';

// request.onload = function() {
//   let data = this.response;
//   console.log(data)
// };

// request.send();
