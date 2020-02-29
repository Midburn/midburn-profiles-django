from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.email = data.get('email')
        user.passport_country = data.get('passport_country')
        user.country_code = data.get('country_code')
        user.city = data.get('city')
        user.street = data.get('street')
        user.address = data.get('address')
        user.birthday = data.get('birthday')
        user.primary_phone_number = data.get('primary_phone_number')
        user.identification_number = data.get('identification_number')
        user.identification_type = data.get('identification_type')
        user.save()
        return user
