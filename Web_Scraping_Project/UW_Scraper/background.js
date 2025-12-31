// Listen for messages from content scripts
// if received, then scrape the necessary page for data, turn it into a map of sorts,
// and send it back to the content script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getPlannedCourses") {
    console.log("Background script received message to get planned courses.");
    fetch("https://myplan.uw.edu/plan", {credentials: 'include'})
      .then(response => response.text())
      .then(html => sendResponse({html: html}));
    return true; // Keeps message channel open for async response
  }
});

// try {
//     // On page change
//     chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
//         if (changeInfo.status === 'complete') {
//             chrome.scripting.executeScript({
//                 target: { tabId: tab.id },
//                 files: ['contentScript.js']
//             });
//         }
//     });
// } catch (e) {
//     console.log(e);
// }