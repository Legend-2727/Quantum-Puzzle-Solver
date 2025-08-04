// Simple animation system
function addScrollAnimations() {
    const elements = document.querySelectorAll('.stMarkdown, .stColumns, .stSelectbox, .stButton, .stSlider, .stMetric, .stProgress, .stAlert, .stCodeBlock, .stImage, .stPlotlyChart, .algorithm-section, .algorithm-button');
    
    elements.forEach((element, index) => {
        setTimeout(() => {
            element.classList.add('animate');
        }, index * 100);
    });
}

// Initialize animations when page loads
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(addScrollAnimations, 500);
});

// Re-initialize after Streamlit updates
if (typeof window !== 'undefined') {
    const originalPushState = history.pushState;
    history.pushState = function() {
        originalPushState.apply(history, arguments);
        setTimeout(addScrollAnimations, 100);
    };
}

// Simple algorithm button handling
function setupAlgorithmButtons() {
    const buttons = document.querySelectorAll('[data-algorithm]');
    buttons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const algorithm = button.getAttribute('data-algorithm');
            
            // Update button states
            document.querySelectorAll('.algorithm-button').forEach(btn => {
                btn.classList.remove('selected');
            });
            
            button.classList.add('selected');
            
            // Update display
            const displayElement = document.getElementById('selected-algorithm-display');
            if (displayElement) {
                displayElement.textContent = algorithm;
            }
        });
    });
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(setupAlgorithmButtons, 500);
}); 