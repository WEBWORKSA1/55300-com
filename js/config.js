/* 55300.com — site configuration. Edit here; no rebuild needed.
   Payment links are optional. When a link is empty, the matching button
   opens the pledge form instead, and the team replies with a secure payment link. */
window.SITE_CONFIG = {
  brand: "55300",
  interestUrl: "https://web.works/contact",
  // Optional hosted payment links (PayPal donate button URL, Stripe Payment Link, Buy Me a Coffee, Ko-fi)
  payments: {
    paypal: "",
    stripe: "",
    buymeacoffee: "",
    kofi: ""
  },
  // Donation goal shown on the Support page
  goal: { label: "2026–27 operations & contest prize pool", target: 25000, raised: 0 },
  youtubeChannel: "" // optional: your channel URL for the Videos page "Subscribe" button
};
