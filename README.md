Macronutrients:
- Carbohydrates (260 - 50 % of calories)
- Proteins (50 - 20 % of calories)
- Fats (70 - 30 % of calories)
- Calories

Frontend will receive historic macronutrients data and will need to send daily macronutrients to the backend.

Frontend does not need to worry about backend - they need to create a HTML page that will make GET and POST requests to the backend.

Making a GET request to /api/days/`n` will return a JSON object as follows, for the last `n` days.
```
{
  day1: {
    "carbohydrate": 50,
    "protein": 40,
    "fats": 70,
    "calories": 2000
  },
  [...]
}
```

"day1" is the most recent day (i.e. yesterday, assuming the user is inputting their nutrients every single day).

Making a GET request to /api/user_info will return a JSON object as follows:
```
{
  "username": "dcoxshall", (for example)
  "height": 175, (cm)
  "weight": 75, (kg)
  "sex": "male" ("male" or "female" - we are referring to biological sex, not gender)
}
```

Calculations: 
| Activity level     | Freq. (times/week) | 
BMR (basic calories) 

Male: 10 * weight + 6.25 * height - 5 * age + 5 

Female: 10 * weight + 6.25 * height - 5 * age -161

| Activity level       | Freq. (times/week) | Macro multiplier |
|:-----------|:---:|------:|
| Sedentary / Very Light      |  0-1x |    1.2 |
| Low        |  1-2x |    1.375 |
| Moderate    |  3-4x |    1.55 |
| High   |  5-6x |    1.725 |
| Very High    |  7x |    1.9  |

