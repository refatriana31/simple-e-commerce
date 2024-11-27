from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm, ProductFilterForm
# Create your views here.

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    paginate_by = 9  # Show 9 products per page
    
    def get_queryset(self):
        queryset = Product.objects.all().order_by('-created_at')
        category = self.request.GET.get('category')
        search_query = self.request.GET.get('search')
        
        if category:
            queryset = queryset.filter(category_id=category)
        
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductFilterForm()
        return context
productlistview=ProductListView.as_view()

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'products'
    
productdetailview=ProductDetailView.as_view()

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = reverse_lazy('product:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context
    
productdeleteview=ProductDeleteView.as_view()

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product:product_list')

productcreateview = ProductCreateView.as_view()

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product:product_list')

productupdateview = ProductUpdateView.as_view()




