window.onload = function() {
  window.ui = SwaggerUIBundle({
    url: document.getElementById("swagger-ui").getAttribute('type'),
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout"
  });
};

 