from django.shortcuts import render

def twicmdfunc(request):
    if request.method == 'GET':
        return render(request, "twicmd.html", {})
    elif request.method == 'POST':
        twicmd = ""
        atSign =request.POST.get('atSign')
        if atSign != "":
            atSign = "@" + atSign
            twicmd = atSign

        fromUser =request.POST.get('from')
        if fromUser != "":
            twicmd = twicmd + " from:" + fromUser

        toUser =request.POST.get('to')
        if toUser != "":
            twicmd = twicmd + " to:" + toUser

        follows = request.POST.get('follows')
        if follows != None:
            twicmd = twicmd + " filter:follows"

        since = request.POST.get('since')
        if since != "":
            twicmd = twicmd + " since:" + since

        until = request.POST.get('until')
        if until != "":
            twicmd = twicmd + " until:" + until

        images = request.POST.get('images')
        if images != None:
            twicmd = twicmd + " filter:images"

        links = request.POST.get('links')
        if links != None:
            twicmd = twicmd + " filter:links"

        word = request.POST.get('word')
        if word != "":
            twicmd = twicmd + " " + word

        return render(request, "twicmd.html", {'twicmd':twicmd})