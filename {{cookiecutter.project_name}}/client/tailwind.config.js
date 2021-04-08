module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },
    borderRadius: {
      none: '0',
      sm: '.125rem',
      DEFAULT: '.25rem',
      lg: '.5rem',
      full: '9999px',
    },
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    extend: {
      colors: {
        // gray: {
        //   100: '#f7fafc',
        //   // ...
        //   900: '#1a202c',
        // },
        gray: {
          100: '#dedede',
          200: '#d4d4d4',
        },
        primary: '#03c2fc',
        secondary: '#009ecf',
        charcoal: '#333333',
      },
      borderWidth: {
        3: '3px',
      },
      ringWidth: {
        3: '3px',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [require('@tailwindcss/forms')],
}
