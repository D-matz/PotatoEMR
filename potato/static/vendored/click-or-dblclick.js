
htmx.defineExtension('click-or-dblclick', {
  onEvent: function(name, evt) {
    if (name === 'htmx:configRequest') {
      let dblclickUrl = evt.detail.elt.getAttribute('dblclick-url');
     if (!dblclickUrl){
         console.log("error: click-or-dblclick extension but no dblclick-url attribute");
      return;
         }

      let triggeringEvent = evt.detail.triggeringEvent;
      if (triggeringEvent && triggeringEvent.type === 'dblclick') {
        evt.detail.path = dblclickUrl;
      }
    }
  }
});
