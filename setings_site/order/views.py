from .models import Orders
from shop.models import Product
from shop.utils import * 
from django.views.generic import ListView

        
class OrdersShow(DataMixin, ListView):
    paginate_by = None
    model = Product
    template_name = 'order/order.htm' # Передаём шаблон в представление
    # ListView - автоматически формирует колекцию object_list, с которой можно работать в teamplate, либо можем переопределить это имя 
    context_object_name = 'product_in_order' # теперь бкдем работать с колекцией по имени posts, имя используемое в templates

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # Берем ранее созданый контекст, чтобы не потерять его 

        c_def = self.get_user_context(title='Ваши покупки')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        listt = Orders.objects.filter(user = self.request.user.pk)
        spis, gg, r = '', ",[]", ''
        
        for prod in listt:
            spis += "".join(map(str,prod.product_slug_list))
        for s in spis:
            if s not in gg:
                r += s
        prod_list = r.split("'")
        # При покупке колво товара нужно отреда
        return Product.objects.filter(available=True, slug__in=prod_list)
        