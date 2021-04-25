from django import forms
from .models import Organization, Role

# creating a form
class RoleForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(RoleForm, self).__init__(*args, **kwargs)

        a = (Organization.objects.all()[0].organization_name, Organization.objects.all()[0].organization_name)
        Orgs = {a}
        for org in Organization.objects.all():
            a = (org.organization_name, org.organization_name)
            Orgs.add(a)

        a = (Role.objects.all()[0].role_name, Role.objects.all()[0].role_name)
        roles = {a}
        for org in Role.objects.all():
            a = (org.role_name, org.role_name)
            roles.add(a)

        self.fields['Role'].choices = roles
        self.fields['Organization'].choices = Orgs



    a = (Organization.objects.all()[0].organization_name, Organization.objects.all()[0].organization_name)
    Orgs = {a}

    for org in Organization.objects.all():
        a = (org.organization_name, org.organization_name)
        Orgs.add(a)

    a = (Role.objects.all()[0].role_name, Role.objects.all()[0].role_name)
    roles = {a}

    for org in Role.objects.all():
        a = (org.role_name, org.role_name)
        roles.add(a)
    Role = forms.ChoiceField(choices = roles)
    Organization = forms.ChoiceField(choices = Orgs)
