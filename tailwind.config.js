const defaultTheme = require("tailwindcss/defaultTheme")

module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily: {
        'font-sans-kr': ['Noto Sans KR', defaultTheme.fontFamily.serif]
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
