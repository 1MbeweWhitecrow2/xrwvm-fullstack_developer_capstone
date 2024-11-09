// eslint.config.js
import { defineConfig } from "eslint-define-config";

export default defineConfig([
  {
    languageOptions: {
      ecmaVersion: 2021,
      sourceType: "module",
      globals: {
        // Define environment globals here (e.g., browser or Node.js globals)
        window: true,
        document: true
      }
    },
    rules: {
      // add custom rules here if needed
    },
    ignores: ["node_modules/**"]
  }
]);



