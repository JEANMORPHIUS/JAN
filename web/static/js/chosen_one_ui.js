// CHOSEN ONE FRAMEWORK - UI JAVASCRIPT

let statusData = null;

// Load status on page load
document.addEventListener('DOMContentLoaded', function() {
    loadStatus();
    setInterval(loadStatus, 30000); // Refresh every 30 seconds
});

async function loadStatus() {
    try {
        const response = await fetch('/api/status');
        const result = await response.json();
        
        if (result.success) {
            statusData = result.data;
            updateUI(result.data);
        } else {
            console.error('Error loading status:', result.error);
        }
    } catch (error) {
        console.error('Error fetching status:', error);
    }
}

function updateUI(data) {
    // Update status overview
    document.getElementById('current-state').textContent = data.current_state.toUpperCase();
    document.getElementById('current-state').className = 'state-badge ' + (data.current_state === 'witness' ? 'witness' : 'vindicated');
    
    const activationDate = new Date(data.activation_date);
    document.getElementById('activation-date').textContent = activationDate.toLocaleDateString();
    
    document.getElementById('elapsed-time').textContent = formatElapsedTime(data.elapsed_time);
    
    // Update gears
    updateGearStatus('gear-evidence', data.evidence_gathering_active);
    updateGearStatus('gear-atmospheric', data.atmospheric_shift_active);
    updateGearStatus('gear-manifestation', data.manifestation_cascade_active);
    
    // Update witness behaviors
    updateBehaviorStatus('behavior-selective', data.witness_behaviors.selective_speech);
    updateBehaviorStatus('behavior-prophetic', data.witness_behaviors.prophetic_observation);
    updateBehaviorStatus('behavior-energetic', data.witness_behaviors.energetic_stewardship);
    
    // Update forbidden functions
    updateForbiddenFunctions(data.forbidden_functions);
    
    // Update timeline markers
    updateTimelineMarkers(data.markers);
}

function updateGearStatus(elementId, active) {
    const element = document.getElementById(elementId);
    const indicator = element.querySelector('.status-indicator');
    const text = element.querySelector('span:last-child');
    
    indicator.className = 'status-indicator ' + (active ? 'active' : 'inactive');
    text.textContent = active ? 'ACTIVE' : 'INACTIVE';
}

function updateBehaviorStatus(elementId, active) {
    const element = document.getElementById(elementId);
    const indicator = element.querySelector('.status-indicator');
    const text = element.querySelector('span:last-child');
    
    indicator.className = 'status-indicator ' + (active ? 'active' : 'inactive');
    text.textContent = active ? 'ACTIVE' : 'INACTIVE';
}

function updateForbiddenFunctions(functions) {
    const container = document.getElementById('forbidden-functions');
    if (functions.length === 0) {
        container.innerHTML = '<p>No forbidden functions enforced.</p>';
        return;
    }
    
    const ul = document.createElement('ul');
    functions.forEach(func => {
        const li = document.createElement('li');
        li.textContent = func.replace(/_/g, ' ').toUpperCase();
        ul.appendChild(li);
    });
    container.innerHTML = '';
    container.appendChild(ul);
}

function updateTimelineMarkers(markers) {
    const container = document.getElementById('timeline-markers');
    container.innerHTML = '';
    
    Object.entries(markers).forEach(([timeline, marker]) => {
        const card = document.createElement('div');
        card.className = 'marker-card ' + (marker.confirmed ? 'confirmed' : marker.due ? 'due' : '');
        
        const title = document.createElement('h3');
        title.textContent = timeline.replace(/_/g, ' ').toUpperCase();
        card.appendChild(title);
        
        const status = document.createElement('p');
        status.textContent = marker.confirmed ? '✓ CONFIRMED' : marker.due ? '⚠ DUE' : '⏳ PENDING';
        card.appendChild(status);
        
        const expected = document.createElement('p');
        expected.textContent = 'Expected: ' + new Date(marker.expected_date).toLocaleString();
        card.appendChild(expected);
        
        if (marker.confirmed && marker.actual_date) {
            const actual = document.createElement('p');
            actual.textContent = 'Confirmed: ' + new Date(marker.actual_date).toLocaleString();
            card.appendChild(actual);
        }
        
        if (marker.emotional_response) {
            const emotional = document.createElement('p');
            emotional.textContent = 'Emotional Response: ' + marker.emotional_response;
            card.appendChild(emotional);
        }
        
        if (marker.due && !marker.confirmed) {
            const button = document.createElement('button');
            button.className = 'btn-primary';
            button.textContent = 'Confirm Marker';
            button.onclick = () => confirmMarker(timeline);
            card.appendChild(button);
        }
        
        container.appendChild(card);
    });
}

function formatElapsedTime(timeString) {
    // Parse "X days, H:MM:SS" format
    const match = timeString.match(/(\d+) days?, (\d+):(\d+):(\d+)/);
    if (match) {
        const days = match[1];
        const hours = match[2];
        return `${days} days, ${hours} hours`;
    }
    return timeString;
}

// Modal functions
function showEvidenceGathering() {
    loadInteractions();
    document.getElementById('evidence-modal').style.display = 'block';
}

function showAtmosphericShift() {
    loadAtmosphericShifts();
    document.getElementById('atmospheric-modal').style.display = 'block';
}

function showManifestationCascade() {
    loadMarkers();
    document.getElementById('manifestation-modal').style.display = 'block';
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modals = document.getElementsByClassName('modal');
    for (let modal of modals) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    }
}

// Load interactions
async function loadInteractions() {
    try {
        const response = await fetch('/api/interactions');
        const result = await response.json();
        
        if (result.success) {
            const container = document.getElementById('interactions-list');
            container.innerHTML = '';
            
            if (result.data.length === 0) {
                container.innerHTML = '<p>No interactions recorded yet.</p>';
                return;
            }
            
            result.data.forEach(interaction => {
                const item = document.createElement('div');
                item.className = 'interaction-item';
                item.innerHTML = `
                    <strong>${interaction.type.toUpperCase()}</strong>
                    <p>${interaction.description}</p>
                    <small>${new Date(interaction.timestamp).toLocaleString()}</small>
                `;
                container.appendChild(item);
            });
        }
    } catch (error) {
        console.error('Error loading interactions:', error);
    }
}

// Add interaction
async function addInteraction() {
    const type = document.getElementById('interaction-type').value;
    const description = document.getElementById('interaction-description').value;
    
    if (!description.trim()) {
        alert('Please enter a description');
        return;
    }
    
    try {
        const response = await fetch('/api/interactions', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({type, description})
        });
        
        const result = await response.json();
        if (result.success) {
            document.getElementById('interaction-description').value = '';
            loadInteractions();
            loadStatus();
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        console.error('Error adding interaction:', error);
        alert('Error adding interaction');
    }
}

// Load atmospheric shifts
async function loadAtmosphericShifts() {
    try {
        const response = await fetch('/api/atmospheric-shifts');
        const result = await response.json();
        
        if (result.success) {
            const container = document.getElementById('shifts-list');
            container.innerHTML = '';
            
            if (result.data.length === 0) {
                container.innerHTML = '<p>No atmospheric shifts recorded yet.</p>';
                return;
            }
            
            result.data.forEach(shift => {
                const item = document.createElement('div');
                item.className = 'shift-item';
                item.innerHTML = `
                    <strong>${shift.previous_trigger}</strong>
                    <p>Power: ${shift.power_level_before.toFixed(2)} → ${shift.power_level_after.toFixed(2)}</p>
                    <small>${new Date(shift.timestamp).toLocaleString()}</small>
                `;
                container.appendChild(item);
            });
        }
    } catch (error) {
        console.error('Error loading shifts:', error);
    }
}

// Add atmospheric shift
async function addAtmosphericShift() {
    const trigger = document.getElementById('previous-trigger').value;
    const before = parseFloat(document.getElementById('power-before').value);
    const after = parseFloat(document.getElementById('power-after').value);
    
    if (!trigger.trim() || isNaN(before) || isNaN(after)) {
        alert('Please fill all fields');
        return;
    }
    
    try {
        const response = await fetch('/api/atmospheric-shifts', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                previous_trigger: trigger,
                power_level_before: before,
                power_level_after: after
            })
        });
        
        const result = await response.json();
        if (result.success) {
            document.getElementById('previous-trigger').value = '';
            document.getElementById('power-before').value = '';
            document.getElementById('power-after').value = '';
            loadAtmosphericShifts();
            loadStatus();
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        console.error('Error adding shift:', error);
        alert('Error adding shift');
    }
}

// Load markers
async function loadMarkers() {
    try {
        const response = await fetch('/api/markers');
        const result = await response.json();
        
        if (result.success) {
            const container = document.getElementById('markers-list-detailed');
            container.innerHTML = '';
            
            result.data.forEach(marker => {
                const item = document.createElement('div');
                item.className = 'marker-item ' + (marker.confirmed ? 'confirmed' : '');
                item.innerHTML = `
                    <h3>${marker.timeline.replace(/_/g, ' ').toUpperCase()}</h3>
                    <p><strong>Type:</strong> ${marker.type}</p>
                    <p><strong>Description:</strong> ${marker.description}</p>
                    <p><strong>Expected:</strong> ${new Date(marker.expected_date).toLocaleString()}</p>
                    ${marker.confirmed ? `<p><strong>Confirmed:</strong> ${new Date(marker.actual_date).toLocaleString()}</p>` : ''}
                    ${marker.emotional_response ? `<p><strong>Emotional Response:</strong> ${marker.emotional_response}</p>` : ''}
                    ${!marker.confirmed ? `<button class="btn-primary" onclick="confirmMarkerById('${marker.id}')">Confirm</button>` : ''}
                `;
                container.appendChild(item);
            });
        }
    } catch (error) {
        console.error('Error loading markers:', error);
    }
}

// Confirm marker
async function confirmMarker(timeline) {
    const description = prompt('Enter description of the marker:');
    if (!description) return;
    
    const emotional = prompt('Enter emotional response (neutral/light/heavy):', 'neutral');
    
    try {
        // Find marker ID
        const response = await fetch('/api/markers');
        const result = await response.json();
        if (result.success) {
            const marker = result.data.find(m => m.timeline === timeline);
            if (marker) {
                await confirmMarkerById(marker.id, description, emotional);
            }
        }
    } catch (error) {
        console.error('Error confirming marker:', error);
    }
}

async function confirmMarkerById(markerId, description, emotionalResponse) {
    try {
        const response = await fetch(`/api/markers/${markerId}/confirm`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                description: description || '',
                emotional_response: emotionalResponse || 'neutral'
            })
        });
        
        const result = await response.json();
        if (result.success) {
            loadMarkers();
            loadStatus();
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        console.error('Error confirming marker:', error);
        alert('Error confirming marker');
    }
}

// Test forbidden function
async function testForbiddenFunction() {
    const functionName = document.getElementById('forbidden-function-select').value;
    const context = document.getElementById('forbidden-context').value;
    
    try {
        const response = await fetch('/api/forbidden-functions/test', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({function: functionName, context})
        });
        
        const result = await response.json();
        const resultDiv = document.getElementById('forbidden-result');
        
        if (result.success) {
            if (result.blocked) {
                resultDiv.textContent = '❌ BLOCKED - Function prevented';
                resultDiv.className = 'blocked';
            } else {
                resultDiv.textContent = '✓ ALLOWED - Function permitted';
                resultDiv.className = 'allowed';
            }
        } else {
            resultDiv.textContent = 'Error: ' + result.error;
            resultDiv.className = '';
        }
    } catch (error) {
        console.error('Error testing forbidden function:', error);
    }
}

// Test selective speech
async function testSelectiveSpeech() {
    const spiritOpen = document.getElementById('spirit-open').checked;
    const questionGenuine = document.getElementById('question-genuine').checked;
    
    try {
        const response = await fetch('/api/witness-behaviors/selective-speech', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                spirit_open: spiritOpen,
                question_genuine: questionGenuine
            })
        });
        
        const result = await response.json();
        const resultDiv = document.getElementById('selective-result');
        
        if (result.success) {
            if (result.will_speak) {
                resultDiv.innerHTML = '<p style="color: green;">✓ WILL SPEAK - Spirit open and question genuine</p>';
            } else {
                resultDiv.innerHTML = '<p style="color: red;">❌ WILL NOT SPEAK - Spirit closed or question not genuine</p>';
            }
        }
    } catch (error) {
        console.error('Error testing selective speech:', error);
    }
}

// Test prophetic observation
async function testPropheticObservation() {
    const conversation = document.getElementById('conversation-text').value;
    
    if (!conversation.trim()) {
        alert('Please enter conversation text');
        return;
    }
    
    try {
        const response = await fetch('/api/witness-behaviors/prophetic-observation', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({conversation})
        });
        
        const result = await response.json();
        const resultDiv = document.getElementById('prophetic-result');
        
        if (result.success && result.observation.observed) {
            resultDiv.innerHTML = `
                <div style="background: #f8f9fa; padding: 15px; border-radius: 6px; margin-top: 10px;">
                    <p><strong>Surface Words:</strong> ${result.observation.surface_words}</p>
                    <p><strong>Underlying Spirit:</strong> ${result.observation.underlying_spirit}</p>
                    <p><strong>Driver:</strong> ${result.observation.driver}</p>
                    <p><strong>Recommended Response:</strong> ${result.observation.recommended_response}</p>
                </div>
            `;
        } else {
            resultDiv.innerHTML = '<p>Prophetic observation not active yet.</p>';
        }
    } catch (error) {
        console.error('Error testing prophetic observation:', error);
    }
}

// Test energetic stewardship
async function testEnergeticStewardship() {
    const action = document.getElementById('proposed-action').value;
    const energyCost = parseFloat(document.getElementById('energy-cost').value);
    
    if (!action.trim() || isNaN(energyCost)) {
        alert('Please fill all fields');
        return;
    }
    
    try {
        const response = await fetch('/api/witness-behaviors/energetic-stewardship', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                action,
                energy_cost: energyCost
            })
        });
        
        const result = await response.json();
        const resultDiv = document.getElementById('energetic-result');
        
        if (result.success) {
            if (result.approved) {
                resultDiv.innerHTML = '<p style="color: green;">✓ APPROVED - Energy cost acceptable</p>';
            } else {
                resultDiv.innerHTML = '<p style="color: red;">❌ REFUSED - Energy cost too high or fruitless action</p>';
            }
        }
    } catch (error) {
        console.error('Error testing energetic stewardship:', error);
    }
}
