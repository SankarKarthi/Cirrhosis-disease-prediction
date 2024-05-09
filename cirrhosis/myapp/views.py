from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login

from django.shortcuts import render, redirect
import joblib
import numpy as np
from django.contrib.auth import login as auth_login  # Rename login function
from .models import patientdata

def login(request):
    # Fixed email and password for testing
    fixed_email = 'sankar@gmail.com'
    fixed_password = '1234'

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check against the fixed email and password
        if email == fixed_email and password == fixed_password:
            # Create a User instance (this is just for testing)
            user, created = User.objects.get_or_create(username=email, email=email)

            # Log in the user
            auth_login(request, user)

            # Redirect to the home page
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html', {})


def result(request):
    # Load the trained model using joblib
    cls = joblib.load("svm.sav")

    # Collect feature values from the GET request
    lis = [float(request.GET['Age']),
           float(request.GET['Sex']),
           float(request.GET['Drug']),
           float(request.GET['N_Days']),
           float(request.GET['Ascites']),
           float(request.GET['Spiders']),
           float(request.GET['Hepatomegaly']),
           float(request.GET['Edema']),
           float(request.GET['Cholesterol']),
           float(request.GET['Bilirubin']),
           float(request.GET['Albumin']),
           float(request.GET['Alk_Phos']),
           float(request.GET['SGOT']),
           float(request.GET['Tryglicerides']),
           float(request.GET['Prothrombin']),
           float(request.GET['Copper']),
           float(request.GET['Platelets'])]

    # Convert the list to a numpy array for prediction
    input_data = np.array([lis])

    # Make predictions using the loaded model
    ans = cls.predict(input_data)

    # Save the entered values to MySQL
    patientdata.objects.create(
        Age=float(request.GET['Age']),
        Sex=float(request.GET['Sex']),
        Drug=float(request.GET['Drug']),
        N_Days=float(request.GET['N_Days']),
        Ascites=float(request.GET['Ascites']),
        Spiders=float(request.GET['Spiders']),
        Hepatomegaly=float(request.GET['Hepatomegaly']),
        Edema=float(request.GET['Edema']),
        Cholesterol=float(request.GET['Cholesterol']),
        Bilirubin=float(request.GET['Bilirubin']),
        Albumin=float(request.GET['Albumin']),
        Alk_Phos=float(request.GET['Alk_Phos']),
        SGOT=float(request.GET['SGOT']),
        Tryglicerides=float(request.GET['Tryglicerides']),
        Prothrombin=float(request.GET['Prothrombin']),
        Copper=float(request.GET['Copper']),
        Platelets=float(request.GET['Platelets']),
        predicted_result=ans[0]  # Assuming 'predicted_result' is a field in your model
    )

    # Assuming you want to pass some data to the template
    context = {
        'result': ans[0],
        # Other data you want to pass to the template...
    }

    return render(request, 'result.html', context)


def prediction(request):
    # Add logic for your prediction page if needed
    return render(request, 'prediction.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})
