export default [
    {
      files: ['*.js'],
      languageOptions: {
        ecmaVersion: 2021,
      },
      rules: {
        // Example rules
        'no-unused-vars': 'warn',
        'no-console': 'off',
        'semi': ['error', 'always'],
        'quotes': ['error', 'single'],
      },
    },
  ];
