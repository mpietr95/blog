import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from blog.models import Post

# Opublikuj wszystkie posty w robocie
updated = Post.objects.filter(status='DF').update(status='PB')
print(f'Opublikowano {updated} postów!')

# Wyświetl statystyki
print(f'\nStatystyki:')
print(f'Wszystkich postów: {Post.objects.count()}')
print(f'Opublikowanych: {Post.published.count()}')
