unlayer.registerTool({
  name: 'my_tool',
  label: 'Subscriber name',
  icon: 'fa-smile',
  supportedDisplayModes: ['web', 'email'],
  options: {},
  values: {},
  renderer: {
    Viewer: unlayer.createViewer({
      render(values) {
        return "+++subscriber_name+++"
      }
    }),
    exporters: {
      web: function(values) {
        return "+++subscriber_name+++"
      },
      email: function(values) {
        return "+++subscriber_name+++"
      }
    },
    head: {
      css: function(values) {},
      js: function(values) {}
    }
  },
  validator(data) {
    return [];
  },
});