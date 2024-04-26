To run a Django app with Gunicorn, you can follow these steps:

1. **Install Gunicorn** (if you haven't already):
   ```bash
   pip install gunicorn
   ```

2. **Navigate to your Django project folder** (where your `manage.py` resides).

3. **Run Gunicorn** with one of the following methods:

   - **Method 1: Specify the WSGI application module**:
     ```bash
     gunicorn myproject.wsgi
     ```
     Replace `myproject` with your actual project name.

   - **Method 2: Specify the application directly**:
     ```bash
     gunicorn [projectname].wsgi:application -b 127.0.0.1:[port number]
     ```
     Replace `[projectname]` with your project name and `[port number]` with the desired port (e.g., 8000).

   - **Method 3: Use Gunicorn's built-in Django integration**:
     - Add `"gunicorn"` to your `INSTALLED_APPS` in `settings.py`.
     - Create a custom management command (e.g., `run_gunicorn`) in your `manage.py`:
       ```python
       # myproject/manage.py
       # ...
       if __name__ == "__main__":
           from django.core.management import execute_from_command_line
           from gunicorn.app.wsgiapp import run

           execute_from_command_line(sys.argv)
           if sys.argv[1] == "run_gunicorn":
               run()
       ```
     - Run Gunicorn using the custom command:
       ```bash
       python manage.py run_gunicorn
       ```

Remember to adjust the settings according to your project's requirements. Gunicorn will serve your Django app, making it accessible via the specified port. 🚀