from django import forms

class Form_New_Listing(forms.Form):
    CHOICES_CATEGORY = [
        ("electronics", "Electronics"),
        ("fashion", "Fashion"),
        ("sports_hobbies", "Sports and Hobbies"),
        ("house_garden", "House and Garden"),
        ("books_movies_music", "Books, Movies, Music"),
        ("others", "Others"),
    ]
    

    title = forms.CharField(label="Title", max_length=64, required=True)
    description = forms.CharField(label="Add description", max_length=255, required=True)
    starting_bid = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    image = forms.URLField(help_text="Put URL for image of product here")
    category = forms.ChoiceField(choices=CHOICES_CATEGORY, help_text="Choose category")
