from django.http import HttpResponse
from django.shortcuts import render

from mini_core.forms.DateFilterForm import DateFilterForm
from mini_core.models import Client, Sale

def report(request):

    form = DateFilterForm(request.GET)
    if not form.data:
        form.errors.clear()
        return render(request, 'report.html', {'form': form})
    if not form.is_valid():
        return render(request, 'report.html', {'form': form})
        
    start_date = form.cleaned_data['start_date']
    end_date = form.cleaned_data['end_date']
    
    sales = Sale.objects.all()
    results = []
    for sale in sales:
        # Filter by creation date
        in_date_range = sale.creation_date >= start_date and sale.creation_date <= end_date
        if not in_date_range:
            continue
        client = sale.client
        # Find the client in the results and update it
        client_found = False
        for result in results:
            if result['client'] == client:
                client_found = True
                result['sales'] += 1
                result['total_price'] += sale.price
                break
        # If the client is not in the results, add it
        if not client_found:
            results.append({
                'client': client,
                'sales': 1,
                'total_price': sale.price
            })
    # Sort the results by total price
    results.sort(key=lambda result: result['total_price'], reverse=True)
    return render(request, 'report.html', {
        'form': form,
        'results': results,
        'summary': {
            'sales': sum(result['sales'] for result in results),
            'total_price': sum(result['total_price'] for result in results),
            'clients': len(results)
        }
    })

def client_list(request):
    clients = Client.objects.all()
    return render(request, "client_list.html", {"clients": clients})

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, "sale_list.html", {"sales": sales})