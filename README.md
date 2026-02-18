# Car‑sales Website (Udemy car‑listing app)

A small Django application for managing car listings (part of your Udemy course).
It provides user Profiles, vehicle `Listing` objects, image uploads, and a
`LikedListing` model for favouriting listings.

## Quick start (Windows PowerShell)

1. Create and activate a virtual environment

   ```powershell
   cd Udemy/src/main
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies

   ```powershell
   # if a requirements file exists in your project root, use it; otherwise
   pip install django pillow
   ```

3. Run migrations and create a superuser

   ```powershell
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Start the development server

   ```powershell
   python manage.py runserver
   # open http://localhost:8000
   ```

## Key files / structure

- `models.py` — core models: `Listing`, `LikedListing` (UUID primary key on Listing)
- `forms.py`, `filters.py`, `views.py` — request handling and search/filter logic
- `templates/`, `static/` — UI and assets
- `utils.py` — helpers (upload paths, etc.)

## Features

- Post and manage car listings with images
- Like/favourite listings (per `Profile`)
- Basic search & filters for brand, model, transmission and location
- Unit tests included in `tests.py`

## Running tests

```powershell
python manage.py test
```

## Contributing

- Open an issue or submit a pull request on the repository: https://github.com/Kendrick80/Car-sales-Website
- Add a LICENSE file if you want to set an explicit license (none specified here).

---

If you want, I can add a LICENSE (MIT), a CI workflow, or expand this README with
example screenshots and environment variables.  Which would you like next?