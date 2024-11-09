const symptomSearch = document.getElementById("symptom-search");
const symptomOptions = document.getElementById("symptom-options");
const selectedSymptoms = document.getElementById("selected-symptoms");
const predictBtn = document.getElementById("predict-btn");
const recommendations = document.getElementById("recommendations");

// Sample symptom data
const symptoms = ["itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering", "chills", "joint_pain", "stomach_pain,acidity","ulcers_on_tongue","muscle_wasting","vomiting","burning_micturition","spotting_urination","fatigue","weight_gain","anxiety","cold_hands_and_feets","mood_swings"];

// Display options in dropdown
symptomSearch.addEventListener("focus", () => {
    symptomOptions.classList.remove("hidden");
});

symptomSearch.addEventListener("input", () => {
    symptomOptions.innerHTML = "";
    const search = symptomSearch.value.toLowerCase();
    symptoms.filter(symptom => symptom.toLowerCase().includes(search)).forEach(symptom => {
        const option = document.createElement("li");
        option.textContent = symptom;
        option.className = "p-2 hover:bg-gray-700 cursor-pointer";
        option.addEventListener("click", () => addSymptom(symptom));
        symptomOptions.appendChild(option);
    });
});

// Add symptom to selected bar
function addSymptom(symptom) {
    if (!Array.from(selectedSymptoms.children).some(span => span.textContent.includes(symptom))) {
        const symptomBadge = document.createElement("span");
        symptomBadge.className = "bg-red-600 text-white px-2 py-1 rounded-full flex items-center gap-2";
        symptomBadge.innerHTML = `${symptom} <button class="remove-symptom font-bold">&times;</button>`;
        selectedSymptoms.appendChild(symptomBadge);

        // Remove symptom
        symptomBadge.querySelector(".remove-symptom").addEventListener("click", () => {
            selectedSymptoms.removeChild(symptomBadge);
        });
    }
    symptomOptions.classList.add("hidden");
    symptomSearch.value = "";
}

// Show Recommendations on Predict button click
predictBtn.addEventListener("click", () => {
    recommendations.classList.remove("hidden");
});

// Toggle descriptions in recommendations
document.querySelectorAll(".recommendation-btn").forEach(button => {
    button.addEventListener("click", () => {
        const description = button.nextElementSibling;
        description.classList.toggle("hidden");
    });
});

// Hide dropdown when clicking outside
document.addEventListener("click", (e) => {
    if (!symptomSearch.contains(e.target) && !symptomOptions.contains(e.target)) {
        symptomOptions.classList.add("hidden");
    }
});

// Update the form submission
const form = document.getElementById("symptom-form");
const selectedSymptomsInput = document.getElementById("selected-symptoms-input");

form.addEventListener("submit", (e) => {
    e.preventDefault();
    
    // Get all selected symptoms
    const symptoms = Array.from(selectedSymptoms.children).map(span => 
        span.textContent.replace(" ×", "")
    );
    
    // Update hidden input
    selectedSymptomsInput.value = JSON.stringify(symptoms);
    
    // Submit the form
    form.submit();
});
