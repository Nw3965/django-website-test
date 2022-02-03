from django import forms

class ChatBotForm(forms.Form):
    question = forms.CharField(
        label="質問",
        max_length=128,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
