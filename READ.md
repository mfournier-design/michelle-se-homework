# LaunchDarkly SE Homework – Feature Flag & Targeting Demo

## Overview

This repository contains a minimal Flask application built for the LaunchDarkly Solutions Engineering technical exercise.

The application demonstrates:

- Feature release control using a LaunchDarkly flag
- Rule-based targeting using context attributes
- Real-time UI updates without page reload
- Operational remediation (kill switch) behavior

The feature under control is a "New Landing Component" that replaces an "Old Landing Component" when the flag evaluates to `true`.

---

## Architecture Summary

- Python (Flask)
- LaunchDarkly Server-side SDK
- Context built using `Context.builder(key)`
- Flag evaluated using `variation()`
- Remediation implemented as an application-level override
- UI updates via polling (`loadFlag()` runs every 2 seconds)

---

## Feature Flag Configuration (LaunchDarkly)

Create a boolean feature flag with:

- **Flag Key:** `new-landing-component`
- **Environment:** Test
- **Default Rule:** Serve `false`

Add a targeting rule:

- Context Kind: `user`
- Attribute: `plan`
- Operator: `is one of`
- Value: `pro`
- Serve: `true`

This configuration enables the feature only for Pro users.

---

## Setup Instructions

### 1. Clone the Repository

### 2. Install Dependencies

### 3. Configure LaunchDarkly SDK Key

Log into LaunchDarkly:

1. Navigate to your project
2. Go to **Project Settings → Environments**
3. Select the **Test** environment
4. Copy the **Server-side SDK key** (NOT the client-side ID)

Open `app.py` and replace:

with your Test environment Server-side SDK key.

---

## Run the Application
python3 app.py

Open in browser:
http://localhost:5001

---

## How to Test

### Targeting Demonstration

1. Set Plan = `free`
   → OLD landing page should display

2. Set Plan = `pro`
   → NEW landing page should display

This demonstrates rule-based targeting based on context attributes.

---

### Remediation Demonstration

1. Ensure Plan = `pro` (NEW landing visible)
2. Click 🚨 Remediate (Force OFF)
   → Page immediately switches to OLD landing
3. Click ✅ Clear Remediation
   → Page returns to normal targeting behavior

This demonstrates operational rollback capability.

---

## Notes

- Context attributes used:
  - `key`
  - `plan`
  - `region`

- Flag evaluation falls back to `false` if:
  - SDK key is invalid
  - Flag is not found
  - Flag is off

- Remediation is implemented locally to simulate emergency rollback behavior without requiring LaunchDarkly API write permissions.

---

## Security Considerations

- SDK keys must be stored securely in production environments.
- This demo uses a placeholder key for safety.
- No sensitive credentials are committed to this repository.

---
