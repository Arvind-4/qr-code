# QR Code

  
Scan here to open our lightning-fast QR code reading website. Built with Django for performance, Bootstrap for design, and Vercel for reliability. 

## 📦 Tech Stack:

- [Django](https://www.djangoproject.com/)  - Django makes it easier to build better web apps more quickly and with less code.
- [Bootstrap](https://getbootstrap.com/)  - Build fast, responsive sites with Bootstrap.
- [Vercel](https://vercel.com/)  - Vercel's Front end Cloud provides the developer experience and infrastructure to build, scale, and secure a faster, more personalised Web.

## Demo:

<a href="https://awesomeqrcode.vercel.app/">
<img src=".github/static/homepage.png" alt="Home Page"/>
</a>



## Getting Started: 

- Clone repository 

```bash
mkdir ~/Dev/qr-code -p
cd ~/Dev/qr-code
git clone https://github.com/Arvind-4/qr-code.git .
```  

- Install Dependencies:

```bash
cd ~/Dev/qr-code
python3.8 -m pip install virtualenv
python3.8 -m virtualenv . 
source bin/activate
pip install -r requirements.txt
```

- Create  `.env`  file:
Add Your Credentials  `.env`  from  `sample.env`:

```bash
DJANGO_SECRET_KEY=
DJANGO_DEBUG=
```
Get your Secret key from:
```python
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

- Run Server:

```bash
cd ~/Dev/qr-code
python manage.py runserver
```

Open [localhost:8000](http://localhost:8000) in your favourite browser :)
