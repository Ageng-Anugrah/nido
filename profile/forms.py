from django import forms
from django.forms.widgets import SelectDateWidget

class ProfileForm(forms.Form):
    # TODO: Implment photo filling form, also handle the backend
    # photo = forms.ImageField(
    #     label='Foto Profil',
    #     required=False,
    # )
    phone_number = forms.CharField(
        label='Nomor Telepon (Contoh: +628123456789)',
        required=True,
        max_length=20,
    )
    secondary_email = forms.EmailField(
        label='Email (selain email akun DSTI)',
        required=True,
        max_length=100,
    )
    line_id = forms.CharField(
        label='Line ID',
        required=True,
        max_length=100,
    )
    birth_place = forms.CharField(
        label='Tempat Lahir',
        required=False,
        max_length=100,
    )
    birth_date = forms.DateField(
        label='Tanggal Lahir (Tanggal-Bulan-Tahun)',
        required=False,
        widget=SelectDateWidget(years=range(1945, 2045)),
    )
    home_address = forms.CharField(
        label='Alamat Rumah',
        required=False,
        max_length=500,
    )
    current_address = forms.CharField(
        label='Alamat Tinggal Sekarang (kos-kosan, apartemen, lainnya)',
        required=False,
        max_length=500,
    )
