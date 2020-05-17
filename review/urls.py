from django.urls import path
from .import views

urlpatterns = [
    path('create_review/<product_id>', views.create_review,
         name='create_review'),
    path('edit_review/<pk>', views.edit_review,
         name='edit_review'),
    path('review_delete/<pk>', views.review_delete, name='review_delete'),
    # path('review_back/<product_id>', views.review_back, name='review_back'),
]

# urlpatterns = [
    # path('get_reviews/<product_id>', views.get_reviews, name='get_reviews'),
#     # path('get_reviews/<product_id>', views.get_reviews, name='get_reviews'),
#     path('create_review/<product_id>', views.create_or_edit_review,
#          name='create_review'),
#     path('edit_review/<pk>', views.create_or_edit_review,
#          name='edit_review'),
#     path('review_delete/<pk>', views.review_delete, name='review_delete')
# ]