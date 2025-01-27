;/*FB_PKG_DELIM*/

__d("cancelAnimationFramePolyfill",[],(function(a,b,c,d,e,f){"use strict";b=a.__fbNativeCancelAnimationFrame||a.cancelAnimationFrame||a.webkitCancelAnimationFrame||a.mozCancelAnimationFrame||a.oCancelAnimationFrame||a.msCancelAnimationFrame||a.clearTimeout;c=b;f["default"]=c}),66);
__d("cancelAnimationFrame",["cancelAnimationFramePolyfill"],(function(a,b,c,d,e,f,g){function a(a){c("cancelAnimationFramePolyfill")(a)}g["default"]=a}),98);
__d("setInterval",["cr:7388"],(function(a,b,c,d,e,f,g){g["default"]=b("cr:7388")}),98);
__d("RelayFBScheduler",[],(function(a,b,c,d,e,f){"use strict";a={cancel:function(){},schedule:function(a){a();return""}};b=a;f["default"]=b}),66);
__d("getReferrerURI",["ErrorGuard","URI","isFacebookURI"],(function(a,b,c,d,e,f,g){"use strict";var h,i;function b(){if(a.PageTransitions&&a.PageTransitions.isInitialized())return a.PageTransitions.getReferrerURI();else{var b=(h||(h=c("ErrorGuard"))).applyWithGuard(function(a){return(i||(i=c("URI"))).tryParseURI(a)},null,[document.referrer]);return b&&c("isFacebookURI")(b)?b:null}}g["default"]=b}),98);
__d("setIntervalBlue",["TimerStorage","setIntervalAcrossTransitions"],(function(a,b,c,d,e,f,g){function a(a,b){for(var d=arguments.length,e=new Array(d>2?d-2:0),f=2;f<d;f++)e[f-2]=arguments[f];var g=c("setIntervalAcrossTransitions").apply(void 0,[a,b].concat(e));c("TimerStorage").set(c("TimerStorage").INTERVAL,g);return g}g["default"]=a}),98);
__d("setIntervalWWW",["cr:896461"],(function(a,b,c,d,e,f,g){g["default"]=b("cr:896461")}),98);