import customtkinter as ctk
import requests

# ------------------------- FREE OPEN-METEO API FUNCTIONS -------------------------
def get_city_coordinates(city):
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        response = requests.get(url).json()
        results = response.get("results")

        if not results:
            return None, None

        lat = results[0]["latitude"]
        lon = results[0]["longitude"]
        return lat, lon
    except:
        return None, None


def get_live_weather(city):
    lat, lon = get_city_coordinates(city)

    if lat is None or lon is None:
        return "⚠ City not found. Please try another."

    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        data = requests.get(url).json()
        w = data.get("current_weather")

        if not w:
            return "⚠ Weather data unavailable."

        temp = w["temperature"]
        wind = w["windspeed"]
        code = w["weathercode"]

        # Convert weather code to readable text
        weather_conditions = {
            0: "Clear Sky", 1: "Mainly Clear", 2: "Partly Cloudy", 3: "Cloudy",
            45: "Foggy", 48: "Freezing Fog", 51: "Light Drizzle", 53: "Drizzle",
            55: "Heavy Drizzle", 56: "Freezing Drizzle", 57: "Freezing Drizzle",
            61: "Light Rain", 63: "Rain", 65: "Heavy Rain", 66: "Freezing Rain",
            67: "Freezing Rain", 71: "Light Snow", 73: "Snow", 75: "Heavy Snow",
            77: "Snow Grains", 80: "Rain Showers", 81: "Rain Showers",
            82: "Violent Rain Showers", 85: "Snow Showers", 86: "Snow Showers",
            95: "Thunderstorm", 96: "Thunderstorm", 99: "Thunderstorm"
        }
        condition = weather_conditions.get(code, "Unknown Weather")

        # Return formatted text
        return (
            f"🌤 Condition: {condition}\n"
            f"🌡 Temperature: {temp}°C\n"
            f"🌬 Wind Speed: {wind} km/h"
        )

    except:
        return "⚠ Unable to retrieve weather information."


# ------------------------- UI -------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Weather Chatbot")
root.geometry("900x650")
root.resizable(False, False)

bg = ctk.CTkFrame(root, width=820, height=560, corner_radius=45, fg_color="#1A1A1A")
bg.place(relx=0.5, rely=0.53, anchor="center")

chat_box = ctk.CTkTextbox(
    bg, width=780, height=400,
    corner_radius=38, fg_color="#0F0F0F",
    text_color="white", font=("Segoe UI Rounded", 16)
)
chat_box.place(relx=0.5, rely=0.34, anchor="center")
chat_box.configure(state="disabled")

input_frame = ctk.CTkFrame(
    bg, width=780, height=70,
    fg_color="#0E0E0E", corner_radius=30
)
input_frame.place(relx=0.5, rely=0.83, anchor="center")

input_box = ctk.CTkEntry(
    input_frame,
    width=700, height=60,
    corner_radius=30,
    fg_color="#0E0E0E",
    border_color="#0E0E0E",
    text_color="white",
    placeholder_text="your thoughts here",
    placeholder_text_color="#4E4E4E",
    font=("Segoe UI Rounded", 18)
)
input_box.place(relx=0.47, rely=0.5, anchor="center")


# ------------------------- CHAT LOGIC -------------------------
def get_bot_reply(message):
    msg = message.lower()

    # Detect weather request
    if "weather" in msg or "temperature" in msg or "rain" in msg or "forecast" in msg:
        words = msg.split()
        for w in words:
            if w not in ["weather", "temperature", "rain", "forecast", "in", "at", "the", "what", "for"]:
                return get_live_weather(w.capitalize())

        return "🌍 Please ask like: Weather in Chennai"

    return "💡 Ask me about weather like:\n• Weather in Chennai\n• Temperature in Delhi\n• Rain in Mumbai"


def send_message():
    user_input = input_box.get().strip()
    if not user_input:
        return

    chat_box.configure(state="normal")
    chat_box.insert("end", f"You: {user_input}\n")

    bot_reply = get_bot_reply(user_input)
    chat_box.insert("end", f"Bot: {bot_reply}\n\n")

    chat_box.configure(state="disabled")
    chat_box.see("end")
    input_box.delete(0, "end")


send_btn = ctk.CTkButton(
    input_frame,
    width=45, height=45,
    corner_radius=23,
    fg_color="#2C75FF",
    hover_color="#1B4FCC",
    text="＋",
    font=("Segoe UI Black", 32),
    text_color="black",
    command=send_message
)
send_btn.place(relx=0.94, rely=0.50, anchor="center")

root.mainloop()
