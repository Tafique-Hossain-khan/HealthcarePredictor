document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('symptom-search');
    const optionsList = document.getElementById('symptom-options');
    const selectedSymptoms = document.getElementById('selected-symptoms');
    const selectedSymptomsInput = document.getElementById('selected-symptoms-input');
    const form = document.getElementById('symptom-form');

    // List of all symptoms (add your complete list here)
    const symptoms =  [
        'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 
        'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 
        'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 
        'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 
        'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 
        'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 
        'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 
        'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 
        'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 
        'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 
        'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 
        'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 
        'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 
        'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 
        'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 
        'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 
        'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 
        'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 
        'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 
        'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 
        'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 
        'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 
        'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 
        'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 
        'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 
        'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 
        'altered_sensorium', 'red_spots_over_body', 'belly_pain', 
        'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 
        'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 
        'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 
        'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 
        'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 
        'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 
        'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 
        'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 
        'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze', 
        'prognosis'
    ];

    // Filter symptoms based on search input
    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        const filteredSymptoms = symptoms.filter(symptom => 
            symptom.toLowerCase().includes(searchTerm)
        );

        // Show/hide options list
        optionsList.classList.toggle('hidden', searchTerm === '');

        // Update options list
        optionsList.innerHTML = filteredSymptoms
            .map(symptom => `<li class="p-2 hover:bg-gray-700 cursor-pointer">${symptom}</li>`)
            .join('');
    });

    // Handle symptom selection
    optionsList.addEventListener('click', function(e) {
        if (e.target.tagName === 'LI') {
            const symptom = e.target.textContent;
            
            // Add symptom to selected symptoms
            const symptomSpan = document.createElement('span');
            symptomSpan.className = 'bg-indigo-500 text-white px-2 py-1 rounded-md flex items-center';
            symptomSpan.innerHTML = `${symptom} <span class="ml-2 cursor-pointer">×</span>`;
            selectedSymptoms.appendChild(symptomSpan);

            // Clear search input and hide options
            searchInput.value = '';
            optionsList.classList.add('hidden');

            // Update hidden input with all selected symptoms
            updateSelectedSymptoms();
        }
    });

    // Remove symptom when clicked
    selectedSymptoms.addEventListener('click', function(e) {
        if (e.target.textContent === '×') {
            e.target.parentElement.remove();
            updateSelectedSymptoms();
        }
    });

    // Update hidden input with selected symptoms
    function updateSelectedSymptoms() {
        const symptoms = Array.from(selectedSymptoms.children).map(span => 
            span.textContent.replace(' ×', '')
        );
        selectedSymptomsInput.value = JSON.stringify(symptoms);
    }

    // Handle form submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get selected symptoms
        const symptoms = Array.from(selectedSymptoms.children).map(span => 
            span.textContent.replace(' ×', '')
        );

        if (symptoms.length === 0) {
            alert('Please select at least one symptom');
            return;
        }

        // Update hidden input
        selectedSymptomsInput.value = JSON.stringify(symptoms);
        
        // Submit the form
        this.submit();
    });
});
