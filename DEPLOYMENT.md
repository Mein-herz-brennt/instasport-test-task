# Deployment Instructions

The application is structured to easily deploy on free platforms such as Render, Railway, or Fly.io.

## Steps

1. Configure environment variables in the hosting dashboard (reference `.env.example`).
   - Specifically set `SECRET_KEY`, `DEBUG=False`, and `DATABASE_URL` (to your provisioned PostgreSQL DB).
2. The project contains a `Procfile` set to run `gunicorn`, which will automatically be detected by Railway or Render.
3. **Database Setup**: Configure the build process to run mutations (`python manage.py migrate`). Render allows specifying build scripts; Railway does too.
4. **Static Files**: A `STATIC_ROOT` has been prepared in settings. Ensure WhiteNoise (if installed later) or the host's standard setup handles `staticfiles`.

## Testing Locally
Run migrations, create a superuser, and host:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
