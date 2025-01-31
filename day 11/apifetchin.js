const api = "https://jsonplaceholder.typicode.com/todos/1";

fetch(api)
  .then((response) => response.json())
  .then((json) => console.log(json));
