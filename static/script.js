// Handle resume upload
document.getElementById('uploadForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const fileInput = document.getElementById('resumeFile');
    const statusDiv = document.getElementById('uploadStatus');
    
    if (!fileInput.files[0]) {
        showStatus('Please select a file', 'error');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    
    showStatus(' Uploading and parsing resume... This may take a few seconds.', 'loading');
    
    try {
        const response = await fetch('/api/upload-resume', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (result.success) {
            showStatus(` Resume parsed successfully! Candidate: ${result.name}`, 'success');
            fileInput.value = ''; // Clear file input
            // Clear the file label
            document.querySelector('.file-label').textContent = 'Choose file (pdf,docs)';
        } else {
            showStatus(' Error: ' + (result.detail || 'Unknown error'), 'error');
        }
    } catch (error) {
        showStatus(' Upload failed: ' + error.message, 'error');
    }
});

// Search candidates
async function searchCandidates() {
    const searchInput = document.getElementById('searchInput');
    const resultsDiv = document.getElementById('searchResults');
    const query = searchInput.value.trim();
    
    if (!query) {
        resultsDiv.innerHTML = '<div class="error">Please enter search terms</div>';
        return;
    }
    
    resultsDiv.innerHTML = '<div class="loading"> Searching candidates...</div>';
    
    try {
        const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
        const result = await response.json();
        
        if (result.success) {
            displaySearchResults(result);
        } else {
            resultsDiv.innerHTML = `<div class="error">Search failed: ${result.detail}</div>`;
        }
    } catch (error) {
        resultsDiv.innerHTML = `<div class="error">Search error: ${error.message}</div>`;
    }
}

// Load all candidates
async function loadAllCandidates() {
    const candidatesDiv = document.getElementById('allCandidates');
    
    candidatesDiv.innerHTML = '<div class="loading">👥 Loading all candidates...</div>';
    
    try {
        const response = await fetch('/api/candidates');
        const result = await response.json();
        
        if (result.success) {
            displayAllCandidates(result);
        } else {
            candidatesDiv.innerHTML = `<div class="error">Failed to load candidates: ${result.detail}</div>`;
        }
    } catch (error) {
        candidatesDiv.innerHTML = `<div class="error">Error loading candidates: ${error.message}</div>`;
    }
}

function displaySearchResults(result) {
    const resultsDiv = document.getElementById('searchResults');
    
    if (result.count === 0) {
        resultsDiv.innerHTML = '<div class="error"> No candidates found matching your criteria</div>';
        return;
    }
    
    let html = `<h3> Found ${result.count} candidates for "${result.query}"</h3>`;
    
    result.results.forEach(candidate => {
        html += `
            <div class="candidate-card">
                <h3>${candidate.name || 'Unknown Name'}</h3>
                <div class="match-percentage"> Match: ${candidate.match_percentage}%</div>
                <p class="candidate-email"> ${candidate.email || 'No email'}</p>
                <p class="experience-summary"> ${candidate.experience_summary || 'No experience summary'}</p>
                <div class="skills">
                    ${candidate.key_skills.map(skill => 
                        `<span class="skill-tag">${skill}</span>`
                    ).join('')}
                </div>
            </div>
        `;
    });
    
    resultsDiv.innerHTML = html;
}

function displayAllCandidates(result) {
    const candidatesDiv = document.getElementById('allCandidates');
    
    if (result.candidates.length === 0) {
        candidatesDiv.innerHTML = '<div class="error"> No candidates in database yet</div>';
        return;
    }
    
    let html = `<h3> All Candidates (${result.candidates.length})</h3>`;
    
    result.candidates.forEach(candidate => {
        html += `
            <div class="candidate-card">
                <h3>${candidate.name || 'Unknown Name'}</h3>
                <p class="candidate-email"> ${candidate.email || 'No email'}</p>
                <p class="experience-summary"> ${candidate.experience_summary || 'No experience summary'}</p>
                <div class="skills">
                    ${candidate.skills.map(skill => 
                        `<span class="skill-tag">${skill}</span>`
                    ).join('')}
                </div>
            </div>
        `;
    });
    
    candidatesDiv.innerHTML = html;
}

function showStatus(message, type) {
    const statusDiv = document.getElementById('uploadStatus');
    statusDiv.innerHTML = `<div class="${type}">${message}</div>`;
}

// Update file label when file is selected
document.getElementById('resumeFile').addEventListener('change', function(e) {
    const fileName = e.target.files[0] ? e.target.files[0].name : 'Choose file (pdf,docs)';
    document.querySelector('.file-label').textContent = fileName;
});

// Allow pressing Enter in search input
document.getElementById('searchInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        searchCandidates();
    }
});