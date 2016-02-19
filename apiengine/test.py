import infermedica_api
api = infermedica_api.API(app_id='16d28cf7', app_key='c5fe62dc174660c87254f1632c37d261')

print(api.info())

# Create diagnosis object with initial patient information.
# Note that time argument is optional here as well as in the add_symptom function
request = infermedica_api.Diagnosis(sex='male', age=35, time='2015-02-09T08:30:00+05:00')

request.add_symptom('s_102', 'present', time='2015-02-09T08:00:00+05:00')
request.add_symptom('s_21', 'present', time='2015-02-09')
request.add_symptom('s_98', 'absent')

request.set_pursued_conditions(['c_76', 'c_9'])  # Optional

# call diagnosis
request = api.diagnosis(request)

print(request)