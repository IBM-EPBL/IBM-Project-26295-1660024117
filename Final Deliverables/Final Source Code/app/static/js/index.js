window.watsonAssistantChatOptions = {
  integrationID: "e1de96c7-2c19-4ce8-bd65-89f8c188a675", // The ID of this integration.
  region: "us-south", // The region your integration is hosted in.
  serviceInstanceID: "6866005d-248a-4c42-adcf-27ca76048e7e", // The ID of your service instance.
  onLoad: function (instance) {
    instance.render();
  },
};
setTimeout(function () {
  const t = document.createElement("script");
  t.src =
    "https://web-chat.global.assistant.watson.appdomain.cloud/versions/" +
    (window.watsonAssistantChatOptions.clientVersion || "latest") +
    "/WatsonAssistantChatEntry.js";
  document.head.appendChild(t);
});
