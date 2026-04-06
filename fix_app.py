import sys

file_path = 'c:/Users/rayis/OneDrive/Desktop/ai/portfolio/js/app.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '    const certIcons = {'
if target in content:
    idx = content.find(target)
    base_content = content[:idx]
    
    new_end = '''    const certIcons = {
        python: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>`,
        web: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>`,
        git: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M6 21V9a9 9 0 0 0 9 9"/></svg>`,
        ai: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>`,
        data: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>`,
        default: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>`
    };

    DOM.certificationsGrid.innerHTML = CERTIFICATIONS.map(cert => `
        <div class="cert-card glass-card reveal-up">
            <div class="cert-icon-wrapper">
                ${certIcons[cert.icon] || certIcons['default']}
            </div>
            <div class="cert-body">
                <h3 class="cert-title">${cert.title}</h3>
                <p class="cert-issuer">${cert.issuer}</p>
                ${cert.description ? `<p class="cert-description">${cert.description}</p>` : ''}
                <div class="cert-footer">
                    <span class="cert-date">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14">
                            <rect x="3" y="4" width="18" height="18" rx="2"/>
                            <line x1="16" y1="2" x2="16" y2="6"/>
                            <line x1="8" y1="2" x2="8" y2="6"/>
                            <line x1="3" y1="10" x2="21" y2="10"/>
                        </svg>
                        ${formatDate(cert.date)}
                    </span>
                    ${cert.pdfUrl ? `
                        <a href="${cert.pdfUrl}" class="cert-verify-link" target="_blank" rel="noopener">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                                <polyline points="14 2 14 8 20 8"/>
                                <line x1="16" y1="13" x2="8" y2="13"/>
                                <line x1="16" y1="17" x2="8" y2="17"/>
                                <polyline points="10 9 9 9 8 9"/>
                            </svg>
                            View PDF
                        </a>
                    ` : ''}
                </div>
            </div>
        </div>
    `).join('');
}

// ============================================================
// 20. CUSTOM CURSOR
// ============================================================
function initCustomCursor() {
    if (!DOM.customCursor || !DOM.customCursorFollower) return;
    
    document.addEventListener('mousemove', (e) => {
        DOM.customCursor.style.left = e.clientX + 'px';
        DOM.customCursor.style.top = e.clientY + 'px';
        
        // Slight delay for the follower
        setTimeout(() => {
            if(DOM.customCursorFollower) {
                DOM.customCursorFollower.style.left = e.clientX + 'px';
                DOM.customCursorFollower.style.top = e.clientY + 'px';
            }
        }, 50);
    });

    // Add hover effect for clickable elements
    const clickables = document.querySelectorAll('a, button, .btn, .project-card, .cert-card, .filter-btn, .hamburger');
    clickables.forEach(el => {
        el.addEventListener('mouseenter', () => {
            DOM.customCursor.classList.add('hover');
            DOM.customCursorFollower.classList.add('hover');
        });
        el.addEventListener('mouseleave', () => {
            DOM.customCursor.classList.remove('hover');
            DOM.customCursorFollower.classList.remove('hover');
        });
    });
}

// ============================================================
// 21. 3D TILT EFFECT
// ============================================================
function init3DTilt() {
    // Only init if device supports hover
    if (window.matchMedia("(hover: none)").matches) return;

    // Mutation observer to attach listeners to newly rendered cards
    const observer = new MutationObserver(() => {
        attachTiltListeners();
    });
    
    if (DOM.projectsGrid) observer.observe(DOM.projectsGrid, { childList: true });
    if (DOM.certificationsGrid) observer.observe(DOM.certificationsGrid, { childList: true });
    
    attachTiltListeners();

    function attachTiltListeners() {
        // Re-calculate all valid cards
        const cards = document.querySelectorAll('.project-card, .cert-card, .bio-card, .contact-info-card, .contact-form');
        cards.forEach(card => {
            // Remove old to prevent duplicate events
            card.removeEventListener('mousemove', handleTilt);
            card.removeEventListener('mouseleave', resetTilt);
            
            card.addEventListener('mousemove', handleTilt);
            card.addEventListener('mouseleave', resetTilt);
        });
    }

    function handleTilt(e) {
        // Don't tilt if elements are hidden/hiding
        if(this.classList.contains('hiding')) return;

        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = ((y - centerY) / centerY) * -10;
        const rotateY = ((x - centerX) / centerX) * 10;
        
        this.style.transition = 'none'; // Snap to mouse instantly as it moves
        this.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
        
        // Glare effect logic can be placed here if desired
    }

    function resetTilt(e) {
        this.style.transition = 'transform 0.4s ease'; // Smooth snap back
        this.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
    }
}

// ============================================================
// 22. SYSTEM CLOCK
// ============================================================
function initSystemClock() {
    const clockEl = document.getElementById('sys-time');
    if (!clockEl) return;

    function updateClock() {
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        clockEl.textContent = `${hours}:${minutes}:${seconds} IST`;
    }

    updateClock();
    setInterval(updateClock, 1000);
}
'''
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(base_content + new_end)
    print("Cleaned up app.js successfully.")
else:
    print("Target string not found in app.js")
