// eslint.config.js
const defineConfig = [
  {
    languageOptions: {
      ecmaVersion: 2021,
      sourceType: "module",
      globals: {
        window: true,
        document: true
      }
    },
    rules: {
      // add custom rules here if needed
    },
    ignores: ["node_modules/**"]
  }
];

module.exports = defineConfig;




