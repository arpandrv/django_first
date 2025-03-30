# Mango Surveillance Website: Focused Code Improvements

This document provides targeted analysis of specific code patterns found in the Mango Surveillance website codebase along with recommended improvements.

## 1. CSS Loading Optimization

**Current Issue:**
Currently, all CSS files are loaded on every page, regardless of whether they're needed:

```html
<link rel="stylesheet" href="{% static 'mango_app/css/base.css' %}">
<link rel="stylesheet" href="{% static 'mango_app/css/home.css' %}">
<link rel="stylesheet" href="{% static 'mango_app/css/pests.css' %}">
<link rel="stylesheet" href="{% static 'mango_app/css/diseases.css' %}">
<link rel="stylesheet" href="{% static 'mango_app/css/surveillance.css' %}">
<link rel="stylesheet" href="{% static 'mango_app/css/about.css' %}">
```

**Recommended Approach:**
Load only the CSS files needed for the current page:

```html
<link rel="stylesheet" href="{% static 'mango_app/css/base.css' %}">
{% if active_section.is_home %}
    <link rel="stylesheet" href="{% static 'mango_app/css/home.css' %}">
{% elif active_section.is_pests %}
    <link rel="stylesheet" href="{% static 'mango_app/css/pests.css' %}">
{% elif active_section.is_diseases %}
    <link rel="stylesheet" href="{% static 'mango_app/css/diseases.css' %}">
{% endif %}
```



## 2. CSS Variables Implementation

**Current Issue:**
Color values, spacing measurements, and other design constants are repeated throughout the CSS files:

```css
.card {
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
}
```

**Recommended Approach:**
Implement CSS variables (custom properties) to centralize design values:

```css
:root {
    --primary-color: #2e7d32;
    --primary-dark: #1b5e20;
    --primary-light: #e8f5e9;
    --text-color: #333;
    --bg-color: #f8f8f8;
    --card-bg: #fff;
    --border-color: #ddd;
    --spacing-sm: 10px;
    --spacing-md: 15px;
    --spacing-lg: 20px;
}

/* Then use them throughout your CSS */
.card {
    background-color: var(--card-bg);
    border-radius: 5px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    padding: var(--spacing-lg);
    margin-bottom: var(--spacing-lg);
}
```



## 3. Error Handling in JavaScript

**Current Issue:**
Some JavaScript functions lack proper error handling, which can lead to silent failures or confusing errors for users.

**Recommended Approach:**
Implement structured error handling with user-friendly messages:

```javascript
function fetchResourceData(resourceId) {
    try {
        // Code to fetch data
        return data;
    } catch (error) {
        console.error(`Error fetching resource ${resourceId}:`, error);
        // Show user-friendly error message
        showErrorMessage('Unable to load resource information. Please try again later.');
        return null;
    }
}
```



## 4. CSS Duplication Issues

### 4.1 Duplicated Button Styling

**Current Issue:**
The `.details-button` styling is duplicated across multiple CSS files with minimal variations:

```css
/* Nearly identical .details-button styling in home.css, pests.css, and diseases.css */
.details-button {
    display: inline-block;
    background-color: white;
    color: #2e7d32;
    border: 1px solid #2e7d32;
    padding: 8px 16px;  /* slight variations in padding values only */
    border-radius: 4px;
    text-decoration: none;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.3s ease;
}
```

### 4.2 Duplicated Card Component Styling

**Current Issue:**
Similar card components have duplicated styling with just different class names:

```css
/* Similar code with just different class names */
.pest-card { /* in pests.css */ }
.disease-card { /* in diseases.css */ }
.pest-content { /* in pests.css */ }
.disease-content { /* in diseases.css */ }
```

**Recommended Approach for CSS Duplication:**
Create a shared components CSS file with base classes, then extend or modify as needed:

```css
/* components.css - shared styles */
.card-base {
    display: flex;
    background-color: var(--card-bg);
    border-radius: 5px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    height: 100%;
}

.button {
    display: inline-block;
    background-color: white;
    color: var(--primary-color);
    border: 1px solid var(--primary-color);
    padding: 8px 16px;
    border-radius: 4px;
    text-decoration: none;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.3s ease;
}

/* Then in specific CSS files */
.pest-card, .disease-card {
    /* Just apply the base class */
    composes: card-base;
}

/* Or add specific modifications */
.pest-content, .disease-content {
    flex: 1;
    padding: var(--spacing-lg);
    /* Additional specific styling */
}
```



## 5. JavaScript Duplication

**Current Issue:**
Similar code blocks for table row highlighting are duplicated across different initialization functions:

```javascript
// Almost identical code in initializeDiseasePage() and initializeSurveillancePage()
tableRows.forEach(row => {
    if (!row.closest('thead')) {
        row.addEventListener('mouseenter', function () {
            this.style.backgroundColor = 'rgba(46, 125, 50, 0.1)';
        });
        
        row.addEventListener('mouseleave', function () {
            if (this.rowIndex % 2 === 0) {
                this.style.backgroundColor = '#f9f9f9';
            } else {
                this.style.backgroundColor = '';
            }
        });
    }
});
```

**Recommended Approach:**
Extract duplicated code into reusable functions:

```javascript
/**
 * Adds interactive highlighting to table rows
 * @param {string} tableSelector - CSS selector for the table
 */
function addTableRowHighlighting(tableSelector) {
    const tableRows = document.querySelectorAll(`${tableSelector} tr`);
    if (tableRows.length === 0) return;
    
    tableRows.forEach(row => {
        if (!row.closest('thead')) {
            row.addEventListener('mouseenter', function () {
                this.style.backgroundColor = 'rgba(46, 125, 50, 0.1)';
            });
            
            row.addEventListener('mouseleave', function () {
                if (this.rowIndex % 2 === 0) {
                    this.style.backgroundColor = '#f9f9f9';
                } else {
                    this.style.backgroundColor = '';
                }
            });
        }
    });
}

// Then use in different initialization functions
function initializeDiseasePage() {
    addTableRowHighlighting('.env-factors');
    // Other disease page specific code
}

function initializeSurveillancePage() {
    addTableRowHighlighting('.monitoring-table');
    // Other surveillance page specific code
}
```



## 6. Unused and Debug Code

### 6.1 Unused Image Error Handler

**Current Issue:**
An image error handler is defined but may not be fully utilized:

```javascript
window.addEventListener('load', function () {
    const images = document.querySelectorAll('img');
    // Error handler code that may not be fully utilized
});
```

### 6.2 Vestigial Dark Mode Implementation

**Current Issue:**
Dark mode functions appear to be an afterthought and not fully integrated:

```javascript
// These functions are defined at the end of the file but appear to be 
// an afterthought that's not fully integrated with the site design
addDarkModeStyles();
createThemeToggle();
```

### 6.3 Debug Console Logs

**Current Issue:**
Debug console logs remain in the production code:

```javascript
console.log('Home page initialized');
console.log('Pest page initialized');
// etc.
```

### 6.4 Overly Specific CSS Selectors

**Current Issue:**
Some CSS selectors are unnecessarily specific:

```css
/* Overly specific selectors that could be simplified */
body.dark-mode .card h2,
body.dark-mode .card h3 { ... }
```

**Recommended Approach for Unused Code:**
1. Remove or properly implement the image error handler
2. Either fully integrate dark mode or remove it
3. Remove all console.log statements from production code
4. Simplify CSS selectors where possible

```css
/* Simplified selectors */
.dark-mode .card-heading { ... }
```




