class times_available(forms.ModelForm):
    #dynamic field
    def __init__(self,pk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # get day info
        hours = list(ReservationDate.objects.filter(day_id=pk).values())[0]

        # display not reserved hours in dropdown box
        open_hours = []
                for key in hours.keys():
                    if key == 'T1'and hours[key] == 'open':
                        free_hours.append((key,'5:00-7:00'))
                    elif key == 'T2'and hours[key] == 'open':
                        free_hours.append((key,'7:00-8:00'))
                    elif key == 'T3'and hours[key] == 'open':
                        free_hours.append((key,'8:00-9:00'))
                    elif key == 'T4'and hours[key] == 'open':
                        free_hours.append((key,'9:00-10:00'))
                    elif key == 'T5'and hours[key] == 'open':
                        free_hours.append((key,'10:00-11:00'))
                    elif key == 'T6'and hours[key] == 'open':
                        free_hours.append((key,'11:00-12:00'))
                    elif key == 'T7'and hours[key] == 'open':
                        free_hours.append((key,'12:00-13:00'))
                    elif key == 'T8'and hours[key] == 'open':
                        free_hours.append((key,'13:00-14:00'))
                    elif key == 'T9'and hours[key] == 'open':
                        free_hours.append((key,'14:00-15:00'))
                    elif key == 'T10'and hours[key] == 'open':
                        free_hours.append((key,'15:00-16:00'))
                    elif key == 'T11'and hours[key] == 'open':
                        free_hours.append((key,'16:00-17:00'))
                    elif key == 'T12'and hours[key] == 'open':
                        free_hours.append((key,'17:00-18:00'))
                    elif key == 'T13'and hours[key] == 'open':
                        free_hours.append((key,'18:00-19:00'))
                    elif key == 'T14'and hours[key] == 'open':
                        free_hours.append((key,'19:00-20:00'))
                    elif key == 'T15'and hours[key] == 'open':
                        free_hours.append((key,'20:00-21:00'))
                    elif key == 'T16'and hours[key] == 'open':
                        free_hours.append((key,'21:00-22:00'))
                    elif key == 'T17'and hours[key] == 'open':
                        free_hours.append((key,'22:00-23:00'))
                    elif key == 'T18'and hours[key] == 'open':
                        free_hours.append((key,'23:00-24:00'))

                self.fields['Time_Select'] = forms.ChoiceField(choices = free_hours)