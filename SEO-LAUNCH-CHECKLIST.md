# C Jackson Plumbing: SEO launch checklist

The site is built to rank, but it can only rank once it is live on **www.cjacksonplumbing.com**.
The GitHub preview is deliberately hidden from Google (noindex).

## 1. Launch the site (one-off)

1. Build the launch version: `python3 build.py --live`
   This removes the noindex tags and the "design preview" footer note.
2. Point www.cjacksonplumbing.com at the new host (GitHub Pages, Netlify or similar) and
   switch off the old Weebly site. Keep the domain itself.
3. Check the old page addresses still work. They redirect automatically:
   - /installations.html → Our work
   - /testimonials.html → Reviews
   - /contact.html → Quote form
4. Connect the quote form to a form service (Formspree, Netlify Forms) so enquiries arrive by email.

## 2. Google Search Console (day of launch)

1. Add the property for https://www.cjacksonplumbing.com and verify it.
2. Submit the sitemap: https://www.cjacksonplumbing.com/sitemap.xml
3. Use "URL inspection" → "Request indexing" on the homepage and the four service pages.
4. Do the same in **Bing Webmaster Tools** (import from Search Console). ChatGPT search and
   Microsoft Copilot use Bing's index, so this matters for AI answers.

## 3. Google Business Profile (the biggest factor for "plumber Castleford")

The map results at the top of Google for local searches come from Business Profiles, not websites.

- Claim or create the profile at business.google.com.
- Primary category: **Plumber**. Secondary: **Bathroom remodeler**, **Kitchen remodeler**.
- Service areas: Castleford, Pontefract, Methley, Rothwell, Garforth, Kippax, Leeds.
- Hours: open 24 hours (matches the 24-hour emergency line).
- Website: https://www.cjacksonplumbing.com
- Add 20+ real photos: the before/during/after sets in the site's img folder are ideal.
- Name, address and phone must match the website exactly:
  C Jackson Plumbing · 75 Lower Oxford Street, Castleford WF10 4AF · 01977 309 517

## 4. Reviews (the second biggest factor, and what AI assistants quote)

- Ask every past customer on the website (Pat, Steve, Joanne, Richard, Paul, Jilly, Meg, Jonathan, Jason)
  to leave the same review on Google. Send them the direct review link from the Business Profile.
- After every job from now on, text the customer the review link on the day of handover.
- Reply to every review, mentioning the job and the town (e.g. "bathroom in Pontefract").

## 5. Directory listings (citations)

Create or update these with identical name, address and phone. AI assistants and Google both
cross-check them:

- Bing Places for Business (feeds ChatGPT and Copilot)
- Apple Business Connect (Apple Maps and Siri)
- Checkatrade, MyBuilder or TrustATrader (pick at least one and collect reviews there too)
- Yell.com, Thomson Local, Facebook page

Once the Google Business Profile URL exists, add it and the directory URLs to the `sameAs`
list in the business schema in build.py, then rebuild.

## 6. Ongoing (monthly)

- Add each finished job to the work page with before/during/after photos and the town name.
- Post the same photos to the Google Business Profile.
- Check Search Console for the search terms people use and which pages show up.

## What's already built in

- Keyword-targeted pages: bathroom fitters, kitchen fitters, plumbing & heating, 24-hour emergency
  plumber, and an areas page with real reviews from each town.
- Structured data on every page (Plumber business, services, breadcrumbs, FAQs).
- FAQ answers written in plain question-and-answer form, which AI search engines quote directly.
- llms.txt: a plain-text summary of the business for AI assistants.
- robots.txt that welcomes Google, Bing and AI crawlers, plus an XML sitemap.
- Fast pages: compressed images, phone-sized photos, no heavy scripts.
