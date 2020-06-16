function lookup(method, endpoint, callback, data) {
    let jsonData
    if (data){
        jsonData = JSON.stringify(data)
    }
    const xhr = new XMLHttpRequest()
    const url = `http://localhost:8000/api/${endpoint}/`
    xhr.responseType = "json"
    xhr.open(method, url)
    xhr.onload = function() {
      callback(xhr.response, xhr.status)
    }
    xhr.onerror = function (e) {
      console.log(e)
      callback({"message": "The request was an error"}, 400)
    }
    xhr.send(jsonData)


}
export function loadTweets(callback) {
    lookup("GET", "tweets", callback)
    const xhr = new XMLHttpRequest()
    const method = 'GET' // "POST"
    const url = "http://localhost:8000/api/tweets/"
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function() {
      callback(xhr.response, xhr.status)
    }
    xhr.onerror = function (e) {
      console.log(e)
      callback({"message": "The request was an error"}, 400)
    }
    xhr.send()
  }