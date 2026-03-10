# LaunchDarkly SE Homework – Feature Flag Demo

## Overview

This project demonstrates:

• Feature release control using LaunchDarkly  
• Rule-based targeting using context attributes  
• Real-time UI updates without page reload  
• Operational remediation (kill switch) behavior  

The application is built using Flask and the LaunchDarkly Server-side SDK.

---

## What This App Does

The application contains a feature flag:

`new-landing-component`

When the flag evaluates to **true**, the page shows:

→ NEW LANDING COMPONENT  

When the flag evaluates to **false**, the page shows:

→ OLD LANDING  

The UI updates automatically without page refresh.

---

## Targeting Demonstration

The app sends context attributes:

- key (user identifier)
- plan (free / pro)
- region (us / eu)

In LaunchDarkly:

Rule example:
If `plan` is one of `pro`
→ serve TRUE

Default rule:
→ serve FALSE

This allows targeted rollout to only Pro users.

---

## Remediation (Kill Switch)

The app includes a remediation endpoint:

POST `/remediate`

When triggered:
- The feature is forced OFF immediately
- Even if LaunchDarkly returns true

A “Clear Remediation” button restores normal targeting behavior.

This simulates operational rollback.

---

## Setup Instructions

### 1. Install Dependencies

### 2. Configure SDK Key

In `app.py`, replace:

With your **Server-side SDK key** from the LaunchDarkly Test environment.

⚠️ Do not commit real SDK keys to GitHub.

---

## Run the Application
python3 app.py

Open:

http://localhost:5001

---

## How to Test

1. Set Plan = free  
   → OLD landing page  

2. Set Plan = pro  
   → NEW landing page  

3. Click 🚨 Remediate  
   → Forces OLD landing  

4. Click ✅ Clear Remediation  
   → Restores targeting behavior  

---

## Notes

• Uses LaunchDarkly Server-side SDK  
• Context evaluation via `variation()`  
• Remediation implemented locally for demonstration purposes  
• Designed for SE technical evaluation exercise  
