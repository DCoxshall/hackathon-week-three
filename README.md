Macronutrients:
- Carbohydrates (45 - 65 % of calories)
- Proteins (20 - 35 % of calories)
- Fats (10 - 35 % of calories)
- Calories

Frontend will receive historic macronutrients data and will need to send daily macronutrients to the backend.

Frontend does not need to worry about backend - they need to create a HTML page that will make GET and POST requests to the backend.

Making a GET request to /api/days/<n> will return a JSON object as follows:
{
  day1: {
    "carbohydrate": 50,
    "protein": 40,
    "fats": 70,
    "calories": 2000
  },
  [...]
}
"day1" is the most recent day (i.e. yesterday, assuming the user is inputting their nutrients every single day).
