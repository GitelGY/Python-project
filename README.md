# 🌍 Life Expectancy Prediction System
### מערכת לחיזוי וניתוח תוחלת חיים מבוססת Machine Learning

מערכת Full-Stack המאפשרת לחזות את תוחלת החיים הצפויה במדינות שונות על סמך נתונים כלכליים (הוצאה ממשלתית) וזמן (שנה), כולל ממשק אינטראקטיבי והסברים על החלטות המודל.

## 🚀 תכונות עיקריות
* **חיזוי מדויק:** שימוש במודל KNN (K-Nearest Neighbors) שהשיג רמת דיוק גבוהה.
* **Explainable AI:** הצגת "מקדמי השפעה" (Coefficients) המראים אילו גורמים העלו או הורידו את התחזית.
* **API מהיר:** שרת Backend מבוסס FastAPI.
* **ממשק ידידותי:** דף אינטרנט מעוצב המאפשר הזנת נתונים וקבלת תוצאות מיידיות.

## 🛠 טכנולוגיות
* **Data Science:** Python, Pandas, NumPy, Scikit-learn
* **Backend:** FastAPI, Uvicorn, Pydantic
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
* **Serialization:** Joblib (לשמירת המודלים והסקיילר)

## 📂 מבנה הפרויקט
```plaintext
├── main.py              # שרת ה-API (FastAPI)
├── index.html           # ממשק המשתמש (Frontend)
├── Project.ipynb        # מחברת מחקר, אימון מודלים והשוואת ביצועים
├── healthexp.csv        # בסיס הנתונים המקורי (OECD Health Data)
├── model.pkl            # מודל ה-KNN המנצח (לחיזוי בפועל)
├── lr_model.pkl         # מודל רגרסיה ליניארית (לצורך הסבר חשיבות משתנים)
├── scaler.pkl           # הסקיילר (StandardScaler) לנרמול הנתונים
└── columns.pkl          # רשימת העמודות מהאימון (לצורך One-Hot Encoding)
```
⚙️ הוראות הרצה
1. התקנת ספריות
יש להריץ את הפקודה הבאה בטרמינל:

Bash

pip install fastapi uvicorn pandas scikit-learn joblib
2. הרצת השרת
נווט לתיקיית הפרויקט והרצ:

Bash

python -m uvicorn main:app --reload
השרת יהיה זמין בכתובת: http://127.0.0.1:8000

3. הרצת הממשק
פתח את הקובץ index.html בכל דפדפן מודרני.

📊 תובנות מהמודל
מהניתוח שביצענו, המשתנה המשפיע ביותר על עליית תוחלת החיים הוא השנה (Year), מה שמעיד על שיפור טכנולוגי ורפואי לאורך זמן. מנגד, מדינות מסוימות מראות קשר מורכב בין הוצאה כספית לתוחלת חיים, מה שמדגיש את החשיבות של יעילות מערכת הבריאות.

פותח על ידי: G.Goldberg e-mail GittyB32@gmail.com שנת פיתוח: 2026

