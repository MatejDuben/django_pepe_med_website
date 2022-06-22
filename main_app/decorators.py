def is_cookies_allowed_or_no(request):
  try:
    this_user = request.user.customer   #skusi ci je user prihlaseny
    return True
  except:
    try:
      device = request.COOKIES['device']    #vrati cookies uzivatela
      return True
    except:
      return False