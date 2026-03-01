from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from blog.forms import CountryForm, CityForm, StreetForm, HomeForm


class AddressWizard(SessionWizardView):


    form_list = [
        CountryForm,
        CityForm, 
        StreetForm,
        HomeForm,
    ]

    TEMPLATES = {"0": "country_form.html",
                "1": "city_form.html",
                "2": "street_form.html",
                "3": "home_form.html"}

    def get_template_names(self):
        # We return defaults templates
        # return super().get_template_names()

        # Or return our templates
        return [self.TEMPLATES[self.steps.current]]

    '''
    Этот метод единственный, который следует создать в обязательном порядке
    '''
    def done(self, form_list, **kwargs):
        
        # print(f"\u001b[32mFORM_LIST:\u001b[33m {form_list}\u001b[0m")
        #print(f"\u001b[32mKWARGS:\u001b[33m {kwargs}\u001b[0m")
        # return(self, 'done.html', {'form_data': [form.cleaned_data for form in form_list]})
        form_data = {}
        try:
            for form in form_list:
                form_data.update(form.cleaned_data)
            print(f"\u001b[31mFORM_DATA:\u001b[33m {form_data}\u001b[0m")
            # Now form_data is a dictionary and you can use .get()
            name_value = form_data.get('name')
            print(f"\u001b[31mNAME:\u001b[33m {name_value}\u001b[0m")
        except Exception as e:
            print(f"\u001b[31m{e}\u001b[0m")
        return render(self.request, 'done.html', {'form_data': form_data})

