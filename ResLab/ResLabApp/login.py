from django.shortcuts import redirect
import ldap
from .models import Usuario

def CreateUser(ldapData):
    usuario = Usuario(uid=ldapData[0][1]['uid'][0].decode('utf-8'))
    usuario.nome = ldapData[0][1]['cn'][0].decode('utf-8')
    usuario.email1 = ldapData[0][1]['mail'][0].decode('utf-8')
    usuario.categoria = '0'
    usuario.cpf = ldapData[0][1]['employeeNumber'][0].decode('utf-8')

    groups = ldapData[0][0].split(',')
    if groups[len(groups)-5] == 'ou=alunos':
        usuario.ra = ldapData[0][1]['carLicense'][0].decode('utf-8')
        usuario.email2 = ldapData[0][1]['displayName'][0].decode('utf-8')
        usuario.cargo = '0'
    else:
        usuario.ra = ldapData[0][1]['pager'][0].decode('utf-8')
        usuario.cargo = '1'
        usuario.email2 = '0'

    usuario.save()


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


    try:
        usuario = Usuario.objects.get(uid=resultData[0][1]['uid'][0].decode('utf-8'))
    except Usuario.DoesNotExist:
        CreateUser(resultData)

    request.session['exists'] = True
    request.session['uid'] = resultData[0][1]['uid'][0].decode('utf-8')
    return redirect('/dashboard')
