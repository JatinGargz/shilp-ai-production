import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        kk: {
          primary: "#5C1A1A",        // Deep Maroon Primary
          primaryHover: "#441212",
          accent: "#B85D2F",         // Warm Terracotta Accent
          camel: "#B78B6A",          // Camel / Light Accent
          canvas: "#F8F1E7",         // Cream Background
          card: "#FFFFFF",
          cardWarm: "#F4EBDD",
          textDark: "#2E1F17",       // Dark Text
          textMuted: "#7A6B62",
          border: "#E6D8C8",
          success: "#2E7D32",
          warning: "#D97706",
          danger: "#C62828"
        }
      },
      fontFamily: {
        serif: ["var(--font-playfair)", "Georgia", "serif"],
        sans: ["var(--font-inter)", "system-ui", "sans-serif"],
      },
      borderRadius: {
        card: "16px",
      }
    },
  },
  plugins: [],
};
export default config;
