# Platform rules relevant to onboarding

Checked 2026-10-29. Paraphrased; open the link for the exact wording. Guidelines change often, so re-check the links before relying on them.

## Apple: App Review Guidelines (https://developer.apple.com/app-store/review/guidelines/)

| Rule | Plain summary | URL |
|---|---|---|
| 5.1.1(v) Account sign-in | If the app has no significant account-based features, let people use it without logging in. If you offer account creation, you must offer account deletion in the app. Don't require personal information unless it is core to the app or legally required. | https://developer.apple.com/app-store/review/guidelines/#data-collection-and-storage |
| 4.8 Login Services | If a third-party or social login (Google, Facebook, X…) sets up the primary account, also offer an equivalent login that limits data to name and email, lets the user hide their email, and doesn't track for ads without consent. (Apps using only their own account system are exempt.) | https://developer.apple.com/app-store/review/guidelines/#login-services |
| 5.1.1(ii) Permission | Collecting user or usage data needs consent. Paid features must not depend on granting data access. Withdrawing consent must be easy. Purpose strings must clearly and fully explain the use. | https://developer.apple.com/app-store/review/guidelines/#data-collection-and-storage |
| 5.1.1(iii) Data minimization | Prefer system pickers or share sheets over full access to Photos or Contacts. | https://developer.apple.com/app-store/review/guidelines/#data-collection-and-storage |
| 5.1.1(iv) Access | Respect permission settings. Don't manipulate, trick or force consent to unnecessary data access. Offer an alternative when consent is declined (e.g. manual address entry if location is declined). This is the rule that governs pre-prompt screens. | https://developer.apple.com/app-store/review/guidelines/#data-collection-and-storage |
| 5.1.2(i) Tracking / ATT | Tracking requires explicit permission through the ATT prompt. Don't require users to enable system features (push, location, tracking) to use the app or to get rewards. | https://developer.apple.com/app-store/review/guidelines/#data-use-and-sharing |
| 3.1.2(a) Subscriptions: free trials | Auto-renewable subscriptions may offer a free trial, configured through App Store Connect. | https://developer.apple.com/app-store/review/guidelines/#subscriptions |
| 3.1.2(c) Subscription information | Before asking someone to subscribe, clearly describe what they get for the price. | https://developer.apple.com/app-store/review/guidelines/#subscriptions |
| 3.1.1 In-App Purchase | Unlocking features or subscriptions must use IAP. A non-subscription trial must state its duration, what is lost at the end, and any charges that follow. | https://developer.apple.com/app-store/review/guidelines/#in-app-purchase |
| 2.3 / 2.3.2 Accurate metadata | Store screenshots and descriptions must match the real experience and make clear what requires purchase. Applies to onboarding promises shown in the store. | https://developer.apple.com/app-store/review/guidelines/#accurate-metadata |

## Apple: User privacy and data use / ATT (https://developer.apple.com/app-store/user-privacy-and-data-use/)

| Rule | Plain summary | URL |
|---|---|---|
| Custom message before ATT | Allowed if it is transparent about how data is used, and must not manipulate (ties to 5.1.1(iv)). | https://developer.apple.com/app-store/user-privacy-and-data-use/ |
| No incentives for tracking | You can't reward users for allowing tracking (5.1.2(i)). | https://developer.apple.com/app-store/user-privacy-and-data-use/ |
| No gating on tracking | Features can't depend on agreeing to tracking. | https://developer.apple.com/app-store/user-privacy-and-data-use/ |
| Respect the ATT answer | The ATT choice wins even if another consent dialog says otherwise. The prompt text comes from the NSUserTrackingUsageDescription purpose string. | https://developer.apple.com/app-store/user-privacy-and-data-use/ |

## Apple: Human Interface Guidelines

| Rule | Plain summary | URL |
|---|---|---|
| HIG Privacy: when to ask | Ask only when a feature needs access, ideally at first use. Avoid asking at launch unless the app can't work without it. | https://developer.apple.com/design/human-interface-guidelines/privacy |
| HIG Privacy: purpose strings | One short, complete, specific sentence on how and why ("…records at night to detect snoring"). No vague "better experience" and no bare commands. | https://developer.apple.com/design/human-interface-guidelines/privacy |
| HIG Privacy: pre-alert screens | Optional. One button only, labelled "Continue" or "Next" (never "Allow"). No Cancel or Close unless legally required. Must not look like or mirror the system alert. No pictures of the alert, no arrows or highlights on its Allow button. No incentives, and no withholding features until the user allows. | https://developer.apple.com/design/human-interface-guidelines/privacy |
| HIG Privacy: ATT pre-alert | A benefits screen is OK in some cases. If you track from launch, show the ATT alert before collecting any tracking data. Any confusing or misleading pre-ATT screen leads to rejection. Legal consent screens before or after ATT are allowed. | https://developer.apple.com/design/human-interface-guidelines/privacy |
| HIG Onboarding: keep it brief | Short, enjoyable, little to memorize. Prefer interactive teaching and in-context tips (TipKit) over long tutorials. | https://developer.apple.com/design/human-interface-guidelines/onboarding |
| HIG Onboarding: tutorials optional | If skipped, don't auto-show it again. Make it findable later. | https://developer.apple.com/design/human-interface-guidelines/onboarding |
| HIG Onboarding: defer setup | Postpone nonessential setup and customization, and use sensible defaults. | https://developer.apple.com/design/human-interface-guidelines/onboarding |
| HIG Onboarding: permissions | Request during onboarding only if the app can't function without the data. Otherwise ask at first use of the feature. | https://developer.apple.com/design/human-interface-guidelines/onboarding |
| HIG Onboarding: no license screens | Don't show licensing details in onboarding (the App Store handles agreements). If unavoidable, keep them unobtrusive. | https://developer.apple.com/design/human-interface-guidelines/onboarding |
| HIG Onboarding: ratings and purchases | Ask for ratings or purchases only after people have engaged with the app. (In tension with onboarding hard paywalls. Not an App Review rule, but worth flagging.) | https://developer.apple.com/design/human-interface-guidelines/onboarding |
| HIG Sign in with Apple: delay sign-in | Ask for sign-in only when it delivers value. Let people explore first. If an account is required, explain why. In commerce, create the account after purchase. | https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple |

## Apple: 2025–2026 changes

| Change | What it means for onboarding | URL |
|---|---|---|
| June 2025: new 3.2.2(x) | Apps may incentivise users to take actions inside the app (moved from 3.1.2(a)). Rewards for tracking or for enabling system permissions remain banned (5.1.2(i)) | https://developer.apple.com/news/?id=r9dcmrvs |
| May 2025, US storefront only | Buttons and links to web purchase allowed (3.1.1, 3.1.3), so an onboarding paywall can hand off to web checkout in the US | https://mjtsai.com/blog/2025/05/02/app-review-guidelines-updated-for-epic-anti-steering/ |
| June 2026 | No change announced to 3.1.2 or 5.1.1. 4.3 now lets Apple remove low-value apps in saturated categories (dating and fortune telling are named) | https://developer.apple.com/news/?id=a233fmpw |

## Kids apps

| Rule | Plain summary | URL |
|---|---|---|
| Apple 1.3 Kids Category | No links out, purchases or other distractions for kids unless behind a parental gate; no third-party analytics or ads | https://developer.apple.com/app-store/review/guidelines/ |
| Apple Kids apps guidance | A parental gate is an adult-level task that must be completed to continue | https://developer.apple.com/app-store/kids-apps/ |
| Apple 5.1.4 | Ask birthdate and parental contact only to comply with COPPA or GDPR; the app must work regardless of age | https://developer.apple.com/app-store/review/guidelines/ |
| UK ICO Children's Code | No nudges that lead children to share unnecessary data or turn off privacy settings; don't pre-select an older age | https://ico.org.uk/for-organisations/guide-to-data-protection/ico-codes-of-practice/age-appropriate-design-a-code-of-practice-for-online-services/13-nudge-techniques |
| Apple 2.3.1(a) | Promoting services the app doesn't offer (e.g. iOS "virus scanners") is grounds for removal; relevant to cleaner apps | https://developer.apple.com/app-store/review/guidelines/ |

## Consumer law (US, EU)

| Rule | Status (Oct 2026) | URL |
|---|---|---|
| FTC Click-to-Cancel rule | Vacated by the Eighth Circuit on 8 July 2025; the FTC restarted rulemaking in March 2026 with no draft text. ROSCA and state auto-renewal laws still require clear trial terms and express consent | https://www.kirkland.com/publications/kirkland-alert/2025/07/eighth-circuit-blocks-ftcs-click-to-cancel-rule |
| EU Digital Fairness Act | Commission proposal expected mid-November 2026. Floated: renewal reminders, express consent before a free trial converts, easier cancellation. DSA Art. 25 and the UCPD already ban deceptive interfaces | https://www.europarl.europa.eu/legislative-train/theme-protecting-our-democracy-upholding-our-values/file-digital-fairness-act |

## Google Play / Android

| Rule | Plain summary | URL |
|---|---|---|
| Runtime permissions workflow | Request only when the user invokes the feature. Check before every use. If `shouldShowRequestPermissionRationale()` is true, show an educational screen with a "no thanks" option and don't block the user. Degrade gracefully. No full-screen blocking warnings and no pushing to Settings. Two denials make the denial permanent, so don't ask early. | https://developer.android.com/training/permissions/requesting |
| Notification permission (Android 13+) | New installs start with notifications off. Don't ask at first launch. Ask in context (bell tap, follow, order) or on a later launch. A pre-prompt is only needed when a rationale is warranted. Explain what the notifications will be. | https://developer.android.com/develop/ui/views/notifications/notification-permission |
| Prominent disclosure & consent (Play User Data policy) | When data use goes beyond what users would reasonably expect, show an in-app disclosure during normal use (not only in the privacy policy) naming the data and its use, before the runtime prompt. Consent must be an active choice. Dismissing or leaving counts as no consent. | https://support.google.com/googleplay/android-developer/answer/10144311 |
| Subscriptions policy: trials and intro offers | Before enrolment, state trial length, price, what's included, when it converts and at what price, and how to cancel, localized. Don't hide the upcoming charge behind the "free" message. The page summary also mentioned a clearly visible way to dismiss the offer and keep using the app; the exact wording is unconfirmed, so verify it before using it as a rule. | https://support.google.com/googleplay/android-developer/answer/9900533 |
