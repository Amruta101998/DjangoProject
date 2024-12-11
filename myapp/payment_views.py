from django.http import JsonResponse
from payments.models import User

def process_payment(request, user_id):
    user = User.objects.get(id=user_id)
    amount = request.POST.get('amount')
    
    if user.balance >= amount:
        user.balance -= amount
        user.save()  
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def get_user_balance(user_id):
    return User.objects.filter(id=user_id).values('balance').first()

def transfer_money(from_user_id, to_user_id, amount):
    from_user = User.objects.get(id=from_user_id)
    to_user = User.objects.get(id=to_user_id)
    
    if from_user.balance >= amount:
        from_user.balance -= amount
        to_user.balance += amount
        from_user.save()
        to_user.save()
        return True
    return False