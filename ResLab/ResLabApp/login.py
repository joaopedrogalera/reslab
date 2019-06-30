from django.shortcuts import redirect, render
import ldap
from .models import Usuario
from . import numeracao

def CreateUser(ldapData):
    usuario = Usuario(uid=ldapData[0][1]['uid'][0].decode('utf-8'))
    usuario.nome = ldapData[0][1]['cn'][0].decode('utf-8')
    usuario.email1 = ldapData[0][1]['mail'][0].decode('utf-8')
    usuario.categoria = numeracao.categoria('usuario')
    usuario.cpf = ldapData[0][1]['employeeNumber'][0].decode('utf-8')

    groups = ldapData[0][0].split(',')
    if groups[len(groups)-5] == 'ou=alunos':
        usuario.ra = ldapData[0][1]['carLicense'][0].decode('utf-8')
        usuario.email2 = ldapData[0][1]['displayName'][0].decode('utf-8')
        usuario.cargo = numeracao.cargo('aluno')
    else:
        usuario.ra = ldapData[0][1]['pager'][0].decode('utf-8')
        usuario.cargo = numeracao.cargo('servidor')

    usuario.save()


def doLogin(request):
    if not (request.method == 'POST') or request.POST['uid'] == '' or request.POST['passwd'] == '':
        return render(request,"loginError.html")

    ldapURI = 'ldap://ldapslave.ct.utfpr.edu.br'

    l = ldap.initialize(ldapURI)
    l.protocol_version = ldap.VERSION3
    l.simple_bind_s()

    ldapResult = l.search("dc=utfpr,dc=edu,dc=br",ldap.SCOPE_SUBTREE,'(uid='+request.POST['uid']+')')
    resultTipe, resultData = l.result(ldapResult, 0)

    if resultData == []:
        return render(request,"loginError.html")

    dn = resultData[0][0]

    l.unbind()

    l = ldap.initialize(ldapURI)
    l.protocol_version = ldap.VERSION3
    try:
        l.simple_bind_s(dn,request.POST['passwd'])
    except ldap.INVALID_CREDENTIALS:
        l.unbind()
        return render(request,"loginError.html")


    try:
        usuario = Usuario.objects.get(uid=resultData[0][1]['uid'][0].decode('utf-8'))
    except Usuario.DoesNotExist:
        CreateUser(resultData)

    request.session['exists'] = True
    request.session['uid'] = resultData[0][1]['uid'][0].decode('utf-8')
    return redirect('/dashboard')
