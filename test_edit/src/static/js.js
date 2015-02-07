
$(document).ready(function() {
  if(!("WebSocket" in window)){
    alert("BOOM NO WEBSOCKET");
  }else{
    connect();
  }
});

$('#editor').keypress(function(event) {
  if (event.which == 13) {  //Enter Key
    event.preventDefault();
    sendChanges();
  }
});

function connect() {
  var host = "ws://localhost:8080/ws";
  //var host = "ws://10.44.88.142:8080/ws";
  var retryTimeout;
  var socket = new WebSocket(host);

  socket.onopen = function(){
    clearTimeout(retryTimeout);
    alert('WSOPEN');
    refreshChat();
  }

  socket.onmessage = function(msg){
    $('#content').html(msg.data);
  }

  socket.onclose = function(){
    clearTimeout(retryTimeout);
    alert('WSCLOSE');
    retryTimeout = setTimeout(function(){
      connect();
    }, 3000);
  }      
}

function sendChanges() {
  $.ajax({
    type: "POST",
    url: "save",
    data: "content=" + $('#editor').val() + '<br>',
    cache: false,
    dataType: "text",
    success: function(data) {
      console.log('SEND SUCCESS')
      $('#editor').val('');
      //alert('AJAX SUCCESS');
      //$('#content').text(data);
    }
  });
}

function refreshChat() {
  $.ajax({
    type: "GET",
    url: "refresh",
    dataType: "text",
    success: function(data) {
      console.log('REFRESH SUCCESS')
      $('#content').html(data);
      //alert('AJAX SUCCESS');
      //$('#content').text(data);
    }
  });
}
