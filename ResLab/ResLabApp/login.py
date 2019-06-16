from django.http import HttpResponse
from django.shortcuts import redirect
import ldap
from . import models

def doLogin(request):
    if not (request.method == 'POST') or request.POST['uid'] == '' or request.POST['passwd'] == '':
        return redirect('/loginError')

    l = ldap.initialize('ldap://ldapslave.ct.utfpr.edu.br')
    l.protocol_version = ldap.VERSION3
    l.simple_bind_s()

    ldapResult = l.search("dc=utfpr,dc=edu,dc=br",ldap.SCOPE_SUBTREE,'(uid='+request.POST['uid']+')')
    resultTipe, resultData = l.result(ldapResult, 0)

    if resultData == []:
        return redirect('/loginError')

    dn = resultData[0][0]

    l.unbind()

    l = ldap.initialize('ldap://ldapslave.ct.utfpr.edu.br')
    l.protocol_version = ldap.VERSION3
    try:
        l.simple_bind_s(dn,request.POST['passwd'])
    except ldap.INVALID_CREDENTIALS:
        l.unbind()
        return redirect('/loginError')

    return HttpResponse("OK")
