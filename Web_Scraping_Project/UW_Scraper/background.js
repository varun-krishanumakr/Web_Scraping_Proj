// Listen for messages from content scripts
// if received, then scrape the necessary page for data, turn it into a map of sorts,
// and send it back to the content script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getPlannedCourses") {
    console.log("Background script received message to get planned courses.");
    fetch("https://plan-app-api.planning.sis.uw.edu/api/plan/terms", {credentials: 'include'})
      .then(response => response.json())
      .then(json => {
        // Extract planned courses from the JSON response
        const plannedCourses = {};
        json.forEach(term => {
          plannedListString = JSON.stringify(term.plannedList);
          plannedListJSON = JSON.parse(plannedListString);
          plannedListJSON.forEach(item => {
            console.log("Planned list courses: ", item.courseDetails);
          });
          // plannedListJSON.forEach(item => {
          //   console.log("Planned list courses: ", item.courseDetails);  
          // })
          // console.log(term.plannedList.courseDetails.abbrGenEdRequirements);
          // term.plannedList.forEach(course => {
          //   plannedCourses[course] = term.qtrYear;
          // });
        });
        // console.log("Planned courses extracted:", plannedCourses);
        // sendResponse({ plannedCourses });
      });
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