var setTargetTo = null;
htmx.defineExtension('click-or-dblclick', {
  onEvent : function(name, evt) {
    if( evt && evt.detail && evt.detail.triggeringEvent)
    {
      //not sure how to set hx-push-url from dblclick-push-url
      //so just always setting true on double click
      //problem with setting attributes is if you don't navigate away from page they're permanently set?
      if(evt.detail.triggeringEvent.type === 'dblclick')
      {
        evt.detail.elt.setAttribute('hx-push-url', 'true');
      }
    }
    if (name === 'htmx:configRequest') {
      if(evt && evt.detail && evt.detail.triggeringEvent)
      {
        if(evt.detail.triggeringEvent.type === 'dblclick')
        {
          let urlSource = evt.detail.elt.closest('[dblclick-url]');
          if (urlSource) {
            evt.detail.path = urlSource.getAttribute('dblclick-url');
          }
          let targetSource = evt.detail.elt.closest('[dblclick-target]');
          if (targetSource) {
            setTargetTo = document.querySelector(targetSource.getAttribute('dblclick-target'));
          }
        }
        else
        {
          setTargetTo = evt.detail.target;
        }
      }
    }
    if(evt && evt.detail && setTargetTo)
    {
      evt.detail.target = setTargetTo;
    }
  }
});
