from django.shortcuts import render
from .models import *


def mysum(lst):
    total = 0
    for i in lst:
        total += i
    return total

# Create your views here.
def ratings(request,name):
    app = App.objects.get(name=name)
    template_name = "accounts/ratings.html"
    users = Rate.objects.filter(app=app).order_by('-date_time')
    args = {'users':users}

    ratings = []
    # .count(element)
    if len(users) > 0:
        for user in users:
            ratings.append(user.rating)
        total_rating = mysum(ratings)
        users_rated = len(users)
        overall_rating = round(((total_rating*1.0)/users_rated),1)
        args['overall_rating'] = overall_rating
        args['no_of_users'] = users_rated
        types_of_ratings = [{'bar5':round((ratings.count(5)/len(ratings))*100,0),'bar5count':ratings.count(5)},
        {'bar4':round((ratings.count(4)/len(ratings))*100,0),'bar4count':ratings.count(4)},
        {'bar3':round((ratings.count(3)/len(ratings))*100,0),'bar3count':ratings.count(3)},
        {'bar2':round((ratings.count(2)/len(ratings))*100,0),'bar2count':ratings.count(2)},
        {'bar1':round((ratings.count(1)/len(ratings))*100,0),'bar1count':ratings.count(1)}]
        for each in types_of_ratings:
            for key,val in each.items():
                args[key]=val
        rates = ""
        for i in range(1,6):
            if overall_rating//1 >= i:
                if i < 5:
                    rates += "1,"
                else:
                    rates += "1"
            else:
                if overall_rating - i >= -0.5:
                    if i < 5:
                        rates += "0.5,"
                    else:
                        rates += "0.5"
                else:
                    if i < 5:
                        rates += "0,"
                    else:
                        rates += "0"
        args['rates'] = rates
    args['user'] = request.user
    # if user.rated:
    #     review = Rate.objects.get(user=user)
        # args['review']=review
    args['title']="Reviews"
    args['object']=app
    return render(request,template_name,args)