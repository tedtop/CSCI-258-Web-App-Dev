from django.shortcuts import render
from django.views.generic import TemplateView


def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.",
    }
    return render(request, "home.html", context)


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context


class ProductsPageView(TemplateView):
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = [
            {"name": "Laptop", "price": "$999.99", "description": "High-performance laptop for work and gaming"},
            {"name": "Smartphone", "price": "$699.99", "description": "Latest smartphone with advanced features"},
            {"name": "Headphones", "price": "$199.99", "description": "Noise-canceling wireless headphones"},
            {"name": "Smart Watch", "price": "$299.99", "description": "Fitness tracking and notifications on your wrist"},
        ]
        return context
