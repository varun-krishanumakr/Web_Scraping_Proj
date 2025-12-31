// this makes sure that we don't run init multiple times
// if (typeof init === 'undefined') {
//     init();
// }

// const init = function(){
//     console.log("Initialization complete.");
//     const injectElement = document.createElement('div');
//     injectElement.className = 'injected-class';
//     injectElement.innerHTML = '<strong>Hello, World!</strong>';
//     injectElement.id = 'injected-element';
//     document.body.appendChild(injectElement);
// }

console.log("Content script is executing.");
window.addEventListener('load', function() {
    console.log("Content script loaded, sending message to background script.");
    chrome.runtime.sendMessage({action: "getPlannedCourses"}, function(response) {
        // Process the received HTML content
        console.log("Received HTML content:", response.html);
    });
});