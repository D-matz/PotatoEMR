var setTargetTo = null;
htmx.defineExtension('click-or-dblclick', {
  onEvent : function(name, evt) {
    if (name === 'htmx:configRequest') {
      if(evt && evt.detail && evt.detail.triggeringEvent)
      {
        if(evt.detail.triggeringEvent.type === 'dblclick')
        {
          let targetSource = evt.detail.elt.closest('[dblclick-target]');
          let urlSource = evt.detail.elt.closest('[dblclick-url]');

          if (urlSource) {
            evt.detail.path = urlSource.getAttribute('dblclick-url');
          }
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
