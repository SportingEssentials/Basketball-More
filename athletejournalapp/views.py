from django.shortcuts import render
from .models import Scent, BasketballEssential, Watch


def home(request):

    return render(request, 'home.html')


def essentials(request):
    basketball_essentials = BasketballEssential.objects.all()




    # Add additional attributes as needed
  # Calculate the number of stars for each basketball essential
    for essential in basketball_essentials:
        num_full_stars = int(essential.stars)
        num_half_stars = round((essential.stars - num_full_stars) * 2)
        essential.num_stars = '★' * num_full_stars + '½' * num_half_stars + '☆' * (5 - num_full_stars - num_half_stars)
    
    context = {
        'basketball_essentials': basketball_essentials,
    
        
    }
    return render(request, 'essentials.html', context)


def cologne(request):
    scents = Scent.objects.all()
    context = {
        'scents':scents
    }
    return render(request, 'cologne.html', context)


def injury(request):
    return render(request, 'injury.html')

def watch(request):
    watches = Watch.objects.all()
    context = {
        'watches':watches
    }
    return render(request, 'watch.html', context)


def gamechanger(request):
    return render(request, 'gamechanger.html')

def game(request):
    return render(request, 'game-analyze.html')




def test(points, blocks):
    test_results = points + blocks
    return round(test_results, 1)



def calculate_true_shooting_percentage(points, fga, fta):
    # Calculate True Shooting Percentage (TS%)
    if fta is None or fga is None:
        return None
    else:
        ts_percent = points / ((2 * float(fga)) + (0.88 * float(fta)))
        return round(ts_percent * 100, 1)
    
   
    



def calculate_effective_field_goal(fga, fieldmakes, threepoint):
    if fieldmakes is None or threepoint is None or fga is None:
        return None
        
        
    else:
        efg_percent = 100 * ((float(fieldmakes) + (0.5 * float(threepoint))) / fga)
        return round(efg_percent, 1)




    
#def three_missed(threepercent, threepoint):
    if threepercent is None or threepoint is None:
        return None
    else:
        three_missed = ((threepoint * 100) / threepercent)
        return round(three_missed, 1)
    


def three_missed(threepoint, threepercent):
    if threepoint is None or threepercent == 'null':
        return None
    else:
        threepoint = float(threepoint)
        threepercent = float(threepercent)
        three_missed = ((threepoint * 100) / threepercent) - threepoint
        return round(three_missed, 1)



def fg_missed(fga, fieldmakes):
    if fga is None or fieldmakes is None:
        return None
    else:
        two_missed = (fga - fieldmakes)
        return round(two_missed, 1)

     #real_fg = fieldmakes - threepoint

        

        #real_fg_missed = fg_missed_data - three_missed_data

def stats_input(request):
    if request.method == 'POST':
        # Process the form data
        points = float(request.POST.get('points', 0.0))
        assists = float(request.POST.get('assists', 0.0))
        #steals = int(request.POST.get('steals', 0))
        steals = request.POST.get('steals', '')
       
      
        blocks = float(request.POST.get('blocks', 0))
        rebounds = float(request.POST.get('rebounds', 0))

        turnover = request.POST.get('turnover', '')
        turnover = float(turnover) if turnover.strip() else 'null'


        #shot_percent = float(request.POST.get('shot_percent', 0.0))
        shot_percent = request.POST.get('shot_percent', '')
        shot_percent = float(shot_percent) if shot_percent.strip() else 'null'
        
        
        #ft_percent = float(request.POST.get('ft_percent', 0.0))
        ft_percent = request.POST.get('ft_percent', '')
        ft_percent = float(ft_percent) if ft_percent.strip() else 'null'
        
        
        #threepercent = float(request.POST.get('threepercent', 0.0))
        threepercent = request.POST.get('threepercent', '')
        threepercent = float(threepercent) if threepercent.strip() else 'null'
        

        
        
        #fieldmakes = int(request.POST.get('fieldmakes', 0))
        fieldmakes = request.POST.get('fieldmakes', '')
        fieldmakes = float(fieldmakes) if fieldmakes.strip() else None
        
        
        
        
        # Added turnover stat
        fta = request.POST.get('fta', '')
        fta = float(fta) if fta.strip() else None
        
        
        
        #fga = int(request.POST.get('fga', 0))
        fga = request.POST.get('fga', '')
        fga = float(fga) if fga.strip() else None      
       
        #threepoint = int(request.POST.get('threepoint', 0))
        threepoint = request.POST.get('threepoint', '')
        threepoint = float(threepoint) if threepoint.strip() else None
       

        steals = float(steals) if steals.strip() else None
        
        # Ensure that the data is not None
        if None in [points, assists, blocks]:
            # Handle the error case where data is missing or not provided
            return render(request, 'stats_input.html', {'error': 'Please provide valid values for points, assists, and blocks.'})

        # Calculate strengths and weaknesses
        strengths = []
        weaknesses = []

        if points >= 14:
            strengths.append('Scoring')
        else:
            weaknesses.append('Scoring')

        if assists >= 2:
            strengths.append('Playmaking')
        else:
            weaknesses.append('Playmaking')

        if steals >= 2:
            strengths.append('Steals')
        else:
            weaknesses.append('Steals')

        if blocks >= 1.5:
            strengths.append('Blocks')
        else:
            weaknesses.append('Blocks')

        if rebounds >= 4:
            strengths.append('Rebounding')
        else:
            weaknesses.append('Rebounding')
        if ft_percent != 'null':
            if ft_percent >= 65:
                strengths.append('Free Throw Percent')
            else:
                weaknesses.append('Free Throw Percentage')
        if turnover != 'null':
            if turnover <= 1.5:
                strengths.append('Minimal Turnovers')
            else:
                weaknesses.append('Turnovers')

        # Calculate efficiency metrics
       
        ts_percent = calculate_true_shooting_percentage(points, fga, fta)
    
        efg_percent = calculate_effective_field_goal(fga, fieldmakes, threepoint)

        
        

        three_missed_data = three_missed(threepoint, threepercent)

        fg_missed_data = fg_missed(fga, fieldmakes)

        


        

        

       
       
        
        

        # Process the data and pass it to the template
        data = {
            'points': points,
            'assists': assists,
            'steals': steals,
            'blocks': blocks,
            'rebounds': rebounds,

            'turnover': turnover,
            'shot_percent': shot_percent,
            
            'ft_percent': ft_percent,
            'threepercent': threepercent,
            
            'fieldmakes': fieldmakes,
            'threepoint': threepoint,
            'fga': fga,
            
            
            'strengths': strengths,
            'weaknesses': weaknesses,
            'ts_percent': ts_percent,
            'efg_percent': efg_percent,
            'threepercent': threepercent,
            
            'three_missed_data': three_missed_data,
            'fg_missed_data': fg_missed_data,
            
        }
        return render(request, 'stats_result.html', {'data': data})
    else:
        return render(request, 'stats_input.html')
