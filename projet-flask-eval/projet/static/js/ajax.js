function getApi(url, data=null, method='GET', content = false) {
    return new Promise(function(resolve, reject) {

      $.ajax({
        url: url,
        method: method,
        dataType: 'json',
        contentType: content,
        processData: false,
        data: data,
        success: function(response) {
          resolve(response);
        },
        error: function(xhr, status, error) {
          reject(error);
        }
      });
    });
  }


  function getApi2(url, data = null, method = 'GET', content = false) {
    return new Promise(function(resolve, reject) {
        var xhr = new XMLHttpRequest();
        xhr.open(method, url, true);
        xhr.setRequestHeader('Content-Type', content);
        xhr.onload = function() {
            if (xhr.status === 200) {
                var valeur = JSON.parse(xhr.responseText);
                resolve(valeur);
            } else {
                reject(xhr.statusText);
            }
        };
        xhr.onerror = function() {
            reject(xhr.statusText);
        };
        xhr.send(data);
    });
}