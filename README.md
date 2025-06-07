# wofigpt

🧠 A Wofi-based AI and web search launcher — search Google or ask ChatGPT from your Wayland desktop using a minimal popup UI.

## ✨ Features

- 🔍 Google search directly from Wofi
- 🤖 Ask ChatGPT with optional auto-typing support
- 🚫 Auto-closes if Wofi is already open
- ⚡ Fast, keyboard-driven interface
- 🪟 Works well with Hyprland and other Wayland compositors

## 📦 Dependencies

- [wofi](https://github.com/SimplyCEO/wofi)
- `xdg-open` (typically preinstalled)
- `xdotool` *(optional)* — for simulating typing into the browser
- `notify-send` *(for fallback notification)*

## 🚀 Installation

### Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/wofigpt.git
cd wofigpt
chmod +x wofigpt.py
```

## ⌨️ Suggested Keybind (Hyprland Example)
`bind = SUPER, D, exec, ~/path-to-wofigpt.py`
