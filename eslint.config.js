export default [
  {
    ignores: ["docs/js/*.min.js", "docs/js/*-min.js", "docs/js/plugins.js", "docs/js/modernizr.js"]
  },
  {
    files: ["docs/js/*.js"],
    languageOptions: {
      globals: {
        browser: true,
        jquery: true,
        modernizr: true
      }
    },
    rules: {
      "no-unused-vars": "warn",
      "no-undef": "warn"
    }
  }
];
