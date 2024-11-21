
# מערכת ניהול מסעדה - Django REST API

## תיאור הפרויקט

שרת Django שנבנה כדי לנהל מערכת לניהול מסעדה. השרת מאפשר:
- ניהול משתמשים.
- ניהול שולחנות והזמנות.
- ניהול פריטי תפריט וקטגוריות.
- ניהול הזמנות אוכל.

המערכת מספקת RESTful API לניהול כל הפונקציונליות.

---

## דרישות מקדימות

1. **גרסת Python**: 3.12.4 ומעלה
2. **ספריות נדרשות**: 
   - Django
   - Django Rest Framework
3. **מסד נתונים**: PostgreSQL (מוגדר בקובץ `.env`)

---

## התקנה והפעלה

1. **Clone the repository**:
   ```bash
   git clone https://github.com/razmazlih/restaurant_management_server.git
   cd restaurant_management_server
   ```

2. **Installing packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Defining the `.env` file**:
   צור קובץ `.env` בתיקייה הראשית עם המשתנים הבאים:
   ```env
   DATABASE_URL=<הכתובת של מסד הנתונים>
   SECRET_KEY=<מפתח סודי של Django>
   ALLOWED_HOSTS=<דומיינים מאושרים לשימוש>
   CORS_ALLOWED_ORIGINS=<דומיינים מאושרים לצד לקוח>
   ```

4. **Running migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Running the server**:
   ```bash
   python manage.py runserver
   ```

---

## תיעוד ה-API

המערכת כוללת את הנתיבים הבאים:

### ניהול משתמשים
- **GET /api/users/**: קבלת רשימת כל המשתמשים.
- **POST /api/users/**: יצירת משתמש חדש.
- **GET /api/users/<id>/**: קבלת פרטי משתמש מסוים.
- **PUT /api/users/<id>/**: עדכון פרטי משתמש.
- **DELETE /api/users/<id>/**: מחיקת משתמש.

### ניהול שולחנות והזמנות
- **GET /api/reservations/tables/**: קבלת רשימת השולחנות.
- **POST /api/reservations/tables/**: יצירת שולחן חדש (למשתמשים עם הרשאת `is_staff` בלבד).
- **GET /api/reservations/reservations/**: קבלת רשימת ההזמנות.
- **POST /api/reservations/reservations/create_reservation/**: יצירת הזמנה חדשה.

### ניהול תפריט
- **GET /api/menu/items/**: קבלת פריטי התפריט.
- **POST /api/menu/items/**: הוספת פריט חדש לתפריט.
- **PUT /api/menu/items/<id>/**: עדכון פריט בתפריט.
- **DELETE /api/menu/items/<id>/**: מחיקת פריט מהתפריט.

### ניהול הזמנות אוכל
- **GET /api/orders/food/**: קבלת רשימת ההזמנות.
- **POST /api/orders/food/**: יצירת הזמנה חדשה.
- **GET /api/orders/food/<id>/**: קבלת פרטי הזמנה.
- **PUT /api/orders/food/<id>/**: עדכון הזמנה.
- **DELETE /api/orders/food/<id>/**: מחיקת הזמנה.

---

## רישיון

הפרויקט מוגן תחת [MIT License](LICENSE).

