# Rayis — Developer Portfolio

A modern, responsive developer portfolio built with vanilla HTML, CSS, and JavaScript.

## 🚀 Quick Start

### Option 1: Open directly
Just double-click `index.html` in your browser.

### Option 2: Local dev server (recommended)
```bash
npx -y serve .
```
Then visit `http://localhost:3000`

### Option 3: PowerShell script
```powershell
.\server.ps1
```

---

## 📝 How to Update Content

**All content lives in one file: `js/data.js`**

### Change your personal info
Edit the `PERSONAL_INFO` object at the top of `data.js`:
- Name, bio, tagline
- Social links (GitHub, LinkedIn, email)
- Education details
- Resume URL

### Add a new project
Add a new object to the `PROJECTS` array in `data.js`:
```javascript
{
    id: "my-new-project",          // unique ID (no spaces)
    title: "Project Name",
    subtitle: "Short tagline",
    description: "Brief description for the card",
    tags: ["Web", "Python"],       // used for filtering
    techStack: ["React", "Node"],
    image: "assets/screenshot.png", // optional
    liveUrl: "https://...",        // optional
    githubUrl: "https://...",
    featured: true,                // shows "Featured" badge
    date: "2026-05",
    details: "Long description for the detail page..."
}
```

### Add a blog post
Add to the `BLOG_POSTS` array in `data.js`.

### Add a skill
Add to the relevant category in the `SKILLS` array, or create a new category.

---

## 📁 Project Structure

```
portfolio/
├── index.html       # Single-page layout (all sections)
├── css/
│   └── styles.css   # Design system + all styles
├── js/
│   ├── data.js      # ALL content (projects, skills, blog)
│   └── app.js       # Application logic (routing, rendering)
├── assets/          # Images, screenshots, resume PDF
├── server.ps1       # Local dev server script
└── README.md        # This file
```

---

## 🌐 Deployment

### GitHub Pages (Free, Recommended)
1. Push this folder to a GitHub repository
2. Go to **Settings → Pages → Source: Deploy from branch → main**
3. Your site will be live at `https://<username>.github.io/<repo>`

### Netlify (Free)
1. Push to GitHub
2. Go to [netlify.com](https://netlify.com) → New site from Git
3. Select your repo → Deploy (no build settings needed)

### Vercel (Free)
1. Push to GitHub
2. Go to [vercel.com](https://vercel.com) → Import project
3. Deploy as static site

---

## 🎨 Customizing the Design

Edit CSS variables in `css/styles.css` under `:root`:
- `--accent-primary` — main accent color
- `--accent-secondary` — secondary accent
- `--bg-primary` — background color
- `--text-primary` — text color

---

## 📈 Future Scaling Ideas

- Add a backend with Node.js/Express for a real contact form
- Integrate a CMS like Contentful or Sanity for blog posts
- Add dark/light theme toggle
- Add project search functionality
- Add analytics (Google Analytics or Plausible)
