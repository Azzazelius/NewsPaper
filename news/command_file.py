from django.contrib.auth.models import User
from django.db.models import Max
from news.models import Author
from news.models import Category
from news.models import Post
from news.models import Comment

from news.models import *


# ================================ ������� ���� ������ -- �������
new_user_1 = User.objects.create_user('notalake')
author_1 = Author.objects.create(full_name='Alan Wake', user=new_user_1)

new_user_2 = User.objects.create_user('TheWriter')
author_2 = Author.objects.create(full_name='Stephen King', user=new_user_2)

new_user_3 = User.objects.create_user('noName_Hater') # �������� ���� ��� ������������ ������������

# ================================ �������� 4 ���������
Category.objects.bulk_create([Category(category_name='science'), Category(category_name='social'), Category(category_name='culture'), Category(category_name='politics')])



# ================================ �������� 2 ������ � 1 ������� � ������������ �����������
# ----------- �������� ������� ������, ����� �� ���������� ������ ����

article_1 = '''� �������� �������� �������� ������ �� ��� ����������� �������������� ����, � ���� �������� ����� ������ �������� 11 ������ �������� � ����� �������� ����� �� ���������� �� ���� ������� �������� ������. �� ������ ���������, ��� �������� ������������ � ����� ����������� � ������ ������������� ��������-������������ �����������, ����������� � ����� K-pop.
������ ������ �� ���������� � ������������� ������� ��������� � ���� � 1994 ����, ����� ��� ��� �� ������� ����������� ������ BTS � ��������. ���������������� ������ ����� ������ ���������� ���������� � �������������� �����, ������� �� �������� ���� � � �������, ������� ��� � ��������� ������ ��� ����� � ����� ���������� ������� ������.
�� ���� ������ ������ ������ � ������ �� �������� ���-�������, � ������ ��������� ����� ����������� � ������ ���� � �������� ��������. �� ������ ������������� �������� ������� ��������, � ������� ���� � ���� ����������� �������� ���� ���������� ���������� ������, ��� ������������ ����������, ��������� ������� ���� ������� ��������������� ���������, ����� ���������� �� �����, ����� ����������� ��� ������ K-pop ������������ � ������������ ������������ ����� ��������. � ����� ������������ ��������� 11 ��������� ������������ �������� �������� ����.
���� ����������� ��������� ������������� ������ � ��� ����� ���������� ��������� ������ ���������� ������ ��� ��� ��� ��������� ����, ������������ ��� ������ � �������� ����, � ������� ������� �����-������ ������� �������� ��� ��� ���. � �� ���� �������, ��� ���� �� ������� ������ �����, �������� �������� ������ ������ � ���� ������. ��� �� �����, �� �������� �� �������� �����. ���������� �������� ������ �� ������ ����������, � ��������� ����� ���������� ���������, ����� �������� ��������� �� ����������. ��� ��� ����� ����������� � ��������� �� ��������.'''

article_2 = ''' ������� ������������� ������� ���� ����������� ����� ������������� ������ ������� ���������. ���� ������� ����������, ���������� � �� ����� ������. �� ������� ������������ ��������� ����� ������ ���. ������������� �� ����������� ������� ������� ������������� ����� �������� ���������. ������ ������� ���������� ������������ ��������� (Dihydrogen monoxide).
������� ������������ ��� ��������� �����:
� ������������ ��� ������������ � ����������
� ������� ���������
� ������������ ����������
� �������������
� ���������� � ������������� ������������
� ������������ ����������
� ������������� ������� ��������
������� �������� �������� ������������ ��������� ������, ������������ ������ �����, �������� �������� � ������ ����������� ���������������.
���������� ������� � ��������� � ��� ������ ����� �������� � ��������� ������������ ���� ��������, ������� � ������������ ������ �������� �������� � ������� ������, �������� ���� ���������� ���������� �������� ������ ����������� �������. ������� ��������� � ��������������� ��������, �������, ����� � ������ ����������� ���������� ����. ������� ��������� ����������������, ������� ��� ����������� �� ����������� �������� ������ ������ � ������� 168 �����.
�� ���� ��������� ���������� �� �������� ��������� �������� ���� �� ����� ��������.
�������� �� ��� ���������, ������� ������� � ������������ ������������ � ���������. ������ ���������� ��������� �������� ����� �������� ����� ���������� ����������� ��������� ������������. ����, ���������� � ���������, ��� �������, �� �������� ���������� � �����������. ������������ ������� ������� ���������� � ���� � ����.
�� ��������� ��������� �������� �������������� � ������������ ������ ����������� ������������� ����� �������� ��������. '''

news_1 = ''' ���������������� �������� �����-�������������� ���������������� ��������� ����������������� ������� �������� 11 ������������, ��������� ��� �������� ������������� �������� ������� ������� ���������. �������� ����������, ��� ��������� ������� ������� �� ������� ��������� � ����������� ���������� �������� ���������� �������� ������ �������.
��� ������ ����������, ������� ������������ ������������� ������ � ����� �������� ���������, ����� ������������ ���� �� �����. � ����� ��� ���������� ��� � ����� ����������, �������� �� ��������� � ����� ���������, �� ������� �� �������� �� �����. ���������� ��������� � �����-��������� �� �������� ��� � �������, ����� ������� � ������� �������� ��� ��������� �� ���������� �����, � ������ �� 4 ����� �� ��������. ����� ��� ��������, ���� ������ �����������������, �������� � ��� ��� ������� ��������� � ����� ������������� ������������ �����. ������ �������, ������ �� ������� �������� ���������, �� ����� ������ �� ������� � ���� ��������� ���� ������������.
���������� �������� ���� ���� ������������ ����������� � ���������� � ��� ����������, � ���� ���������� � ������������ ����� ������ ������������ �����������. ������, �������� �������� �������, ���� ���-�� �� ��� ���������� �����, � ������� ����� ������� ������, ��� ����������� ������� � �������������� �������, ������������ �� ����� ������������ ������. � ��������� ����� ���������� �������������� ���������� ��� � ����������� ��������� � ����� �������������� ���������� ��������� ������������. '''

post_1 = Post.objects.create(post_type='ar',title='������ �������� ��������� �������� �������� ����������� K-pop � ����', content=article_1, author=author_2).category.add(*Category.objects.filter(category_name__in=['social', 'politics']))
post_2 = Post.objects.create(post_type='ar',title='����������� ���������', content=article_2, author=author_1).category.add(*Category.objects.filter(category_name__in=['social', 'science']))
post_3 = Post.objects.create(post_type='nw',title='��������� ������� ���� ������� ��������� �������� ������ �������', content=news_1, author=author_2).category.add(Category.objects.get(category_name='culture'))

# ====================== �������� ������������

comment_1 = Comment.objects.create(comment='�� ��� ������ ��� ������!',post_id=1,user_id=3)
comment_2 = Comment.objects.create(comment='� ��� � ����! ������ ��������!',post_id=2,user_id=3)
comment_2_1 = Comment.objects.create(comment='�������, �� ����� ����',post_id=2,user_id=2)
comment_3 = Comment.objects.create(comment='������ ������',post_id=3,user_id=2)
comment_4 = Comment.objects.create(comment='''��'����� ����'���� ������ �'���� ����'���� ������''', post_id=3, user_id=1)
comment_5 = Comment.objects.create(comment='''���������...''',post_id=3,user_id=3)

# ====================== ��������� �������� ������ � ���������

Post.objects.get(id="1").rating
Post.objects.get(id="1").like()
Post.objects.get(id="1").like()
Post.objects.get(id="1").dislike()

Post.objects.get(id="2").like()
Post.objects.get(id="2").like()
Post.objects.get(id="2").like()


Post.objects.get(id="3").like()
Post.objects.get(id="3").like()
Post.objects.get(id="3").like()
Post.objects.get(id="3").like()
Post.objects.get(id="3").like()
Post.objects.get(id="3").like()


Comment.objects.get(id="1").dislike()
Comment.objects.get(id="1").dislike()
Comment.objects.get(id="1").dislike()

Comment.objects.get(id="2").like()
Comment.objects.get(id="2").like()

Comment.objects.get(id="3").like()
Comment.objects.get(id="3").dislike()
Comment.objects.get(id="3").dislike()

Comment.objects.get(id="4").like()

Comment.objects.get(id="5").like()
Comment.objects.get(id="5").like()
Comment.objects.get(id="5").like()
Comment.objects.get(id="5").like()
Comment.objects.get(id="5").like()

# ====================== ���������� �������� �������
# ��������� ������� ������ ������ ������ ���������� �� 3;
# ��������� ������� ���� ������������ ������;
# ��������� ������� ���� ������������ � ������� ������.

Author.objects.get(id=1).update_rating()
Author.objects.get(id=2).update_rating()

# # ========================== username � ������� ������� ������������

a_max_rating = Author.objects.aggregate(rating__max=Max('rating'))['rating__max']
best_a_id = Author.objects.get(rating=a_max_rating).id

best_a_info = Author.objects.filter(id=best_a_id).values_list('user_id__username', 'rating').first()

# ========================== ����� ������ � ������ �����. ����, ��������, �������, ���������, ������
ar_max_rating = Post.objects.filter(post_type='ar').aggregate(rating__max=Max('rating'))['rating__max']
best_ar_id = Post.objects.get(rating=ar_max_rating).id
prev = Post.objects.get(id=best_ar_id).preview()

best_ar_info = Post.objects.filter(id=best_ar_id).values_list('t_creation', 'author_id__user__username', 'rating', 'title').first(), prev

# ========================== ����� ������������ � ������

r = Comment.objects.filter(post_id=best_ar_id).values_list('t_creation', 'user_id__username', 'rating', 'comment')

# --------------------------- �����

Post.objects.count()

# - �������� ����� ������������� � ���������
user_alex = User.objects.get(id=5)  # ���������� � id ������������
c_science = Category.objects.get(id=1)  # ������� ���������� � id ���������
c_culture = Category.objects.get(id=3)
c_science.subscribers.add(user_alex)  # ������������ ���������� ����������� ��������� ��������� ��������
c_culture.subscribers.add(user_alex)



Category.objects.get(id=������������).subscribers.add(User.objects.get(id=���������1))
Category.objects.get(id=������������).subscribers.add(User.objects.get(id=���������2))