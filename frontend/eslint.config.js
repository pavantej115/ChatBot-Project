module.exports = [
    {
      files: ['*.js'],
      languageOptions: {
        ecmaVersion: 2021,
      },
      rules: {
        'no-unused-vars': 'warn',
        'no-console': 'off',
        'semi': ['error', 'always'],
        'quotes': ['error', 'single'],
      },
    },
  ];
