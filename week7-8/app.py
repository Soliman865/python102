# app.py — Reference Implementation
# Week 8: AI Weather Mood App — Tkinter GUI
#
# This is the reference — try building your own version with AI first (see README.md).
# Run: python app.py
# Requires: pip install requests  (for weather.py)

import tkinter as tk
from tkinter import font as tkfont
from weather import get_weather, get_mood

# ============================================================
# MOOD → VISUAL STYLE MAPPING
# Each mood gets: a background colour, an emoji, and a text colour
# ============================================================
MOOD_STYLES = {
    "sunny":   {"bg": "#FFD97D", "emoji": "☀️",  "fg": "#5D4037"},
    "cloudy":  {"bg": "#B0BEC5", "emoji": "☁️",  "fg": "#263238"},
    "rainy":   {"bg": "#5C9BD6", "emoji": "🌧️", "fg": "#FFFFFF"},
    "stormy":  {"bg": "#546E7A", "emoji": "⛈️",  "fg": "#FFFFFF"},
    "snowy":   {"bg": "#E3F2FD", "emoji": "❄️",  "fg": "#1565C0"},
    "foggy":   {"bg": "#CFD8DC", "emoji": "🌫️", "fg": "#37474F"},
    "unknown": {"bg": "#ECEFF1", "emoji": "🌡️", "fg": "#546E7A"},
}

# Default style shown on startup
DEFAULT_STYLE = MOOD_STYLES["unknown"]


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Mood App")
        self.root.geometry("420x520")
        self.root.resizable(False, False)

        self._build_ui()
        self._apply_style(DEFAULT_STYLE)

    # ----------------------------------------------------------
    # UI CONSTRUCTION
    # ----------------------------------------------------------

    def _build_ui(self):
        # --- Search bar at the top ---
        search_frame = tk.Frame(self.root, pady=16)
        search_frame.pack(fill="x", padx=20)

        self.city_entry = tk.Entry(
            search_frame, font=("Helvetica", 14), width=22, relief="flat",
            bd=2, highlightthickness=1, highlightbackground="#BDBDBD"
        )
        self.city_entry.pack(side="left", ipady=6)
        self.city_entry.insert(0, "Enter a city…")
        self.city_entry.bind("<FocusIn>",  self._clear_placeholder)
        self.city_entry.bind("<FocusOut>", self._restore_placeholder)
        self.city_entry.bind("<Return>",   self._on_search)   # Enter key works too

        search_btn = tk.Button(
            search_frame, text="Search", font=("Helvetica", 13, "bold"),
            command=self._on_search, relief="flat", padx=12, pady=6,
            bg="#546E7A", fg="white", activebackground="#455A64", cursor="hand2"
        )
        search_btn.pack(side="left", padx=(8, 0))

        # --- Main display area ---
        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack(expand=True, fill="both")

        # Emoji — large, centred
        self.emoji_label = tk.Label(
            self.display_frame, text="🌡️",
            font=("Helvetica", 80)
        )
        self.emoji_label.pack(pady=(30, 8))

        # Temperature — big
        self.temp_label = tk.Label(
            self.display_frame, text="-- °C",
            font=("Helvetica", 42, "bold")
        )
        self.temp_label.pack()

        # "Feels like" line
        self.feels_label = tk.Label(
            self.display_frame, text="",
            font=("Helvetica", 13)
        )
        self.feels_label.pack(pady=(2, 0))

        # City + country
        self.city_label = tk.Label(
            self.display_frame, text="Search for a city",
            font=("Helvetica", 18, "bold")
        )
        self.city_label.pack(pady=(14, 2))

        # Description + humidity + wind
        self.desc_label = tk.Label(
            self.display_frame, text="",
            font=("Helvetica", 13)
        )
        self.desc_label.pack()

        self.detail_label = tk.Label(
            self.display_frame, text="",
            font=("Helvetica", 12)
        )
        self.detail_label.pack(pady=(4, 0))

        # Error message (hidden until needed)
        self.error_label = tk.Label(
            self.display_frame, text="",
            font=("Helvetica", 13), fg="red"
        )
        self.error_label.pack(pady=(12, 0))

    # ----------------------------------------------------------
    # EVENT HANDLERS
    # ----------------------------------------------------------

    def _on_search(self, event=None):
        city = self.city_entry.get().strip()
        if not city or city == "Enter a city…":
            return

        self.error_label.config(text="")   # clear any previous error

        try:
            weather = get_weather(city)
            mood    = get_mood(weather["condition"])
            self._update_display(weather, mood)

        except ValueError:
            # City not found
            self._show_error("City not found. Check the spelling and try again.")
        except RuntimeError as e:
            self._show_error(f"API error — {e}")
        except Exception:
            self._show_error("Something went wrong. Try again.")

    def _clear_placeholder(self, event):
        if self.city_entry.get() == "Enter a city…":
            self.city_entry.delete(0, "end")

    def _restore_placeholder(self, event):
        if not self.city_entry.get():
            self.city_entry.insert(0, "Enter a city…")

    # ----------------------------------------------------------
    # DISPLAY UPDATE
    # ----------------------------------------------------------

    def _update_display(self, weather, mood):
        style = MOOD_STYLES.get(mood, MOOD_STYLES["unknown"])
        self._apply_style(style)

        self.emoji_label.config(text=style["emoji"])
        self.temp_label.config(text=f"{weather['temp']}°C")
        self.feels_label.config(text=f"Feels like {weather['feels_like']}°C")
        self.city_label.config(text=f"{weather['city']}, {weather['country']}")
        self.desc_label.config(text=weather["description"])
        self.detail_label.config(
            text=f"💧 {weather['humidity']}% humidity  •  💨 {weather['wind_speed']} m/s"
        )

    def _apply_style(self, style):
        """Set background and foreground colour on every widget that needs it."""
        bg = style["bg"]
        fg = style["fg"]

        self.root.config(bg=bg)
        self.display_frame.config(bg=bg)

        # Every label's background must match the window background,
        # otherwise you'll see grey boxes behind the text.
        for widget in [
            self.emoji_label, self.temp_label, self.feels_label,
            self.city_label, self.desc_label, self.detail_label,
        ]:
            widget.config(bg=bg, fg=fg)

        self.error_label.config(bg=bg)
        search_frame = self.root.winfo_children()[0]
        search_frame.config(bg=bg)

    def _show_error(self, message):
        # Reset to default style and show the error message in red
        self._apply_style(DEFAULT_STYLE)
        self.emoji_label.config(text=DEFAULT_STYLE["emoji"])
        self.temp_label.config(text="-- °C")
        self.feels_label.config(text="")
        self.city_label.config(text="Search for a city")
        self.desc_label.config(text="")
        self.detail_label.config(text="")
        self.error_label.config(text=message)


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
