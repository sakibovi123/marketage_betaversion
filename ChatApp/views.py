from django.shortcuts import render, HttpResponse, redirect
from ChatApp.models import ChatRoom, Message
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime
from django.utils import timezone
from django.http import JsonResponse
import json
# Create your views here.


def home_page(request):
    all_users = User.objects.exclude(username=request.user)
    # all_users = User.objects.all()
    ct_room = ChatRoom.objects.filter(sellers=request.user).order_by("-id")
    for_buyer = ChatRoom.objects.filter(buyer=request.user).order_by("-id")
    # print(ct_room)
    args = {
        'all_users': all_users,
        'ct_room': ct_room,
        'for_buyer': for_buyer
    }
    return render(request, 'Test/index.html', args)



def user_details(request, id):
    user_details = User.objects.get(pk=id)
    
    args = {
        'user_details': user_details
    }
    if request.method == 'POST':
        buyer = request.user
        sellers = user_details.username
        
        try:
            sellers = User.objects.get(username=sellers)
            
            room_name = request.POST.get('room_name')
        except:
            return redirect("/")
        else:
            room = ChatRoom(
                buyer=buyer, sellers=sellers, room_name=room_name
            )
            room.save()
        
            return redirect(f"/chat/chatroom/{room.id}")
        
    return render(request, 'Test/user_details.html', args)


def chatRoomView(request, id):
    chatroom = ChatRoom.objects.get(pk=id)
    values = Message.objects.filter(chatroom=id)
    rooms = ChatRoom.objects.filter(Q(buyer=request.user) or Q(sellers=request.user)).order_by("-id")
    # print(values.sent_date)
    current_time = datetime.now(timezone.utc)
    print("Current Time: " + str(current_time))

    last = chatroom.buyer.last_login

    ago = str(current_time - last).split(",")[0]

    print(ago + "AGOOOOOOOO")

    print("BEFORE:", len(Message.objects.all()))

    if request.method == 'POST':
        sender = request.user
        msg = request.POST.get('msg')
        message = None
        sent = Message(sender=sender, msg=msg, chatroom=chatroom)

        chatroom.recent_chat = True
        chatroom.save()
        sent.save()

        print("IMAGE:", str(sender.selleraccount.profile_picture))
        print("USER:", sender)
        print("MESSAGE:", msg)

        if request.is_ajax():
            month_dct = {
                1: "Jan.", 2: "Feb.", 3: "March", 4: "April", 5: "May",
                6: "June", 7: "July", 8: "Aug.", 9: "Sept.", 10: "Oct.",
                11: "Nov.", 12: "Dec."
            }

            send_at = sent.sent_date
            month = int(send_at.strftime("%m"))
            month = str(month_dct[month])
            # print(month)
            day = str(int(send_at.strftime("%d")))
            # print(day)
            year = str(send_at.strftime("%Y"))
            hour = str(send_at.strftime("%I"))
            minute = str(send_at.strftime("%M"))
            am_pm = str(send_at.strftime("%p").lower())
            

            # send_at = send_at.strftime("%b %d, %Y, %I:%M %p")
            send_at = f"{month} {day}, {year}, {hour}:{minute} {am_pm}"
            profile_image = str(sender.selleraccount.profile_picture)

            message = {
                "id": str(sent.id),
                "profile_image": profile_image,
                "message": msg,
                "username": sender.username,
                "send_at": send_at
            }

            print("MESAGE", message)
            print("AFTER:", len(Message.objects.all()))

            # x =  str(Message.objects.all())
            # print(Message.objects.values())

            data = {
                "message_info": message
            }
            return JsonResponse(data)
        return redirect(f"/chat/chatroom/{chatroom.id}")


    args = {
        'chatroom': chatroom,
        'values': values,
        'rooms': rooms,
        'ago': ago
    }
    
    # print(chatroom)
    return render(request, "Test/chatRoom.html", args)