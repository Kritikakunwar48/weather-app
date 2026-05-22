import tkinter as tk
import requests

def get_weather():

    city = city_entry.get()
    api_key = "b650ea58982a676fd96d0cc5eed8c446"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    print(data)

    if data["cod"] == 200:

        city_name = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        result_label.config(
            text=f"City: {city_name}\nTemperature: {temp} °C\nWeather: {weather}"
        )

    else:
        result_label.config(
            text=data["message"]
        )


root = tk.Tk()
root.title("Weather App")
root.geometry("400x350")
root.config(bg="skyblue")

frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

title = tk.Label(frame,
                 text="Weather App",
                 font=("Arial", 20, "bold"),
                 bg="white")

title.pack(pady=10)

city_entry = tk.Entry(frame,
                      font=("Arial", 16),
                      width=20)

city_entry.pack(pady=10)

search_btn = tk.Button(frame,
                       text="Get Weather",
                       font=("Arial", 12),
                       bg="blue",
                       fg="white",
                       command=get_weather)

search_btn.pack(pady=10)

result_label = tk.Label(frame,
                        text="",
                        font=("Arial", 12),
                        bg="white")

result_label.pack(pady=10)

root.mainloop()