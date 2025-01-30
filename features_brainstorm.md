# Feature List for Upgrade & Churn Prediction Models

---

For both models, we should add the features that we currently have for the current prediction model.

## Common Features (Applicable to Both Models)

### Data Available at User Sign Up

- Previous account deletion history (if detectable)
- Industry (e.g., e-commerce, logistics, retail)
- Company size (expected order count, driver count)
- Geographic region (country, urban/rural)
- User role (owner, manager, team member)
- Referral source (organic search, paid ad, partner, referral program)
- Number of fields completed in sign-up form
- Onboarding completion rate (% of steps finished)
- Team member invitations sent/accepted
- Support tickets raised in first 48 hours/7 days/...
- First feature used post-signup
- Multiple email verification attempts
- Password reset in first 24 hours

### User's Daily Data

- Payment method provided (credit card, PayPal, none)
- Account type (free trial, freemium, paid tier)
- Daily login frequency (7d/30d rolling averages)
- Session duration (median, max, variance)
- Number of drivers added in the apps
- Active days in last 14 days
- Core feature usage rate (e.g., shipment tracking, analytics)
- API call volume (for developers)
- In-app notifications clicked
- Tutorials/help articles/documentation viewed
- Feature adoption latency (time to first use)
- Device type consistency (e.g., mobile-to-desktop ratio)
- Clicks on "Compare Plans" page
- Payment success/failure history
- Customer support ticket frequency
- Support interaction sentiment (NLP analysis)
- Responses to in-app surveys
- Integration used?
- 30-day login trend (slope calculation)
- "Last active" date recency
- Feature abandonment sequence (e.g., stopped using analytics → stopped using tracking)

---

## Upgrade Prediction Model

### Data Available at User Sign Up

### User's Daily Data

---

## Churn Prediction Model

### Data Available at User Sign Up

### User's Daily Data
