(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{11:function(e,n,o){e.exports=o(25)},16:function(e,n,o){},19:function(e,n,o){},21:function(e,n,o){},25:function(e,n,o){"use strict";o.r(n);var t=o(0),i=o.n(t),a=o(10),r=o.n(a),c=(o(16),o(3)),s=o(4),l=o(7),u=o(5),d=o(8),f=o(27);o(18),o(19),o(21),t.Component,t.Component;var m=function(e){function n(e){var o;return Object(c.a)(this,n),(o=Object(l.a)(this,Object(u.a)(n).call(this,e))).state={mode:"normal"},o}return Object(d.a)(n,e),Object(s.a)(n,[{key:"toggleEdit",value:function(e){console.log("goteem"),this.setState({mode:"normal"==this.state.mode?"edit":"normal"})}},{key:"render",value:function(){[["/","Home"],["/settings","Settings"]].map(function(e){return function(e,n){return i.a.createElement("div",{className:"nav-item",key:e},i.a.createElement(f.a,{className:"nav-link",to:e},n))}.apply(null,e)});return i.a.createElement("div",{className:"App"},i.a.createElement("header",{className:"home_bar"}))}}]),n}(t.Component),g=(i.a.Component,m),v=Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));function h(e){navigator.serviceWorker.register(e).then(function(e){e.onupdatefound=function(){var n=e.installing;n.onstatechange=function(){"installed"===n.state&&(navigator.serviceWorker.controller?console.log("New content is available; please refresh."):console.log("Content is cached for offline use."))}}}).catch(function(e){console.error("Error during service worker registration:",e)})}r.a.render(i.a.createElement(g,null),document.getElementById("root")),function(){if("serviceWorker"in navigator){if(new URL("",window.location).origin!==window.location.origin)return;window.addEventListener("load",function(){var e="".concat("","/service-worker.js");v?(function(e){fetch(e).then(function(n){404===n.status||-1===n.headers.get("content-type").indexOf("javascript")?navigator.serviceWorker.ready.then(function(e){e.unregister().then(function(){window.location.reload()})}):h(e)}).catch(function(){console.log("No internet connection found. App is running in offline mode.")})}(e),navigator.serviceWorker.ready.then(function(){console.log("This web app is being served cache-first by a service worker. To learn more, visit https://goo.gl/SC7cgQ")})):h(e)})}}()}},[[11,2,1]]]);
//# sourceMappingURL=main.b9a01ed9.chunk.js.map